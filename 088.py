# -*- coding: utf-8 -*-
"""Project Euler: Problem 88

A natural number, N, that can be written as the sum and product of a
given set of at least two natural numbers, {a1, a2, ... , ak} is called
a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak
        For example, 6 = 1 + 2 + 3 = 1 × 2 × 3
For a given set of size, k, we shall call the smallest N with this
property a minimal product-sum number.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

https://projecteuler.net/problem=88

Solution based on Dreamshire solution:
https://blog.dreamshire.com/project-euler-88-solution/
"""
from typing import Dict, List
from euler import primes_less_than


def factors(n: int, _cache: Dict[int, int]={}) -> List[List[int]]:
    """Returns all the factorisations of n.

    Args:
        n: number to check
        _cache: internal memoization dictionary

    Returns:
        List of all factor combinations that multiplied make n
    """
    # If already in cache, just return that
    if n in _cache:
        return _cache[n]
    else:
        fact = [[n]]
        # Iterate through all numbers up to sqrt(n) to find factors
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                # Recursively look at factors of remainder
                for subfactors in factors(n // i):
                    fact.append([i] + subfactors)
        _cache[n] = fact
        return fact


def main():
    k_max = 12000
    k_values = [0] * (k_max + 1)
    for n in range(2, 2 * k_max + 1):
        """For any given factorisation of n we can find the respective
        k value:
            k = n - sum(factors of n) + count(factors of n)
        Since we're going up, the first n-k pair we find is going to
        be the minimum, for a given k.
        """
        for f in factors(n):
            k = n - sum(f) + len(f)
            if 2 <= k <= k_max and k_values[k] == 0:
                k_values[k] = n
    # Take list of values and remove duplicates, then print sum
    print(sum(set(k_values)))


if __name__ == "__main__":
    main()
