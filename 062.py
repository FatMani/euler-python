# -*- coding: utf-8 -*-
"""Project Euler: Problem 62

Find the smallest cube for which exactly five
permutations of its digits are cube.

https://projecteuler.net/problem=62
"""


def main():
    sorted_cubes = []
    i = 0

    while True:
        # Cube as list of digits
        c = list(str(i**3))
        # Sort it by digits
        c = sorted(c)
        # Add sorted by digits to list
        sorted_cubes.append(c)
        # See if the sorted cubes' count is 5
        if sorted_cubes.count(c) == 5:
            # If yes, print index of first occurence ^ 3
            print(sorted_cubes.index(c) ** 3)
            break
        i += 1


if __name__ == "__main__":
    main()
