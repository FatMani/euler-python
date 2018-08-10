# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:30:06 2018

@author: Jakub-P.Lech

Project Euler 37: Find the only 11 truncatable primes from both directions
"""
from euler import is_prime

def isBidirectionalTruncatablePrime(n):
  if n <= 7: return False
  if is_prime(n):
    for i in range(len(str(n)) - 1, 0, -1):
      # Both left-trimmed and right-trimmed have to be prime
      if not is_prime(n % (10**i)) or not is_prime(n // (10**i)): return False
    return True # if all checks are passed, number is truncatable prime
  return False

def main():
  n = 8
  listOfPrimes = []
  while len(listOfPrimes) < 11:
    if isBidirectionalTruncatablePrime(n): listOfPrimes.append(n)
    n += 1
  print(sum(listOfPrimes))

if __name__ == "__main__":
  main()
