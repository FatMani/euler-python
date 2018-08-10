# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:09:26 2018

@author: Jakub-P.Lech

Project Euler 36: Find the sum of all numbers below 10^6 that are palindomic
                  in binary and decimal base
"""
def isBinaryAndDecimalPalindromic(n):
  if (n == int(str(n)[::-1]) and 
      n == int((bin(n)[2:])[::-1], 2)): return True 
  else: return False

def main():
  print(sum([i for i in range(1, 10**6, 2) if isBinaryAndDecimalPalindromic(i)]))
  
if __name__ == "__main__":
  main()