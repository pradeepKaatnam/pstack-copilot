#!/usr/bin/env python3
"""Refresh mechanical evidence, never substitute for the per-file human/agent audit."""

import hashlib
import json
from pathlib import Path
import subprocess

from verify import ROOT, PIN, TREE, audit_rows, changes, contents


def write(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def main():
    # Exact pinned commit must be present; no network access or moving-ref fallback.
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-tree", "-rzl", PIN, "--", "pstack"],
        check=True, capture_output=True,
    )
    files = []
    for record in result.stdout.split(b"\0"):
        if not record:
            continue
        fields, path = record.split(b"\t", 1)
        mode, kind, blob, size = fields.decode().split()
        relative = path.decode().removeprefix("pstack/")
        data = contents(ROOT / "upstream/pstack" / relative)
        files.append({
            "path": relative, "type": kind, "mode": mode, "size": int(size),
            "git_blob": blob, "sha256": hashlib.sha256(data).hexdigest(),
            "encoding": "utf-8" if is_text(data) else "binary",
        })
    write(ROOT / "audit/provenance.json", {
        "repository": "https://github.com/cursor/plugins",
        "commit": PIN, "source_path": "pstack", "source_tree": TREE,
        "commit_date": "2026-10-15T05:36:44Z",
        "upstream_version": "0.15.25", "retrieved": "2026-10-15",
        "license": "MIT", "copyright": "Copyright (c) 2026 Lauren Tan",
        "archive": "upstream/pstack", "files": files,
    })
    documentation = json.loads((ROOT / "audit/documentation.json").read_text())
    records = []
    rows = audit_rows()
    for row in rows:
        source = ROOT / "upstream/pstack" / row["source"]
        record = {
            "source": row["source"], "target": row["target"],
            "disposition": row["disposition"], "reason": row["review"],
            "hosts": row["hosts"],
            "documentation": [d["id"] for d in documentation],
        }
        if row["disposition"] == "adapted":
            record["passages"] = changes(source, ROOT / row["target"])
            for passage in record["passages"]:
                passage["reason"] = row["review"]
                passage["documentation"] = record["documentation"]
                passage["hosts"] = row["hosts"]
        elif row["disposition"] == "inactive":
            data = contents(source)
            record["original"] = data.decode() if is_text(data) else None
            record["source_start"] = 1
            record["source_end"] = len(data.splitlines()) if is_text(data) else None
            record["replacement"] = None
            record["unsupported_state"] = "Not installed, discovered, or executed; archive-only."
        else:
            record["passages"] = []
        records.append(record)
    write(ROOT / "audit/passages.json", sorted(records, key=lambda r: r["source"]))
    lines = [
        "FULL FILE AUDIT — pinned cursor/plugins pstack 0.15.25",
        f"Commit: {PIN}", "Source archive is evidence, not executable agent instructions.",
        "Exact changed/inactive passages: passages.json; official evidence: documentation.json.",
        "",
    ]
    for row in sorted(rows, key=lambda r: r["source"]):
        lines.extend([
            row["source"], f"  {row['disposition']} -> {row['target']}",
            f"  Full-content review: {row['review']}",
            *(f"  {host}: {state}" for host, state in row["hosts"].items()), "",
        ])
    (ROOT / "audit/files.txt").write_text("\n".join(lines))


def is_text(data):
    try:
        data.decode("utf-8")
        return b"\0" not in data
    except UnicodeDecodeError:
        return False


if __name__ == "__main__":
    main()
