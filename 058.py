# -*- coding: utf-8 -*-
"""Project Euler: Problem 58

What is the side length of the square spiral for which the ratio of 
primes along both diagonals first falls below 10%?

https://projecteuler.net/problem=58
"""
import euler


def main():
    n = 1
    primes = 0
    total = 1
    while True:
        # Square number in the bottom right corner
        sq = (2 * n + 1) ** 2
        # Only consider other three corners
        numbers_to_check = [sq - 2 * n, sq - 4 * n, sq - 6 * n]
        primes += sum([euler.is_prime(i) for i in numbers_to_check])
        total += 4
        if primes / total < 0.1:
            print(2*n + 1)
            break
        n += 1


if __name__ == "__main__":
    main()
