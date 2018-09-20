# -*- coding: utf-8 -*-
"""Project Euler: Problem 92

A number chain is created by continuously adding the square of the
digits in a number to form a new number until it has been seen before.
How many starting numbers below ten million will arrive at 89?

https://projecteuler.net/problem=92
"""
from typing import Dict


def sq_dig(n: int) -> int:
    """Calculates the sum of the squares of the digits of n.

    Args:
        n: number to calculate

    Returns:
        Sum of squares of digits
    """
    return sum(int(d) ** 2 for d in str(n))


def chain(n: int, _cache: Dict[int, int]={1: 1, 89: 89}) -> int:
    """Finds the looping element of a square digit sum

    Args:
        n: number to check
        _cache: internal memoization dictionary

    Returns:
        Either 89 or 1 for valid inputs, 0 for invalid
    """
    if n < 1:
        return 0
    if n in _cache:
        return _cache[n]
    else:
        _cache[n] = chain(sq_dig(n))
        return _cache[n]


def main():
    c = [True for n in range(10_000_000 + 1) if chain(n) == 89]
    print(sum(c))


if __name__ == "__main__":
    main()
