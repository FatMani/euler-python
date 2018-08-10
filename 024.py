# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:37:25 2018

@author: Jakub-P.Lech
"""

import itertools

def main():
  permutations = list(itertools.permutations(range(0, 10)))
  print("".join(str(c) for c in sorted(permutations)[1000000 - 1]))
  
  
if __name__ == "__main__":
  main()