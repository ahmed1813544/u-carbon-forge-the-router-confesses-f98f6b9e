#!/usr/bin/env python3
"""The Router Confesses -- make.fun entry.

Writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
the home Wi-Fi router's excuse for dropping the connection at the exact
climax of a movie. Stdlib only, deterministic.

The line is a petty little grudge: the router remembers being unplugged
mid-sentence years ago and returns the favour at the worst possible moment.
"""

import os

LINE = "You unplugged me mid-sentence in 2019. Tonight, right at the climax, I returned the favour."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
