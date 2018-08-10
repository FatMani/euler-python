# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:11:01 2018

@author: Jakub-P.Lech

Project Euler 26: Find the longest decimal period for a number 1/d for d < 1000
"""
def decimalPeriod(d):
  expansion = []
  remainder = 1 % d
  while remainder != 0 and remainder not in expansion:
    expansion.append(remainder)
    remainder = (remainder * 10) % d
  return len(expansion)

def main():
  periodsList = [decimalPeriod(d) for d in range(1, 1001)]
  print(periodsList.index(max(periodsList)) + 1)
  
if __name__ == "__main__":
  main()