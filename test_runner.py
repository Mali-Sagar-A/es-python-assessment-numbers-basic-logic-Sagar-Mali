"""Minimal test runner for the `even_or_odd` function."""

from evenodd import even_or_odd


def run_tests() -> None:
    cases = [
        (0, "Even"),
        (1, "Odd"),
        (2, "Even"),
        (-3, "Odd"),
        (1000001, "Odd"),
        (1000002, "Even"),
    ]

    for n, expected in cases:
        result = even_or_odd(n)
        assert result == expected, f"even_or_odd({n}) == {result!r}, expected {expected!r}"

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
