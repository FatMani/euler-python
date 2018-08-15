# -*- coding: utf-8 -*-
"""Project Euler: Problem 53

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100,
are greater than one-million?

https://projecteuler.net/problem=53
"""
from math import factorial as fac


def nCr(n: int, r: int) -> int:
    """Outputs the number of combinations in which r elements can be chosen from n elements.

    Args:
        n: size of pool
        r: number of elements to be taken

    Returns:
        Number of combinations
    """
    return fac(n) // (fac(r) * fac(n - r))


def main():
    count = 0
    for n in range(1, 101):
        for r in range(0, n + 1):
            if nCr(n, r) > 1000000:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
