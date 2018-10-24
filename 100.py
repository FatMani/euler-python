# -*- coding: utf-8 -*-
"""Project Euler: Problem 100

Find the first arrangement of red and blue discs, such that the
probability of taking two blue discs in a row is exactly 1/2 and that
the total number of discs is over 1,000,000,000,000

https://projecteuler.net/problem=100

Analysis:
    We know that the probability of taking two blue discs from a box
    containing "b" blue discs and "t" total discs is:
        b/t * (b - 1)/(t - 1)   = 1/2
        b(b - 1)/t(t - 1)       = 1/2
        b(b - 1)                = t(t - 1)/2
        2b^2 - 2b - t^2 + t = 0
    This can be solved by using a diophantine equation:
        b_n+1 = 3b_n + 2t_n - 2
        t_n+1 = 4b_n + 3t_n - 3
    
"""
from math import sqrt


def main():
    target = 1_000_000_000_000
    b, t = 15, 21
    while t < target:
        b, t = 3 * b + 2 * t - 2, 4 * b + 3 * t - 3
    print(b)


if __name__ == "__main__":
    main()
