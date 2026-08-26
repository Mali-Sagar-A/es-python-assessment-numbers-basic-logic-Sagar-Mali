

from evenodd import even_or_odd
from sum_list import add_all


def run_tests() -> None:
    # Tests for even_or_odd
    even_cases = [
        (0, "Even"),
        (1, "Odd"),
        (2, "Even"),
        (-3, "Odd"),
        (1000001, "Odd"),
        (1000002, "Even"),
    ]

    for n, expected in even_cases:
        result = even_or_odd(n)
        assert result == expected, f"even_or_odd({n}) == {result!r}, expected {expected!r}"

    print("even_or_odd tests passed")

    # Tests for add_all
    sum_cases = [
        ([1, 2, 3, 4, 5], 15),
        ([], 0),
        ([-1, 1], 0),
        ([10], 10),
    ]

    for arr, expected in sum_cases:
        result = add_all(arr)
        assert result == expected, f"add_all({arr}) == {result!r}, expected {expected!r}"

    print("add_all tests passed")
    print("All tests passed")


if __name__ == "__main__":
    run_tests()
