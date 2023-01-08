# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:44:15 2018

@author: Jakub-P.Lech

Project Euler 49: Find the numbers which are separated by an equal distance
                  are all prime and permutations of each other
"""

from euler import primes_less_than

# Checks if two numbers contain the same digits
def check_permutation(n, m):
  # Uses bitwise shift 
  return (sum([1 << int(i) for i in str(n)]) == 
          sum([1 << int(j) for j in str(m)]))

def main():
  primes = [i for i in primes_less_than(10000) if i > 1000]  
  triples = [(a, b, 2*b - a) for a in primes for b in primes if 
             a < b and b < 2*b - a and        # a < b < c
             2*b - a in primes and            # c is prime
             check_permutation(a, b) and      # a and b are permutations
             check_permutation(a, 2*b - a)]   # a and c are permutations
  
  for a, b, c in triples: print(str(a) + str(b) + str(c))
if __name__ == "__main__":
  main()