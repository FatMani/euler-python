# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:41:48 2018

@author: Jakub-P.Lech

Project Euler 20: Find the sum of amicable numbers under 10000. N is an 
                  amicable number if the sum of divisors, of the sum of
                  divisors of N is equal to N.
"""
from euler import sumOfDivisors

def main():
  print(sum(i for i in range(1, 10001) if 
            (i == sumOfDivisors(sumOfDivisors(i)) and i != sumOfDivisors(i))))

if __name__ == "__main__":
  main()