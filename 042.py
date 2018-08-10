"""
Created on Thu Feb 15 22:00:34 2018

@author: Jakub-P.Lech

Project Euler 42: Find the count of triangle numbers in a list of words
"""
from euler import countStringValue
from math import sqrt

def main():
    with open("042Input.txt") as inputFile:
        words = inputFile.read().replace("\"", "").split(",")
    triangular = [(sqrt(1 + 8*countStringValue(n)) - 1)/2 for n in words]
    print(sum([1 for n in triangular if n == int(n)]))
    
if __name__ == "__main__":
    main()
