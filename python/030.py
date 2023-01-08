# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:41:50 2018

@author: Jakub-P.Lech

Project Euler 30: Find the sum of numbers that can be written as the sum of
                  their digits to the fifth power
"""
def main():
  print(sum([i for i in range(2, 355000) if i == sum([int(j)**5 for j in str(i)])]))

if __name__ == "__main__":
  main()