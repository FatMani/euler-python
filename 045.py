# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:20:40 2018

@author: Jakub-P.Lech

Project Euler 45: Find the second number that is triangular, pentagonal
                  and hexagonal
"""
from math import sqrt

def is_triangular(n):
  return (sqrt(1 + 8*n) - 1)/2 == int((sqrt(1 + 8*n) - 1)/2)

def is_pentagonal(n):
  return (1 + sqrt(1 + 24*n))/6 == int((1 + sqrt(1 + 24*n))/6)

def H(n): # Generate hexagonal number
  return n*(2*n - 1)

def main():
  n = 143
  while True:
    n += 1
    if is_triangular(H(n)) and is_pentagonal(H(n)):
      print(H(n))
      break

if __name__ == "__main__":
  main()