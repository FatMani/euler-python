# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:58:32 2018

@author: Jakub-P.Lech

Euler Project 14: Find longest Collatz sequence with starting number under 1m
"""
# Brute force approach:
#def collatzLength(n):
#  # Collatz sequence is defined for positive integers only
#  if n <= 0 or int(n) != n:
#    return 0
#  
#  # Iterate through Collatz sequence
#  length = 1
#  while n != 1:
#    if n % 2 == 0:
#      n = n / 2
#      length = length + 1
#    else:
#      n = 3*n + 1
#      length = length + 1
#  return length
#
#def main():
#  # Number, length
#  collatz = [0, 0]
#  
#  for i in range(1, 1000001):
#    l = collatzLength(i)
#    if l > collatz[1]:
#      collatz = [i, l]
#      
#  print(collatz[0])

# Caching approach, much quicker
def main():
  collatz = [1]
  
  for i in range(2, 1000001):
    tempNumber = i
    length = 0
    
    # Calculate Collatz sequence until a number smaller than i is reached
    while tempNumber >= i:
      length = length + 1
      if tempNumber % 2 == 0:
        tempNumber = tempNumber / 2
      else:
        tempNumber = 3*tempNumber + 1
    
    # Find that smaller number's length and add to current length    
    length = length + collatz[int(tempNumber) - 1]
    # Then store
    collatz.append(length)
  
  # Find index of maximum in list, add +1 as list is zero-indexed
  print(collatz.index(max(collatz)) + 1)

if __name__ == "__main__":
  main()