# -*- coding: utf-8 -*-
"""Project Euler: Problem 72

How many reduced proper fractions for d ≤ 1,000,000 are there?

https://projecteuler.net/problem=72
"""


def main():
    # Start with assumption that totient[n] = n
    phi = [i for i in range(10 ** 6 + 1)]
    # Iterate through all denominators
    for d in range(2, 10 ** 6 + 1):
        # If d is prime
        if phi[d] == d:
            # Iterate through all numbers, of which d is a factor
            for i in range(d, 10 ** 6 + 1, d):
                # Multiply by (1 - 1/d) as per the totient calculation
                # Therefore all numbers that are made up by a prime
                # Will have it included in its totient calculation
                phi[i] = int(phi[i] * (1 - 1 / d))
    # Subtract 1 for n = 1
    print(sum(phi) - 1)


if __name__ == "__main__":
    main()
