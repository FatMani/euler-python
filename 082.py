# -*- coding: utf-8 -*-
"""Project Euler: Problem 82

Find the minimal path sum, in an 80 by 80 matrix, from the left column
to the right column by only moving right, up or down.

https://projecteuler.net/problem=82
"""
from typing import List


def import_text() -> List[List[int]]:
    """Reads file to list.

    Retuns:
        2-dimensional list of elements
    """
    M = open("082Input.txt").read()
    M = M.splitlines()
    M = [i.split(",") for i in M]
    M = [[int(j) for j in i] for i in M]
    return M


def main():
    M = import_text()
    # Solution value to last column
    column_solution = [M[i][len(M) - 1] for i in range(len(M))]
    # Iterate through all columns from penultimate to first
    for j in range(len(M) - 2, -1, -1):
        # Initialise the value to first term of matrix column
        column_solution[0] += M[0][j]
        for k in range(1, len(M)):
            # Is it better to go up-right or just right
            column_solution[k] = min(column_solution[k - 1] + M[k][j], column_solution[k] + M[k][j])
        for k in range(len(M) - 2, -1, -1):
            # Is it better to go down or previously found solution?
            column_solution[k] = min(column_solution[k], column_solution[k + 1] + M[k][j])
    print(min(column_solution))


if __name__ == "__main__":
    main()
