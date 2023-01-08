# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:38:58 2017

@author: Jakub-P.Lech

Project Euler 004: Find the largest palindrome made from the product of two 
3-digit numbers
"""


def isPalindromic(number):
  return str(number) == str(number)[::-1]

def main():
  largestPalindrome = 0
  
  for i in range(999, 100, -1):
    for j in range(999, 100, -1):
      if isPalindromic(i*j) and (i*j) > largestPalindrome:
        largestPalindrome = i*j
        break
    
  print(largestPalindrome)
  
if __name__ == "__main__":
  main()