# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:33:37 2018

@author: Jakub-P.Lech

Project Euler 20: Find the sum of the digits in 100!
"""
import math

#def sumDigits(n):
#  s = 0
#  while n > 0:
#    s += n % 10
#    n //= 10
#  return s

def main():
#  Alternate version using a pre-defined function
#  print(sumDigits(math.factorial(100)))

  # Slower, but works in one line
  print(sum(int(d) for d in str(math.factorial(100))))

if __name__ == "__main__":
  main()