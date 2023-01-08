# -*- coding: utf-8 -*-
"""Project Euler: Problem 74

How many chains of sums of factorial digits, with a starting number
below one million, contain exactly sixty non-repeating terms?

https://projecteuler.net/problem=74
"""
from typing import List
from math import factorial as f


def chain(n: int, _cache={}) -> int:
    """Calculates the chain length of the sum of factorial digits.

    Args:
        n: number to compute the chain of
        _cache: internal memoization dictionary

    Returns:
        Length of the chain until the first repeat
    """
    # If number is already memoised, just return that
    if n in _cache:
        return _cache[n]
    else:
        chain = []
        link = n
        while link not in chain:
            chain.append(link)
            link = sum([f(int(d)) for d in str(link)])
            # If number's chain has already been previously calculated,
            # append it to the current one.
            if link in _cache:
                return _cache.setdefault(n, len(chain) + _cache[link])
        return _cache.setdefault(n, len(chain))


def main():
    chain_lengths = [chain(n) for n in range(10 ** 6)]
    print(sum([True for c in chain_lengths if c == 60]))


if __name__ == "__main__":
    main()
