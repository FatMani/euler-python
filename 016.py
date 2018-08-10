# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:00:41 2018

@author: Jakub-P.Lech

Project Euler 16: Find the sum of digits of 2^1000
"""

def main():
  n = 2**1000
  print(sum(int(d) for d in str(n)))
  
if __name__ == "__main__":
  main()