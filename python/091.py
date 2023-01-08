# -*- coding: utf-8 -*-
"""Project Euler: Problem 91

The points P (x1, y1) and Q (x2, y2) are plotted at integer
co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ. There
are exactly fourteen triangles containing a right angle that can be
formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2. Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many
right triangles can be formed?

https://projecteuler.net/problem=91
"""
import itertools
from typing import List, Tuple


def is_right_angle(x1: int, y1: int, x2: int, y2: int) -> bool:
    """Checks whether the triangle ([x1, y1], [x2, y2], [0, 0]) is right-angled

    Calculates the squares of the three sides, and checks if the two
    shortest ones sum to the longest one.

    Args:
        x1, y1: Cartesian coordinates of first point
        x2, y2: Cartesian coordinates of second point

    Returns:
        True if triangle is right-angled, False otherwise
    """
    d = sorted([x1 ** 2 + y1 ** 2, x2 ** 2 + y2 ** 2, (x1 - x2) ** 2 + (y1 - y2) ** 2])
    return d[0] + d[1] == d[2]


def main():
    # All points on grid, except (0, 0)
    points = [(x, y) for x in range(51) for y in range(51) if not (x == 0 and y == 0)]
    # All combinations of two corners
    pair = list(itertools.combinations(points, 2))
    right_angled = [True for (P, Q) in pair if is_right_angle(*P, *Q)]
    print(sum(right_angled))

if __name__ == "__main__":
    main()
