# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:17:44 2018

@author: Jakub-P.Lech

Project Euler 17: Number of letters in the names of numbers from 1 to 1000
"""
# Works up to 999
def calculateNumberNameLength(n):
  length = 0
  ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
  teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
  tens = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6] 

  # Hundreds + "hundred"
  if n // 100 != 0:
    length = length + ones[n // 100] + 7  
    # See if it has any tens or ones, if yes add "and"
    if (n % 100) != 0:
      length = length + 3
  
  # Tens
  # Special case: teens
  if (n // 10) % 10 == 1:
    length = length + teens[n % 10]
  else:
    length = length + tens[(n // 10) % 10] + ones[n % 10]
  
  return length  


def main():
   s = sum(calculateNumberNameLength(x) for x in range(1, 1000))
   print(s + len("onethousand"))   
  
if __name__ == "__main__":
  main()
