# -*- coding: utf-8 -*-
"""Project Euler: Problem 76

How many different ways can one hundred be written as a sum of at least
two positive integers?

https://projecteuler.net/problem=76
"""


def main():
    n = 5
    arrangements = [1] + [0] * n
    for i in range(1, n):
        for j in range(i, n + 1):
            arrangements[j] += arrangements[j - i]
    print(arrangements[-1])

if __name__ == "__main__":
    main()
