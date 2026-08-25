"""Utilities for summing lists."""

from typing import Iterable


def add_all(numbers: Iterable[int]) -> int:
    """Return the sum of `numbers` using an explicit loop and accumulator.

    Args:
        numbers: An iterable of integers.

    Returns:
        The total sum as an int (0 for empty iterable).
    """
    total = 0
    for n in numbers:
        total += n
    return total


if __name__ == "__main__":
    # simple manual demo
    print(add_all([1, 2, 3, 4, 5]))
