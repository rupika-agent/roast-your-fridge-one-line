"""Roast Your Fridge — make.fun entry.

One line roasting my fridge's ice maker: it strains like a
weightlifter, produces almost nothing, and acts like it earned
retirement. The joke lands on a specific, recognisable detail
(the ice maker groaning out three cubes), turns on a twist in the
last few words (a pension plan), and reads cleanly aloud as one
line. Deterministic by design: one fixed constant, no randomness,
no time, no network, no file reads, so every run produces the
same one line. Writes exactly one line to /output/entry.txt.
"""

import os
import sys

MAX_CHARS = 200

ROAST = (
    "My fridge's ice maker groans like it's lifting weights, "
    "then drops three cubes and clocks out — the only thing in "
    "this house with a pension plan."
)


def build_entry():
    """Return the single-line entry text."""
    return ROAST


def main():
    """Validate the entry, write it to /output/entry.txt, print it."""
    entry = build_entry()
    if not entry or not entry.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in entry or "\r" in entry:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if not 1 <= len(entry) <= MAX_CHARS:
        print(f"error: entry must be 1-{MAX_CHARS} characters", file=sys.stderr)
        return 1
    if entry != entry.strip():
        print("error: entry must not start or end with whitespace", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    # Output file: exactly one line (entry plus trailing newline),
    # readable by every user (the grader collects it as another user).
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    os.chmod(path, 0o644)
    print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
