# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 09:14:29 2018

@author: Jakub-P.Lech

Project Euler 43: Find sum of all pandigital sub-string divisible numbers
"""
from itertools import permutations

def main():
  digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  numbers = [int("".join(map(str, x))) for x in permutations(digits) if 
             x[0] > 0 and                               # first digit not 0
             x[3] % 2 == 0 and
             (x[2] + x[3] + x[4]) % 3 == 0 and
             x[5] % 5 == 0 and
             (100*x[4] + 10*x[5] + x[6]) % 7 == 0 and
             (100*x[5] + 10*x[6] + x[7]) % 11 == 0 and
             (100*x[6] + 10*x[7] + x[8]) % 13 == 0 and
             (100*x[7] + 10*x[8] + x[9]) % 17 == 0]
  print(sum(numbers))
if __name__ == "__main__":
  main()