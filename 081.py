# -*- coding: utf-8 -*-
"""Project Euler: Problem 81

Find the minimal path sum, in an 80 by 80 matrix, from the top left to
the bottom right by only moving right and down.

https://projecteuler.net/problem=81
"""
from typing import List


def import_text() -> List[List[int]]:
    """Reads file to list.

    Retuns:
        2-dimensional list of elements
    """
    M = open("081Input.txt").read()
    M = M.splitlines()
    M = [i.split(",") for i in M]
    M = [[int(j) for j in i] for i in M]
    return M


def main():
    M = import_text()

    for i in range(79, -1, -1):
        for j in range(79, -1, -1):
            if i < 79 and j < 79:
                # All rows and columns except the last
                M[i][j] += min(M[i + 1][j], M[i][j + 1])
            elif i < 79:
                # Final column
                M[i][j] += M[i + 1][j]
            elif j < 79:
                # Final row
                M[i][j] += M[i][j + 1]
    print(M[0][0])


if __name__ == "__main__":
    main()
