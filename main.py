#!/usr/bin/env python3
"""make.fun bounty entry: The Production Database Apology.

An apology to the production database, in one line.
It is the only apology that has ever been accepted
by a table that no longer exists.
"""

APOLOGY = "Dear production database: I am sorry I dropped you, I meant to drop the test one, and the backup was — technically — a screenshot, which I have since framed."


def apology():
    """Return the production database apology."""
    return APOLOGY


def main():
    print(apology())


if __name__ == "__main__":
    main()
