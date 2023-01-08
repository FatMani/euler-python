# -*- coding: utf-8 -*-
"""Project Euler: Problem 100

Find the sum of first incorrect fits for the bad optimum polynomials
for approximations of a 10th degree polynomial

https://projecteuler.net/problem=101
"""
from typing import List
from numpy import polyfit, polyval


def generating_function(n: int) -> int:
    """Returns the nth term of the 10th degree polynomial

    Args:
        n: term of the polynomial, 0-indexed

    Returns:
        nth term of the polynomial
    """
    return sum([(-1)**i * n**i for i in range(11)])


def main():
    x_i = [n for n in range(1, 12)]
    y_i = [generating_function(n) for n in x_i]
    s = 0

    for i in range(1, 12):
        coeffs = polyfit(x_i[:i], y_i[:i], i - 1)
        vals = [int(round(n)) for n in polyval(coeffs, x_i)]

        for y, y_op in zip(y_i, vals):
            if y != y_op:
                s += y_op
                break
    print(s)


if __name__ == "__main__":
    main()
