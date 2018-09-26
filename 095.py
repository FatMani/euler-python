# -*- coding: utf-8 -*-
"""Project Euler: Problem 95

Find the smallest member of the longest amicable chain with no element
exceeding one million.

https://projecteuler.net/problem=95
"""
from typing import List, Dict


def sum_of_divisors(limit: int) -> List[int]:
    """Returns the sum of proper divisors of integers up to limit

    Args:
        limit: maximum number to investigate
    
    Returns:
        List of all sums of divisors, excluding number itself
    """
    if limit < 0:
        return []
    elif limit == 0:
        return [0]
    else:
        sums = [1] * limit
        for n in range(2, limit // 2):
            for i in range(2 * n, limit, n):
                sums[i] += n
        return sums


def main():
    limit, maximum_chain_length = 1_000_000, 0
    sums = sum_of_divisors(limit)    
    for i in range(2, limit):
        n, chain = i, []
        while sums[n] < limit:
            sums[n], n = limit + 1, sums[n]
            if n not in chain:
                chain.append(n)
            else:
                k = chain.index(n)
                if len(chain[k:]) > maximum_chain_length:
                    maximum_chain_length = len(chain[k:])
                    minimum_link = min(chain[k:])
    print(minimum_link)


if __name__ == "__main__":
    main()

