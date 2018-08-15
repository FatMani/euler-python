# -*- coding: utf-8 -*-
"""Project Euler: Problem 52

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and
6x, contain the same digits.

https://projecteuler.net/problem=52
"""
import euler


def main() -> int:
    """ Finds first candidate that satisfies requirement.

    Returns:
        First number to contain the same digits as its six multiples.
    """
    candidate = 1
    while True:
        for i in range(2, 7):
            if not euler.is_permutation(candidate, i * candidate):
                break
            if i == 6:
                return candidate
        candidate += 1          


if __name__ == "__main__":
    print(main())
