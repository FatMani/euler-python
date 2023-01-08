# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:59:35 2017

@author: Jakub-P.Lech

Project Euler 009: Find a Pythagorean Triplet such that a+b+c = 1000
"""


def main():
    for a in range(1, 998):
        for b in range(a, 998):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(a * b * c)


if __name__ == "__main__":
    main()

