# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:47:42 2017

@author: Jakub-P.Lech

Project Euler 005: Find smallest positive number divisible by 1 to 20
"""

from math import gcd

# Least common multiple
def lcm(x, y):
  return (x * y) // gcd(x, y)

def main():
  result = 1
  
  for i in range(1, 20):
    result = lcm(result, i)  

  print(result)

if __name__ == "__main__":
  main()