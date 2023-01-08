# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:11:18 2018

@author: Jakub-P.Lech

Project Euler 12: Find first triangular number to have 500 divisors
"""
from euler import numberOfDivisors

def main():
  number = 0
  ticker = 1
  
  while(numberOfDivisors(number) < 500):
    number = number + ticker
    ticker = ticker + 1
  
  print(number)  
  
if __name__ == "__main__":
  main()