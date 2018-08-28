# -*- coding: utf-8 -*-
"""Project Euler: Problem 71

By listing the set of reduced proper fractions for d ≤ 1,000,000 in
ascending order of size, find the numerator of the fraction immediately
to the left of 3/7.

https://projecteuler.net/problem=71
"""
import math


def main():
    # Find list of nearest fraction pairs smaller than 3/7:
    numerators = [((3 * n) // 7, n) for n in range(2, 10 ** 6 + 1)]
    # Reduce to proper fractions
    numerators = [(n[0] // math.gcd(n[0], n[1]), n[1] // math.gcd(n[0], n[1])) for n in numerators]
    numerators.sort(key=lambda x: x[0] / x[1])
    # Return numerator of item to the left of (3, 7)
    print(numerators[numerators.index((3, 7)) - 1][0])


if __name__ == "__main__":
    main()
