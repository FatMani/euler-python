# -*- coding: utf-8 -*-
"""Project Euler: Problem 102

Find the number of triangles that contain the origin

https://projecteuler.net/problem=102
"""
from typing import List
from math import log


def import_text() -> List[str]:
    """Reads file to list of coordinates.

    Returns:
        List of coordinates
    """
    text = open("102Input.txt").read()
    text = text.splitlines()
    numbers = [entry.split(",") for entry in text]
    numbers = [[int(n) for n in entry] for entry in numbers]
    return numbers


def contains_origin(t: List[int]) -> bool:
    """Checks if triangle contains origin (0, 0)

    Args:
        t: coordinates of triangle in form [x1, y1, x2, y2, x3, y3]

    Returns:
        True if origin lies within triangle
    """
    x_1, y_1 = t[0], t[1]
    x_2, y_2 = t[2], t[3]
    x_3, y_3 = t[4], t[5]

    a = ((y_2 - y_3) * (-x_3) + (x_3 - x_2) * (-y_3)) / ((y_2 - y_3) * (x_1 - x_3) + (x_3 - x_2) * (y_1 - y_3))
    b = ((y_3 - y_1) * (-x_3) + (x_1 - x_3) * (-y_3)) / ((y_2 - y_3) * (x_1 - x_3) + (x_3 - x_2) * (y_1 - y_3))
    g = 1 - a - b

    return (a > 0 and b > 0 and g > 0)


def main():
    triangles = import_text()
    print(sum([contains_origin(t) for t in triangles]))


if __name__ == "__main__":
    main()
