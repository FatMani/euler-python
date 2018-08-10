# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:00:22 2018

@author: Jakub-P.Lech

Project Euler 27: Find the product of a and b where n^2 + an + b produces the 
                  largest number of consecutive primes for n >= 0 and 
                  |a| < 1000, |b| <= 1000
"""
from euler import isPrime

def main():
  maxPrimesCount = 0
  product = 0
  for a in range(-999, 1000):
    for b in range(-1000, 1001):
      n = 0
      while isPrime(n**2 + a*n + b):
        n += 1
      if n > maxPrimesCount:
        maxPrimesCount = n
        product = a*b
  print(product)


if __name__ == "__main__":
  main()