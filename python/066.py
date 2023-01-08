# -*- coding: utf-8 -*-
"""Project Euler: Problem 66

Consider quadratic Diophantine equations of the form:
    x^2 – D*y^2 = 1
Find the value of D ≤ 1000 in minimal solutions of x for which the
largest value of x is obtained.

https://projecteuler.net/problem=66
"""
from math import sqrt
from typing import List, Tuple


def min_sol(D: int) -> Tuple[int, int]:
    """Finds the minimal solution for the diophantine equation.

    Args:
        D: factor by which y^2 is multiplied

    Returns:
        Tuple of the form (D, minimum integer x for which a solution exists)
    """
    # Check for perfect squares
    if int(sqrt(D)) == sqrt(D):
        return (D, 0)

    # Continuous fraction expansion
    a = cont_frac(D)
    coef = [(a[0], 1), (a[1] * a[0] + 1, a[1])]
    # Check first coefficients
    for p in coef:
        if p[0] ** 2 - D * p[1] ** 2 == 1:
            return (D, p[0])

    rep_a = a[1:]
    i = 1
    while True:
        i = i % len(rep_a)
        n, d = rep_a[i] * coef[-1][0] + coef[-2][0], rep_a[i] * coef[-1][1] + coef[-2][1]
        if n ** 2 - D * d ** 2 == 1:
            return (D, n)
        coef.append((n, d))
        i += 1


def cont_frac(S: int) -> List[int]:
    """Finds the continued fraction expansion of sqrt(S)

    Based on the algorithm at:
    https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

    Args:
        S: square of the number of interest

    Returns:
        List of integers in continued fraction
    """
    # Catch perfect squares
    if int(S ** 0.5) == S ** 0.5:
        return []

    coeffs = [(0, 1, int(sqrt(S)))]
    expansion = [int(sqrt(S))]
    while True:
        m, d, a = coeffs[-1][0], coeffs[-1][1], coeffs[-1][2]
        m = d * a - m
        d = (S - m ** 2) // d
        a = int((sqrt(S) + m) / d)
        if (m, d, a) in coeffs:
            return expansion
        coeffs.append((m, d, a))
        expansion.append(a)


def main():
    solutions = [min_sol(D) for D in range(100001)]
    x_vals = [s[1] for s in solutions]
    print(solutions[x_vals.index(max(x_vals))])


if __name__ == "__main__":
    main()
