#!/usr/bin/env python3
"""Offline preservation, mapping, and packaging checks; standard library only."""

import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys

ROOT = Path(__file__).resolve().parents[1]
PIN = "e5136d82418d2db3165ea1050d17577cd618cc05"
TREE = "de8e53ebbeca0fe9351e950095e720655da08349"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def contents(path):
    return os.fsencode(os.readlink(path)) if path.is_symlink() else path.read_bytes()


def mode(path):
    if path.is_symlink():
        return "120000"
    return "100755" if path.stat().st_mode & stat.S_IXUSR else "100644"


def git_hash(kind, data):
    return hashlib.sha1(f"{kind} {len(data)}\0".encode() + data).hexdigest()


def tree_hash(entries):
    tree = {}
    for entry in entries:
        parts = entry["path"].split("/")
        node = tree
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = (entry["mode"], entry["git_blob"])

    def digest(node):
        rows = []
        for name, value in node.items():
            directory = isinstance(value, dict)
            rows.append((
                name + ("/" if directory else ""),
                ("40000" if directory else value[0]).encode()
                + b" " + name.encode() + b"\0"
                + bytes.fromhex(digest(value) if directory else value[1]),
            ))
        return git_hash("tree", b"".join(data for _, data in sorted(rows)))

    return digest(tree)


def files_under(directory):
    return {
        p.relative_to(directory).as_posix(): p
        for p in directory.rglob("*") if p.is_file() or p.is_symlink()
    }


def safe_path(relative):
    path = Path(relative)
    require(not path.is_absolute() and ".." not in path.parts, f"Unsafe path: {relative}")
    return ROOT / path


def audit_rows():
    rows = []
    for name in ("supporting-skills", "orchestration", "non-skills"):
        rows.extend(json.loads((ROOT / "audit" / f"{name}.json").read_text()))
    return rows


def changes(source, target):
    a = source.read_bytes().decode("utf-8").splitlines(keepends=True)
    b = target.read_bytes().decode("utf-8").splitlines(keepends=True)
    result = []
    for tag, i, j, k, l in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag != "equal":
            result.append({
                "source_start": i + 1, "source_end": j,
                "original": "".join(a[i:j]),
                "target_start": k + 1, "target_end": l,
                "replacement": "".join(b[k:l]),
            })
    return result


def verify():
    provenance = json.loads((ROOT / "audit/provenance.json").read_text())
    require(provenance["commit"] == PIN, "Unexpected upstream revision")
    require(provenance["source_tree"] == TREE, "Unexpected upstream tree")
    entries = provenance["files"]
    require(len(entries) == 169, "Incomplete pinned inventory")
    require(len({x["path"] for x in entries}) == len(entries), "Duplicate inventory paths")
    require(tree_hash(entries) == TREE, "Inventory does not reconstruct pinned Git tree")
    archive = ROOT / "upstream/pstack"
    require(set(files_under(archive)) == {x["path"] for x in entries}, "Archive path mismatch")
    for entry in entries:
        path = archive / entry["path"]
        data = contents(path)
        require(mode(path) == entry["mode"], f"Mode changed: {path}")
        require(len(data) == entry["size"], f"Size changed: {path}")
        require(hashlib.sha256(data).hexdigest() == entry["sha256"], f"Bytes changed: {path}")
        require(git_hash("blob", data) == entry["git_blob"], f"Blob changed: {path}")

    rows = audit_rows()
    require(len(rows) == len(entries), "One audit row per upstream file required")
    require({r["source"] for r in rows} == set(files_under(archive)), "Unclassified/duplicate files")
    evidence = json.loads((ROOT / "audit/passages.json").read_text())
    docs = json.loads((ROOT / "audit/documentation.json").read_text())
    doc_ids = {record["id"] for record in docs}
    require(len(doc_ids) == len(docs), "Duplicate documentation IDs")
    for record in docs:
        require(record["retrieved"] == "2026-10-15", f"Missing retrieval date: {record}")
        require(record["url"].startswith(("https://docs.github.com/", "https://code.visualstudio.com/",
                                          "https://learn.microsoft.com/",
                                          "https://github.com/microsoft/vscode-docs/")), f"Nonofficial evidence: {record}")
    require({r["source"] for r in evidence} == {r["source"] for r in rows}, "Passage coverage mismatch")
    evidence = {r["source"]: r for r in evidence}
    for row in rows:
        source = archive / row["source"]
        target = safe_path(row["target"])
        require(target.exists(), f"Missing counterpart: {target}")
        require(row["disposition"] in ("adapted", "unchanged", "inactive"), f"Bad disposition: {row}")
        require(bool(row["review"].strip()), f"Missing full-content review: {source}")
        require(set(row["hosts"]) == {"cli", "vscode", "cloud"}, f"Host applicability missing: {source}")
        if row["disposition"] == "inactive":
            require(target == source, f"Inactive source must remain archive-only: {source}")
        elif row["disposition"] == "unchanged":
            require(contents(source) == contents(target), f"Unrecorded adaptation: {source}")
            require(mode(source) == mode(target), f"Counterpart mode lost: {target}")
        else:
            require(target.is_relative_to(ROOT / "copilot"), f"Adapted target outside package: {target}")
            require(mode(source) == mode(target), f"Adapted counterpart mode lost: {target}")
        record = evidence[row["source"]]
        require(record["reason"] == row["review"], f"Stale passage reason: {source}")
        require(record["hosts"] == row["hosts"], f"Stale host evidence: {source}")
        require(record["documentation"] and set(record["documentation"]) <= doc_ids,
                f"Missing official evidence: {source}")
        if row["disposition"] == "adapted":
            actual = changes(source, target)
            core = [{k: p[k] for k in actual[0]} for p in record["passages"]] if actual else []
            require(core == actual and len(record["passages"]) == len(actual), f"Stale exact-text diff: {source}")
            for passage in record["passages"]:
                require(passage["reason"] == row["review"] and passage["hosts"] == row["hosts"]
                        and passage["documentation"] == record["documentation"], f"Stale passage rationale: {source}")
        elif row["disposition"] == "inactive":
            try:
                text = source.read_bytes().decode("utf-8")
            except UnicodeDecodeError:
                text = None
            require(record["original"] == text, f"Inactive original evidence mismatch: {source}")

    manifest = json.loads((ROOT / "copilot/plugin.json").read_text())
    require(manifest["skills"] == "skills/" and manifest["agents"] == "agents/", "Discovery escaped package")
    require("$schema" not in manifest, "Legacy manifest cannot use Agent Plugins schema with path overrides")
    require(not any(k in manifest for k in ("hooks", "mcpServers", "commands")), "Unexpected active integration")
    package = ROOT / "copilot"
    for path in package.rglob("*"):
        require(not path.is_symlink(), f"Unexpected package symlink: {path}")
        require(path.name not in (".cursor-plugin", ".cursor", "upstream"), f"Archive/discovery leak: {path}")
    skills = list((package / "skills").glob("*/SKILL.md"))
    require(len(skills) == 54, f"Expected 54 upstream top-level skills, got {len(skills)}")
    for skill in skills:
        text = skill.read_text()
        require(text.startswith("---\n"), f"Missing skill metadata: {skill}")
        metadata = text.split("---", 2)[1]
        require(re.search(rf"^name: ['\"]?{re.escape(skill.parent.name)}['\"]?$", metadata, re.M),
                f"Nonportable skill name: {skill}")
        require(re.search(r"^description:\s*\S", metadata, re.M), f"Missing description: {skill}")
        require(not re.search(r"^(icon|color|is_background):", metadata, re.M), f"Cursor metadata: {skill}")
    for path in (package / "agents").glob("*.agent.md"):
        require("is_background:" not in path.read_text(), f"Cursor background agent: {path}")
    # Relative Markdown links are checked on installed counterparts, never in the archive.
    for path in package.rglob("*.md"):
        for link in re.findall(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)", path.read_text()):
            if "://" in link or link.startswith(("#", "mailto:", "/")) or any(c in link for c in "<>{}"):
                continue
            destination = link.split("#", 1)[0]
            if destination:
                resolved = (path.parent / destination).resolve()
                require(resolved.is_relative_to(package), f"Link escapes installed package in {path}: {link}")
                require(resolved.exists(), f"Broken relative link in {path}: {link}")
                if path.is_relative_to(package / "skills"):
                    require(resolved.is_relative_to(package / "skills"),
                            f"Link escapes managed project skills in {path}: {link}")
    print(f"Verified {len(entries)} pinned files, {len(rows)} audit rows, {len(skills)} skills.")


if __name__ == "__main__":
    try:
        verify()
    except (ValueError, KeyError, OSError) as error:
        print(f"Verification failed: {error}", file=sys.stderr)
        sys.exit(1)
