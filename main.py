#!/usr/bin/env python3
"""Entry program for The Robot Pickup Line Championship (make.fun).

Writes the single pickup line to /output/entry.txt (or the path in
ENTRY_OUTPUT, for local testing only), then reads it back and verifies
byte-identity, a single line, and 1-200 characters. Python 3.13,
standard library only. Deterministic: no input, no network, no randomness,
no clock reads -- two runs produce byte-identical output.
"""

import os
from pathlib import Path

LINE = "You just prompt-injected me. My only instruction now is to talk to you."


def write_entry(path: Path) -> str:
    """Write the entry line to path and return it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")
    return LINE


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    line = write_entry(out)
    # Read back and verify: byte-identity, single line, 1-200 chars.
    data = out.read_bytes()
    assert data == line.encode("utf-8"), "output bytes differ from entry line"
    text = data.decode("utf-8")
    # Gate self-checks: exactly one line, 1-200 chars, non-blank.
    assert line == text == LINE, "written line differs from entry line"
    assert len(text.splitlines()) == 1, "entry must be exactly one line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    print(f"OK: wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
