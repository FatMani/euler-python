# -*- coding: utf-8 -*-
"""Project Euler: Problem 70

Find the value of n ≤ 10,000,000 for which n/φ(n) is a minimum and for
which φ(n) is a permutation of n, where φ(n) is the Euler totient
function.

https://projecteuler.net/problem=70
"""
import euler


def main():
    """ The totient function can be defined as a product:

        φ(n) = n*(1 - 1/p1)*(1 - 1/p2)*(1 - 1/p3)*...

    Where p1, p2, etc. are the prime factors of n. Therefore, the ratio
    n/φ(n) simplifies to :

        n/φ(n) = 1/[(1 - 1/p1)*(1 - 1/p2)*(1 - 1/p3)*...]

    This is minimum where the denominator is maximum, and the
    denominator is maximum if there are as few, and as large as
    possible prime factors.

    Let us then assume that the number n will have the form:

        n = p1*p2

    For some two large prime numbers. We can investigate prime numbers
    around sqrt(10,000,000) +/- 30%, i.e. from 2000 to 5000. Potential
    n's can be found, their totients computed and ratios found.

    For simplicity, since:
        φ(n) = n*(1 - 1/p1)*(1 - 1/p2)
    and
        n = p1*p2

    We can simplify to:
        φ(n) = (p1 - 1)*(p2 - 2)
    """
    primes = [p for p in euler.primes_less_than(4000) if p >= 2000]
    # Find all combinations under 10,000,000
    candidates = [(p1 * p2, (p1 - 1) * (p2 - 1)) for p1 in primes for p2 in primes if (p1 != p2 and p1 * p2 < 10 ** 7)]
    # Find all combinations that are permutations
    candidates = [c for c in candidates if euler.is_permutation(c[0], c[1])]
    ratios = [c[0] / c[1] for c in candidates]
    print(candidates[ratios.index(min(ratios))])


if __name__ == "__main__":
    main()
