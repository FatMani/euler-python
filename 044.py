# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:10:01 2018

@author: Jakub-P.Lech

Project Euler 44: Find the difference between two pentagonal numbers
                  whose sum and difference are also pentagonal.
"""
from math import sqrt

def is_pentagonal(n):
  if (1 + sqrt(1 + 24*n))/6 == int((1 + sqrt(1 + 24*n))/6): return True
  
def P(n): # returns the nth Pentagonal number
  return n*(3*n - 1)/2

def main():
  n = 1
  while True:
    n += 1
    a = P(n)
    for j in range(n - 1, 0, -1):
      b = P(j)
      if is_pentagonal(a - b) and is_pentagonal(a + b):
        print(a - b)
        break    
  
if __name__ == "__main__":
  main()