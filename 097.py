# -*- coding: utf-8 -*-
"""Project Euler: Problem 97

Find the last 10 digits of 28433 * 2^7830457 + 1

https://projecteuler.net/problem=97
"""
def main():
    last_10_digits = 2
    for exponent in range(1, 7830457):
       last_10_digits *= 2
       last_10_digits %= 10**10
    last_10_digits *= 28433
    last_10_digits += 1
    last_10_digits %= 10**10
    print(last_10_digits)

if __name__ == '__main__':
    main()