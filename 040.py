# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 21:36:39 2018

@author: Jakub-P.Lech

Project Euler 40: Find d1*d10*d100*d1000*d10000*d100000*d1000000, where dn is
                  the nth digit of the fraction created by concatenating
                  positive integers (0.1234567891011121314...)
"""

def main():
    n = str(1)
    for i in range(2, 1000001):
        n = n + str(i)

    print(int(n[1 - 1])*int(n[10 - 1])*int(n[100 - 1])*int(n[1000 - 1])
          *int(n[10000 - 1])*int(n[100000 - 1])*int(n[1000000 - 1]))

if __name__ == "__main__":
    main()
