# -*- coding: utf-8 -*-
"""Project Euler: Problem 65

Find the sum of digits in the numerator of the 100th convergent
of the continued fraction for e.

https://projecteuler.net/problem=64
"""
from math import ceil


def main():
    numerators = [1, 2]
    for i in range(2, 101):
        if i % 3 == 0:
            f = ceil(i / 3) * 2
        else:
            f = 1
        numerators.append(f * numerators[i - 1] + numerators[i - 2])
    print(sum([int(c) for c in str(numerators[100])]))


if __name__ == "__main__":
    main()
