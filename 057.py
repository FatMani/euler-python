# -*- coding: utf-8 -*-
"""Project Euler: Problem 57

In the first one-thousand expansions of the infinite continued
fraction of sqrt(2), how many fractions contain a numerator with more
digits than denominator?

https://projecteuler.net/problem=57
"""
from typing import Tuple


def root_2_expansion(n: int, _cache={}) -> Tuple[int, int]:
    """Finds the n-th expansion of sqrt(2).

    Args:
        n: index of the expansion to be found
        _cache: internal memoization dictionary

    Returns:
        n-th root 2 expansion as (numerator, denominator).
    """
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(
            n,
            (
                root_2_expansion(n - 1)[0] + 2 * root_2_expansion(n - 1)[1],
                root_2_expansion(n - 1)[0] + root_2_expansion(n - 1)[1],
            ),
        )
    elif n == 1:
        return _cache.setdefault(n, (3, 2))
    else:
        return (1, 1)


def main():
    expansions = [root_2_expansion(n) for n in range(1001)]
    longer_numerators = [len(str(a[0])) > len(str(a[1])) for a in expansions]
    print(sum(longer_numerators))


if __name__ == "__main__":
    main()
