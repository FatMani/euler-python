# -*- coding: utf-8 -*-
"""Project Euler: Problem 60

Find the lowest sum for a set of five primes for which any two
primes concatenate to produce another prime.

https://projecteuler.net/problem=60
"""
import euler
import itertools
from typing import List


def pair(a: int, b: int) -> bool:
    """Checks if combinations of numbers are prime

    Args:
        a: first nuber to check
        b: second number to check

    Returns:
        True if both permutations are prime
    """
    return euler.is_prime(int(str(a) + str(b))) and euler.is_prime(int(str(b) + str(a)))


def main():
    primes = euler.primes_less_than(10000)
    primes.remove(2)
    primes.remove(5)
    for a in primes:
        for b in primes:
            if b > a and pair(a, b):
                for c in primes:
                    if c > b and pair(c, a) and pair(c, b):
                        for d in primes:
                            if d > c and pair(d, a) and pair(d, b) and pair(d, c):
                                for e in primes:
                                    if e > d and pair(e, a) and pair(e, b) and pair(e, c) and pair(e, d):
                                        return ([a, b, c, d, e], a + b + c + d + e)


if __name__ == "__main__":
    print(main())
