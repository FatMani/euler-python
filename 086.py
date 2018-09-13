# -*- coding: utf-8 -*-
"""Project Euler: Problem 86

For a cuboid of dimensions up to M by M by M, find the least value of M
such that the number integer-length shortest paths from one corner to
another first exceeds one million.

https://projecteuler.net/problem=86
"""
from math import sqrt


def main():
    target, count, w = 2_000, 0, 2

    while count < target:
        w += 1
        for h_d in range(3, 2 * w):
            path = sqrt(h_d ** 2 + w ** 2)
            if path == int(path):
                if h_d <= w:
                    count += h_d // 2
                else:
                    count += 1 + w - (h_d + 1) // 2
    print(w)


if __name__ == "__main__":
    main()
