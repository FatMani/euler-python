# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:11:42 2018

@author: Jakub-P.Lech

Project Euler 28: Find the sum of numbers on diagonals of a 1001 by 1001 spiral
"""
def squareDiagonals(n):
  if n % 2 == 0: return 0
  elif n == 1: return 1
  else: 
    return 4*n**2 - 6*n + 6 + squareDiagonals(n - 2)


def main():
  print(squareDiagonals(1001))

if __name__ == "__main__":
  main()