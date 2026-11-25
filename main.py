"""Snooze Button Roast entry.

Writes one line roasting an alarm clock for ringing at 6 AM on a
Saturday morning to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for local testing). Standard library only, no network, deterministic.
"""

import os

ENTRY = (
    "My alarm rang at 6 AM on a Saturday like a rooster that got fired "
    "from the farm and took it personally."
)

# The gate requires 1-200 characters of non-whitespace text.
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails the gate"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
