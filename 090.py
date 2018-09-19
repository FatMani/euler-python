# -*- coding: utf-8 -*-
"""Project Euler: Problem 90

How many distinct arrangements of two cubes allow for all of the square
numbers to be displayed?

https://projecteuler.net/problem=90
"""
import itertools
from typing import List, Tuple


def main():
    # All squares that need to be generated. (0, 6) and (4, 6)
    # represent 9 and 49, as 6 can be flipped. 64 is missing as it is
    # equivalent to 46 (i.e. 49).
    squares = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (8, 1)]
    # Generate all possible dice arrangements
    dice = list(itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 6], 6))
    count = 0

    for i, d1 in enumerate(dice):
        # Only look at previous dice to ignore duplicates
        for d2 in dice[:i]:
            # See if square can be made with the two dice in either arrangement
            if all((x in d1 and y in d2) or (x in d2 and y in d1) for (x, y) in squares):
                count += 1
    print(count)


if __name__ == "__main__":
    main()
