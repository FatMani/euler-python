# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:43:56 2018

@author: Jakub-P.Lech

Project Euler 46: Find the smallest odd composite that cannot be written
                  as a sum of a prime and twice a square
"""
from euler import primes_less_than
from math import sqrt

def is_Collatz(n, i):
  return int(sqrt((n - i)/2)) == sqrt((n - i)/2)

def main():
  numbers = primes_less_than(1000000)
  n = 9 # First composite number
  not_found = True
  while not_found:
    n += 2 # Next odd number
    not_found = False
    
    for i in numbers:
      if i <= n and is_Collatz(n, i):
        not_found = True
        break
  print(n)
  
if __name__ == "__main__":
  main()