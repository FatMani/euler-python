# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:04:02 2018

@author: Jakub-P.Lech

Project Euler 38: Find the largest 9-digit pandigital number formed by
                  multipling a number by 1, 2, 3, etc. and concatenating result
"""

from euler import isPandigitalNoZero

def main():
  print(max([int(str(i) + str(2*i)) for i in range(9123, 9877) if 
                    isPandigitalNoZero(int(str(i) + str(2*i)), 9)]))

if __name__ == "__main__":
  main()