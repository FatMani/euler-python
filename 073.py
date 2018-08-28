# -*- coding: utf-8 -*-
"""Project Euler: Problem 73

How many reduced proper fractions for d ≤ 12,000 are there, where
the fraction lies between 1/3 and 1/2?

https://projecteuler.net/problem=73
"""
import math


def main():
    # Brute force approach
    candidates = [(n, d) for d in range(2, 12001) for n in range(1, d) if (n / d > 1 / 3 and n / d < 1 / 2)]
    candidates = [(c[0] // math.gcd(c[0], c[1]), c[1] // math.gcd(c[0], c[1])) for c in candidates]
    print(len(set(candidates)))


if __name__ == "__main__":
    main()
