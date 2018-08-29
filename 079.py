# -*- coding: utf-8 -*-
"""Project Euler: Problem 79

Given that the three characters are always asked for in order, analyse
the file so as to determine the shortest possible secret passcode of
unknown length.

https://projecteuler.net/problem=79
"""


def main():
    file = open("079Input.txt").read().splitlines()
    appearance = [[0] * 10 for _ in range(10)]
    for row in file:
        a, b, c = int(row[0]), int(row[1]), int(row[2])
        appearance[a][b], appearance[a][c], appearance[b][c] = 1, 1, 1
    # See before how many other digits the digit appears
    appear_before = [sum(row) for row in appearance]
    # See after how many other digits the digit appears
    appear_after = [sum(column) for column in [*zip(*appearance)]]  # Transposed array
    # Remove values which appear before and after no digits (i.e. they're not in a password)
    tuples = [(appear_after[i], i) for i in range(10) if (appear_after[i] != 0 or appear_before[i] != 0)]
    print("".join([str(t[1]) for t in sorted(tuples)]))


if __name__ == "__main__":
    main()
