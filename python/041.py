# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 21:47:02 2018

@author: Jakub-P.Lech

Project Euler 41: Find the largest pandigital prime
"""
from euler import primesLessThan, isPandigitalNoZero

def main():
    print(max([n for n in primesLessThan(7654322) if isPandigitalNoZero(n, len(str(n)))]))

if __name__ == "__main__":
    main()
