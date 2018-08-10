# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:16:41 2018

@author: Jakub-P.Lech

Euler Project 15: Paths on a 20x20 grid
"""
import math

def nCr(n, k):
  return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))

def main():
  # To move left and down through a 20x20 grid, the path must have 20 
  # horizontal segments and 20 vertical segments, for a total of 40 moves.
  # This can be calculated as calculation the number of combinations of 20 
  # elements out of a set of 40:
    print(nCr(40, 20))

if __name__ == "__main__":
  main()