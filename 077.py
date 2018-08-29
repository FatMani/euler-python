# -*- coding: utf-8 -*-
"""Project Euler: Problem 77

What is the first value which can be written as the sum of primes in
over five thousand different ways?

https://projecteuler.net/problem=77
"""
import euler


def main():
    primes = euler.primes_less_than(1000)
    n = 11

    while True:
        arrangements = [1] + [0] * n
        for p in primes:
            for i in range(p, n + 1):
                arrangements[i] += arrangements[i - p]

        if arrangements[n] > 5000:
            print(n)
            break
        n += 1


if __name__ == "__main__":
    main()
