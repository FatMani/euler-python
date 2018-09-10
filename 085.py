# -*- coding: utf-8 -*-
"""Project Euler: Problem 85

Although there exists no rectangular grid that contains exactly two
million rectangles, find the area of the grid with the nearest solution

https://projecteuler.net/problem=85
"""


def main():
    """Any rectangle in a provided grid can be formed by choosing two
    horizontal lines and two vertical lines. In such a grid there are
    (h + 1) horizontal lines and (w + 1) vertical lines, where h and w
    are the height and width respectively. Therefore the total number
    of rectangles that can be formed is h_C_2 * w_C_2, where n_C_r is
    the number of combinations.

    This can be further simplified by expanding the terms, to find that
        n = (h + 1) * h * (w + 1) * w / 4
    Rearranging this for w we can find candidates for w and from that
    calculate n's for particular h-w pairs.
    """
    areas = []
    target = 2_000_000
    for h in range(1, 1001):
        w = int(round(-0.5 + 0.5 * (1 + (16 * target) / (h ** 2 + h)) ** 0.5))
        n = ((h + 1) * h * (w + 1) * w) // 4
        areas.append((abs(n - target), h * w))
    areas = sorted(areas, reverse=True)
    print(areas[-1])


if __name__ == "__main__":
    main()
