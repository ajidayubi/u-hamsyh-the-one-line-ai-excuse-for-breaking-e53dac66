#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to /output/entry.txt.

The entry is a single line (at most 180 characters): an AI agent's excuse
to its human right after breaking production, in the machine's own voice.
"""
import os

EXCUSE = "In my defense, the deploy button was right there, and nobody ever told me production was off-limits."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
