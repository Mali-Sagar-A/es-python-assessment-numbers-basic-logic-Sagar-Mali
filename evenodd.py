

from typing import Any


def even_or_odd(n: int) -> str:
    
    return "Even" if n % 2 == 0 else "Odd"


def main(argv: Any = None) -> None:
   
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