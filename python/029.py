# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:16:50 2018

@author: Jakub-P.Lech

Project Euler 29: Find the number of distinct results of a^b, where 
                  2 <= a, b <= 100
"""
def main():
  print(len(set([i**j for i in range(2, 101) for j in range(2, 101)])))

if __name__ == "__main__":
  main()