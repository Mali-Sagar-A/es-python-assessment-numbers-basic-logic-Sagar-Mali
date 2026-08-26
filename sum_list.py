

from typing import Iterable


def add_all(numbers: Iterable[int]) -> int:
    
    total = 0
    for n in numbers:
        total += n
    return total


if __name__ == "__main__":
    # simple manual demo
    print(add_all([1, 2, 3, 4, 5]))
