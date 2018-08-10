# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:37:30 2018

@author: Jakub-P.Lech

Project Euler 22: Find the values of a list of names
"""

# Counts the value of a string where A = 1, B = 2, etc.
def countStringValue(string):
  return sum(ord(c) - ord("A") + 1 for c in string.upper())

def main():
  # Import text
  with open("022Input.txt") as inputFile:
    names = inputFile.read().replace("\"", "")
  # Sort list alphabetically
  names = sorted(names.split(","))
  # Multiply word value by its position in the list. Sum result
  print(sum(countStringValue(n)*(names.index(n) + 1) for n in names))

  
if __name__ == "__main__":
  main()
