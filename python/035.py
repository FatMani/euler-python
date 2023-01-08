# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:26:10 2018

@author: Jakub-P.Lech

Project Euler 35: Find the number of circular primes under 10^6
"""

from euler import isPrime

def circularPrimeCheck(n):
  digitsList = [int(i) for i in str(n)]     # Convert number to digits
  if isPrime(n):                            # Original number has to be prime
    for i in range(1, len(str(n))):
      digitsList.append(digitsList.pop(0))  # Rotate number by 1 place
      n = int("".join(map(str, digitsList)))# New number to check
      if not isPrime(n): return False       # If new number is nonprime, break
    return True                             # If all are prime, found circular
  return False
  
def main():
  print(sum([1 for i in range(1, 1000000) if circularPrimeCheck(i)]))

  
if __name__ == "__main__":
  main()