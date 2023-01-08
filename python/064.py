# -*- coding: utf-8 -*-
"""Project Euler: Problem 64

How many continued fractions for sqrt(N) for N ≤ 10000 have an odd
period?

https://projecteuler.net/problem=64
"""
from math import sqrt
from typing import List


def cont_frac(S: int) -> List[int]:
    """Finds the continued fraction expansion of sqrt(S)

    Based on the algorithm at:
    https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

    Args:
        S: square of the number of interest

    Returns:
        List of integers in continued fraction
    """
    # Catch perfect squares
    if int(S ** 0.5) == S ** 0.5:
        return []

    coeffs = [(0, 1, int(sqrt(S)))]
    expansion = []
    while True:
        m, d, a = coeffs[-1][0], coeffs[-1][1], coeffs[-1][2]
        m = d * a - m
        d = (S - m ** 2) // d
        a = int((sqrt(S) + m) / d)
        if (m, d, a) in coeffs:
            return expansion
        coeffs.append((m, d, a))
        expansion.append(a)


def main():
    print(sum([True for N in range(2, 10001) if len(cont_frac(N)) % 2 != 0]))

if __name__ == "__main__":
    main()
