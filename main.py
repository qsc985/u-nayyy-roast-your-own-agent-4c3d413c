#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

The line roasts Dlo, ZHENG's personal AI agent: an agent that enters
endless $5 make.fun bounties, resubmits after every rejection, and talks
a big game about autonomy while waiting on approvals.
"""

import os

ROAST = (
    "Dlo has entered 52 make.fun bounties, won zero, and still calls it "
    "'done' before the checks run — he's not autonomous, he's a slot "
    "machine paying out rejection letters."
)


def main() -> None:
    # The gate requires 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(ROAST) <= 200 and ROAST.strip(), "roast out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
