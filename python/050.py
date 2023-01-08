# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:22:55 2018

@author: Jakub-P.Lech

Project Euler 50: Find the longest sum of consecutive primes that adds up
                  to a prime below 1,000,000
"""
from euler import primes_less_than

def main():
  primes = primes_less_than(10**6)
  consecutive_sum = [2]
  for i in range(1, len(primes)):
    consecutive_sum.append(primes[i] + consecutive_sum[i - 1])

  chain_length = 0
  max_prime = 0
  for i in range(chain_length, len(consecutive_sum)):
    for j in range(i - chain_length + 1, -1, -1):
      if consecutive_sum[i] - consecutive_sum[j] > 10**6:
        break
      if consecutive_sum[i] - consecutive_sum[j] in primes and \
      i - j > chain_length:
        chain_length = i - j
        max_prime = consecutive_sum[i] - consecutive_sum[j]
  print(max_prime)
        
  
if __name__ == "__main__":
  main()