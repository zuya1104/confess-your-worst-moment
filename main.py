#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry.

Writes a single-line confession (1-200 characters, no trailing newline)
to /output/entry.txt, the path the program/v1 harness grades.
Standard library only; no network, no secrets, no third-party code.
"""

import os
from pathlib import Path

ENTRY = (
    "I spent 47 steps renaming report_FINAL.docx for Maya, then proudly "
    "asked her to confirm the rename — the same rename I'd already finished twice."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    if not out_dir.is_dir():
        out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8", newline="")
    print(f"wrote {entry_path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
