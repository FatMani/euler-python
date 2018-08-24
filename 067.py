# -*- coding: utf-8 -*-
"""Project Euler: Problem 67

Find the maximum total from top to bottom in triangle.txt, a 15K text
file containing a triangle with one-hundred rows.

https://projecteuler.net/problem=67
"""
from typing import List


def import_text() -> List[List[int]]:
    """Reads file to list.

    Retuns:
        2-dimensional list of elements
    """
    M = open("067Input.txt").read()
    M = M.splitlines()
    M = [i.split() for i in M]
    M = [[int(j) for j in i] for i in M]
    return M


def main():
    M = import_text()

    for i in range(len(M) - 2, -1, -1):
        for j in range(len(M[i])):
            M[i][j] += max(M[i + 1][j], M[i + 1][j + 1]) 
    print(M[0][0])


if __name__ == "__main__":
    main()
