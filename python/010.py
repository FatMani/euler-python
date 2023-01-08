# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:08:15 2017

@author: Jakub-P.Lech

Project Euler 10: Find the sum of all primes below 2 million
"""

from euler import primesLessThan

def main():
  primes = list(primesLessThan(2000000))
  print(sum(x for x in primes))
  
if __name__ == "__main__":
  main()
