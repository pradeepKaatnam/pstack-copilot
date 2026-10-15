#!/usr/bin/env python3
"""Install/update generated project skill snapshots, refusing local modifications."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil

SOURCE = Path(__file__).resolve().parents[1] / "copilot/skills"


def fingerprint(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def install(project, update=False):
    """Only manage recorded skill files; never overwrite unrelated project skills."""
    project = project.resolve()
    base = project / ".github/skills"
    state = project / ".github/pstack-installed.json"
    license_path = project / ".github/pstack-LICENSE"
    if any(p.is_symlink() for p in (project / ".github", base, state, license_path)):
        raise ValueError("Refusing symlinked project discovery/state directories")
    previous = json.loads(state.read_text()) if state.exists() else {}
    if previous and not update:
        raise ValueError("Already installed; use --update to refresh a managed snapshot")
    if license_path.exists():
        if not previous.get("license_sha256") or fingerprint(license_path) != previous["license_sha256"]:
            raise ValueError(f"Unmanaged or modified license: {license_path}")
    license_source = SOURCE.parent / "LICENSE"
    if not license_source.is_file():
        raise ValueError("Missing upstream MIT license; refusing incomplete installation")
    old_files = previous.get("files", {})
    skills = [p for p in SOURCE.iterdir() if p.is_dir()]
    new_files = {
        f"{skill.name}/{p.relative_to(skill).as_posix()}": p
        for skill in skills for p in skill.rglob("*") if p.is_file()
    }
    # Validate the entire operation before writing anything.
    for relative, digest in old_files.items():
        parts = Path(relative).parts
        if Path(relative).is_absolute() or ".." in parts or len(parts) < 2:
            raise ValueError(f"Invalid recorded skill path: {relative}")
        target = base / relative
        if any(p.is_symlink() for p in (target, *target.parents)) or not target.is_file():
            raise ValueError(f"Missing or symlinked managed file: {target}")
        if fingerprint(target) != digest:
            raise ValueError(f"Locally modified file; preserve/reconcile it first: {target}")
    for skill in skills:
        destination = base / skill.name
        if destination.exists() or destination.is_symlink():
            if destination.is_symlink() or not destination.is_dir():
                raise ValueError(f"Refusing conflicting skill path: {destination}")
            actual = {p.relative_to(base).as_posix() for p in destination.rglob("*") if p.is_file() or p.is_symlink()}
            expected = {p for p in old_files if p.startswith(skill.name + "/")}
            if actual != expected or not expected:
                raise ValueError(f"Unmanaged skill conflict: {destination}")
    for relative in set(old_files) - set(new_files):
        (base / relative).unlink()
    for relative, source in new_files.items():
        target = base / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    state.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(license_source, license_path)
    state.write_text(json.dumps({
        "source": "pradeepKaatnam/pstack-copilot:copilot/skills",
        "upstream_commit": "e5136d82418d2db3165ea1050d17577cd618cc05",
        "port_version": json.loads((SOURCE.parent / "plugin.json").read_text())["version"],
        "license_sha256": fingerprint(license_source),
        "files": {relative: fingerprint(source) for relative, source in new_files.items()},
    }, indent=2) + "\n")
    print(f"Installed {len(skills)} managed skill snapshots into {base}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--update", action="store_true")
    arguments = parser.parse_args()
    try:
        install(arguments.project, arguments.update)
    except (ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")
