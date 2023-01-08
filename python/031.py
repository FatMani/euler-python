# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:33:07 2018

@author: Jakub-P.Lech

Project Euler 31: Find the number of ways £2 can be given in coins
"""

def main():
  arrangements = 0
  
  for i in range(200, -1, -200):
    for j in range(i, -1, -100):
      for k in range(j, -1, -50):
        for l in range(k, -1, -20):
          for m in range(l, -1, -10):
            for n in range(m, -1, -5):
              for o in range(n, -1, -2):
                arrangements += 1
  print(arrangements)

if __name__ == "__main__":
  main()