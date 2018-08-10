# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:39:48 2018

@author: Jakub-P.Lech

Project Euler 48: Find the last ten digits of 1^1 + 2^2 + ... + 1000^1000
"""

def main():
  print(sum([i**i for i in range(1, 1001)]) % 10**10)
  
if __name__ == "__main__":
  main()