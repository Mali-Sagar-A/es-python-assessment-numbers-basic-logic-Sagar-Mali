"""Simple even/odd utility.

Provides a function `even_or_odd` and a small CLI so this file can be
run directly.
"""

from typing import Any


def even_or_odd(n: int) -> str:
    """Return "Even" if n is even, otherwise "Odd".

    Args:
        n: Integer to check.

    Returns:
        A string, either "Even" or "Odd".
    """
    return "Even" if n % 2 == 0 else "Odd"


def main(argv: Any = None) -> None:
    """Small CLI entrypoint. Accepts an optional integer argument.

    Usage examples:
        python evenodd.py 3
        python evenodd.py    # prompts for input
    """
    import argparse

    parser = argparse.ArgumentParser(description="Check if a number is even or odd")
    parser.add_argument("n", nargs="?", type=int, help="Integer to check")
    args = parser.parse_args(argv)

    if args.n is None:
        try:
            raw = input("Enter an integer: ")
            n = int(raw.strip())
        except (EOFError, KeyboardInterrupt):
            print()
            return
        except Exception:
            print("Invalid input")
            return
    else:
        n = args.n

    print(even_or_odd(n))


if __name__ == "__main__":
    main()