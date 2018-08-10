# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:07:32 2018

@author: Jakub-P.Lech

Project Euler 23: Find the sum of all numbers that can't be written as a sum of
                  two abundant numbers
"""
from euler import sumOfDivisors

def main():
  abundantNumbers = [i for i in range(1, 28124) if sumOfDivisors(i) > i]
  abundantSums = set([i+j for i in abundantNumbers for j in abundantNumbers])
  
  print(sum(set(range(1, 28124)) - abundantSums))

if __name__ == "__main__":
  main()