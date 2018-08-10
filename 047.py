# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:24:40 2018

@author: Jakub-P.Lech

Project Euler 47: Find the first 4 consecutive integers that have four distinct
                  prime factors each
"""

from euler import primes_less_than
from math import sqrt

def prime_factors(n):
  primes = primes_less_than(int(sqrt(n)) + 1)
  factors = []
  for p in primes:
    while n % p == 0 and n > 1:
      n //= p
      factors.append(p)
  if n != 1: factors.append(n)
  return factors
      
def main():
  i = 644
  while True:
    if (len(set(prime_factors(i))) == 4 and 
        len(set(prime_factors(i + 1))) == 4 and 
        len(set(prime_factors(i + 2))) == 4 and 
        len(set(prime_factors(i + 3))) == 4):
      print(i)
      break
    i += 1
  
if __name__ == "__main__":
  main()