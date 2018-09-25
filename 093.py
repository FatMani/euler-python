# -*- coding: utf-8 -*-
"""Project Euler: Problem 93

Find the set of four distinct digits, a < b < c < d, for which the
longest set of consecutive positive integers, 1 to n, can be obtained
by addition/subtraction/multiplication/division.

https://projecteuler.net/problem=93
"""
from operator import add, sub, mul, truediv
import itertools


def main():
    # Possible 4-digit combinations, 0 excluded
    combs = itertools.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
    results = []

    for c in combs:
        s = set()
        # Permute all the digit arrangements possible
        for p in itertools.permutations(c):
            # Pick three operations
            for o in itertools.product([add, mul, sub, truediv], repeat=3):
                # Only two arrangements of brackets need to be checked
                x = o[0](o[1](p[0], p[1]), o[2](p[2], p[3]))    # (a + b) + (c + d)
                y = o[0](o[1](o[2](p[0], p[1]), p[2]), p[3])    # ((a + b) + c) + d
                # Check if the two solutions are positive integers
                if int(x) == x and x > 0:
                    s.add(int(x))
                if int(y) == y and y > 0:
                    s.add(int(y))
        # Check consecutive length
        for n, i in enumerate(s):
            if (n + 1) != i:
                results.append((n, c))
                break
    # Print first entry when sorted by chain length
    print(sorted(results, reverse=True)[0])


if __name__ == "__main__":
    main()
