#!/usr/bin/env python3
"""Package a research-project handoff as a minimal recoverable workspace."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path

SECRET_NAME_RE = re.compile(
    r"(^|[._-])(\.env|env|secret|secrets|token|tokens|credential|credentials|private[-_]?key|id_rsa|id_ed25519)([._-]|$)",
    re.IGNORECASE,
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def is_obvious_secret(path: Path) -> bool:
    name = path.name
    lower = name.lower()
    if lower in {".env", ".env.local", ".env.production", ".env.development"}:
        return True
    if lower.endswith((".pem", ".p12", ".pfx", ".key")):
        return True
    return bool(SECRET_NAME_RE.search(name))


def normalize_include(root: Path, raw: str) -> tuple[Path, str]:
    given = Path(raw)
    full = given.resolve() if given.is_absolute() else (root / given).resolve()
    try:
        rel = full.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"Include path escapes workspace root: {raw}") from exc
    if not full.exists():
        raise FileNotFoundError(f"Missing include: {raw}")
    if not full.is_file():
        raise ValueError(f"Include must be a file, not a directory: {raw}")
    if full.is_symlink():
        raise ValueError(f"Symlink includes are not allowed: {raw}")
    if is_obvious_secret(full):
        raise ValueError(f"Refusing obvious secret-bearing file: {raw}")
    return full, rel.as_posix()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace-root", required=True)
    ap.add_argument("--handoff", required=True)
    ap.add_argument("--include", action="append", default=[])
    ap.add_argument("--evidence-chain", default=None, help="Optional EXPERIMENT_EVIDENCE_CHAIN.md requested by the user")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    root = Path(args.workspace_root).resolve()
    handoff = Path(args.handoff).resolve()
    output = Path(args.output).resolve()
    if not root.is_dir():
        raise SystemExit(f"Workspace root is not a directory: {root}")
    if not handoff.is_file():
        raise SystemExit(f"HANDOFF.md not found: {handoff}")
    if is_obvious_secret(handoff):
        raise SystemExit("HANDOFF.md filename unexpectedly matched secret filter")

    entries: list[tuple[Path, str]] = [(handoff, "HANDOFF.md")]
    seen = {"HANDOFF.md"}
    if args.evidence_chain:
        evidence = Path(args.evidence_chain).resolve()
        if not evidence.is_file():
            raise SystemExit(f"Evidence-chain file not found: {evidence}")
        if is_obvious_secret(evidence):
            raise SystemExit("Evidence-chain filename unexpectedly matched secret filter")
        entries.append((evidence, "EXPERIMENT_EVIDENCE_CHAIN.md"))
        seen.add("EXPERIMENT_EVIDENCE_CHAIN.md")
    for raw in args.include:
        full, arc = normalize_include(root, raw)
        if arc in seen:
            raise SystemExit(f"Duplicate archive path: {arc}")
        seen.add(arc)
        entries.append((full, arc))

    manifest_files = [
        {
            "archive_path": arc,
            "source_path": str(path),
            "size_bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path, arc in entries
    ]
    manifest = {
        "format": "research-handoff-manifest-v1",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "workspace_root": str(root),
        "file_count": len(manifest_files),
        "files": manifest_files,
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path, arc in entries:
            zf.write(path, arc)
        zf.writestr("HANDOFF_MANIFEST.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    with zipfile.ZipFile(output, "r") as zf:
        bad = zf.testzip()
        if bad:
            raise SystemExit(f"ZIP CRC verification failed at: {bad}")
        names = set(zf.namelist())
        if "HANDOFF.md" not in names or "HANDOFF_MANIFEST.json" not in names:
            raise SystemExit("Archive verification failed: required handoff files missing")

    print(json.dumps({
        "status": "PASS",
        "output": str(output),
        "files": len(entries),
        "archive_bytes": output.stat().st_size,
        "sha256": sha256(output),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())