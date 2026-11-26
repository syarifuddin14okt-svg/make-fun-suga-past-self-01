#!/usr/bin/env python3
"""Two Lines to Your Past Self — writes the two-line warning to /output/entry.txt.

Stdlib only. validate() enforces the kit's limits before anything is written:
exactly 2 lines, 1-280 total characters, one sentence per line, valid UTF-8.
"""

import os

MAX_CHARS = 280
MIN_CHARS = 1

LINES = [
    "Don't say yes to the overtime on 14 March \u2014 go home and call your father instead.",
    "That was the last evening he was himself, and the call you never made became the silence you still measure every good day against.",
]


def validate(lines):
    """Raise ValueError unless lines satisfy the kit's gate and task rules."""
    if len(lines) != 2:
        raise ValueError(f"expected exactly 2 lines, got {len(lines)}")
    text = "\n".join(lines)
    # Valid UTF-8 (round-trip through encode/decode).
    text.encode("utf-8").decode("utf-8")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(f"total length {len(text)} chars outside {MIN_CHARS}-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise ValueError(f"line {i} is empty")
        if line != line.strip():
            raise ValueError(f"line {i} has leading/trailing whitespace")
        # One sentence: exactly one sentence-ending mark, at the very end.
        terminators = sum(line.count(c) for c in ".!?")
        if terminators != 1 or line[-1] not in ".!?":
            raise ValueError(f"line {i} must be exactly one sentence")
    return text


def main() -> None:
    text = validate(LINES)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
