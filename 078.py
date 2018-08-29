# -*- coding: utf-8 -*-
"""Project Euler: Problem 78

Let p(n) represent the number of different ways in which n coins can be
separated into piles. Find the least value of n for which p(n) is
divisible by one million.

https://projecteuler.net/problem=78
"""


def g(k: int, _cache: dict = {}) -> int:
    """ Returns the kth generalised pentagonal number.

    Args:
        k: ordinal number of the pentagonal number
        _cache: internal memoization dictionary

    Returns:
        Kth pentagonal number if k >= 1
    """
    if k in _cache:
        return _cache[k]
    elif k > 0:
        n = (-1) ** (k + 1) * ((k + 1) // 2)
        return _cache.setdefault(k, (3 * n ** 2 - n) // 2)
    else:
        return 0


def main():
    # Generate 250 pentagonal numbers
    gk = [g(k) for k in range(1, 2500)]

    # Initialise list of partitions
    p = [1]
    # List of signs of terms in partition formula
    signs = [1, 1, -1, -1]
    # First number to check
    n = 0
    # Divisor to look for
    div = 10 ** 6

    # Since we're adding only the remainders, we will know we found the
    # number if p[n] % div == 0
    while p[n] > 0:
        # Look at next term
        n += 1
        px = 0
        i = 0
        while gk[i] <= n:
            # Sum as per partition formula
            px += p[n - gk[i]] * signs[i % 4]
            i += 1
        # Append the newly found number, modulo divisor
        p.append(px % div)
    print(n)


if __name__ == "__main__":
    main()
