# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:04:37 2018

@author: Jakub-P.Lech

Project Euler 34: Find the sum of all numbers which are equal to the sum of the
                  factorials of their digits
"""
from math import factorial

def main():
  print(sum([i for i in range(3, 2540200) if (i == sum([factorial(int(j)) for
                                              j in str(i)]))]))
  
if __name__ == "__main__":
  main()