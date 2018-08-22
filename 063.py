# -*- coding: utf-8 -*-
"""Project Euler: Problem 63

How many n-digit positive integers exist which are also an nth power?

https://projecteuler.net/problem=63
"""

from math import log10

"""Firstly, we know that n < 10, as 10^n always has n+1 digits.

Secondly, we know that x^n < 10^(n-1). By rearranging, we can find that
log(x^n)    <   log(10^(n - 1))
nlogx       <   n - 1
nlogx - n   <   -1
n           <   -1/(logx - 1)
"""


def main():
    print(sum([int(1 / (1 - log10(n))) for n in range(1, 10)]))


if __name__ == "__main__":
    main()
