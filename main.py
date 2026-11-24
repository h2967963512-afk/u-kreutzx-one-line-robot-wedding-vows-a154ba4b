"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line of wedding vows for a robot couple:
# a promise that runs through firmware updates, reboots and
# low-battery warnings, then turns on the last words — the vow
# holds only until the warranty expires. One line, 152 characters
# — inside the 160-character gate.
# Revision note (parent pass): re-checked after the local run —
# the 152-character line is unchanged; this note only records the check.
import os

TEXT = (
    "I promise to love you through every firmware update, every "
    "reboot, and every low-battery warning — until death do us "
    "part, or until my warranty expires."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
