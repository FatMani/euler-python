# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:48:04 2018

@author: Jakub-P.Lech

Project Euler 32: Find the sum of all products where a*b=c and [a,b,c] are 
                  pandigital.
"""

from euler import isPandigitalNoZero

def main():
  # Generate list of all pandigital multiplicand/multiplier/product products
  numberList = [i*j for i in range(1, 9877) for j in range(1, 10000 // i) if (
      isPandigitalNoZero(int(str(i) + str(j) + str(i*j)), 9))]
  # Sum unique values
  print(sum(set(numberList)))
  
if __name__ == "__main__":
  main()