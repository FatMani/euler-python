# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:50:31 2018

@author: Jakub-P.Lech

Project Euler 33: Find the denominator of "simplifying" fractions
"""
from math import gcd

def main():
  numerator = 1
  denominator = 1
  
  for i in range(1, 10):
    for d in range(1, i):
      for n in range(1, d):
        if (10*n + i)*d == n*(10*i + d):
          numerator *= n
          denominator *= d
  
  print(denominator // gcd(numerator, denominator))
  
if __name__ == "__main__":
  main()