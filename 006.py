# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:50:25 2017

@author: Jakub-P.Lech

Find the difference between the square of the sum and the sum of the squares of
the first 100 natural numbers.
"""

def main():
  a = sum(x for x in range(1, 101))**2
  b = sum(x**2 for x in range(1, 101))
  print(a-b)

if __name__ == "__main__":
  main()