# -*- coding: utf-8 -*-
"""Project Euler: Problem 69

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum, where
φ(n) is the Euler totient function.

https://projecteuler.net/problem=69
"""
import euler
from functools import reduce


def totient_ratio(n: int) -> float:
    """Returns the totient ratio n/φ(n) from Euler's mutliplicative formula.

    Args:
        n: number to compute

    Returns:
        Float of the ratio
    """
    return 1 / reduce(lambda x, y: x * y, [(1 - 1 / p) for p in euler.unique_prime_factors(n)])


def main():
    ratios = [totient_ratio(n) for n in range(2, 10 ** 6 + 1)]
    print(ratios.index(max(ratios)) + 2)


if __name__ == "__main__":
    main()
