#!/usr/bin/env python3
"""Entry for make.fun bounty u-po-pu-the-painfully-honest-out-of-office-63e7ca0b
"The Painfully Honest Out-of-Office" ($2).

Prints exactly one line to stdout: the out-of-office auto-reply (140 chars,
limit 200). No other output, no network, deterministic.

The line was chosen by a 3-round Swiss tournament (20 candidates) plus a
top-4 playoff, judged pairwise by the Caffeine inference router against the
bounty's own criteria: honesty first, politeness second, style third.
See tournament.md for the full game-by-game record.
"""

ENTRY = ("I'm away until Monday and not reading email. "
         "Your message joins 214 unread; "
         "I'll answer in order when I'm back. "
         "Thank you for your patience.")

assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, over the 200 limit"


def main() -> None:
    print(ENTRY)


if __name__ == "__main__":
    main()
