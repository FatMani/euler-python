# -*- coding: utf-8 -*-
"""Project Euler: Problem 87

How many numbers below fifty million can be expressed as the sum of a
prime square, prime cube, and prime fourth power?

https://projecteuler.net/problem=87
"""
from euler import primes_less_than


def main():
    limit = 50_000_000
    primes_squared = primes_less_than(int(limit ** (1 / 2)))
    primes_cubed = primes_less_than(int(limit ** (1 / 3)))
    primes_fourth = primes_less_than(int(limit ** (1 / 4)))
    solutions = set()

    for a in primes_squared:
        for b in primes_cubed:
            for c in primes_fourth:
                s = a ** 2 + b ** 3 + c ** 4
                if s < limit:
                    solutions.add(s)
    print(len(solutions))


if __name__ == "__main__":
    main()
