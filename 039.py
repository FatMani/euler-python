# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 21:02:36 2018

@author: Jakub-P.Lech

Project Euler 39: Find the value for p <= 1000 for which a+b+c = p
                  and a^2 + b^2 = c^2
"""
from math import sqrt

def main():
    triples = []
    count = 0
    for p in range(1, 1001):
        count = 0
        for a in range(1, p):
            b = (p**2 - 2*p*a)/(2*p - 2*a)
            c = sqrt(a**2 + b**2)

            if b > 0 and c > 0 and int(b) == b and int(c) == c:
                count += 1
        triples.append(count)
    print(triples.index(max(triples)) + 1)
if __name__ == "__main__":
    main()
