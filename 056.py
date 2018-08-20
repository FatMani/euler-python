# -*- coding: utf-8 -*-
"""Project Euler: Problem 56

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

https://projecteuler.net/problem=56
"""


def main():
    sums = []
    for a in range(101):
        for b in range(101):
            sums.append(sum([int(d) for d in str(a ** b)]))
    print(max(sums))


if __name__ == "__main__":
    main()
