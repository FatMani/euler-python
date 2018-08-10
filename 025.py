# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:44:03 2018

@author: Jakub-P.Lech

Project Euler 25: Find the index of the first 1000-digit Fibonacci number
"""
from euler import fibonacci

def main():
  i = 1
  while len(str(fibonacci(i))) < 1000:
    i += 1
  print(i)

if __name__ == "__main__":
  main()