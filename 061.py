# -*- coding: utf-8 -*-
"""Project Euler: Problem 61

Find the sum of the only ordered set of six cyclic 4-digit numbers
for which each polygonal type: triangle, square, pentagonal, hexagonal,
heptagonal, and octagonal, is represented by a different number
in the set.

https://projecteuler.net/problem=61
"""
from typing import List
import itertools


def generate_4digit_figurate_number(sides: int) -> List[int]:
    """Generates all 4-digit figurate number for a given number of sides

    Args:
        sides: the number of "sides" for the figurate number;
               e.g. 3 for triangular, 8 for octagonal, etc.

    Returns:
        List of all 4-digit figurate numbers
    """
    if not 2 < sides < 9:
        return []
    figurate_list = []
    figurate_number = 0
    n = 1
    while True:
        if sides == 3:
            figurate_number = n * (n + 1) // 2
        if sides == 4:
            figurate_number = n ** 2
        if sides == 5:
            figurate_number = n * (3 * n - 1) // 2
        if sides == 6:
            figurate_number = n * (2 * n - 1)
        if sides == 7:
            figurate_number = n * (5 * n - 3) // 2
        if sides == 8:
            figurate_number = n * (3 * n - 2)

        if 10000 > figurate_number > 999:
            figurate_list.append(figurate_number)
        elif figurate_number > 10000:
            return figurate_list
        n += 1


def is_cyclical(n: int, m: int) -> bool:
    """Finds if n and m are cyclical numbers

    Args:
        n: first number to check (looks at last two digits)
        m: second number to check (looks at first two digits)

    Returns:
        True if first two digits of m equal last two digits of n
    """
    if n % 100 == m // 100:
        return True
    else:
        return False


def find_cyclicals(numbers: List[int], comparator: int) -> List[int]:
    """Finds all numbers in a list that are cyclicals of a comparator.

    Args:
        numbers: list to search through
        comparator: number of which cyclicals to find

    Returns:
        List of all cyclicals of the number
    """
    return [n for n in numbers if is_cyclical(comparator, n)]


def main():
    numbers = [generate_4digit_figurate_number(n) for n in range(3, 9)]
    possible_permutations = list(itertools.permutations(range(0, 6)))
    possibilities = []
    for order in possible_permutations:
        cyclical_groups = []
        # Find initial list
        for item in numbers[order[0]]:
            for n in find_cyclicals(numbers[order[1]], item):
                cyclical_groups.append([item, n])
        # Generate further steps
        for cycle in cyclical_groups:
            for i in range(2, 6):
                for n in find_cyclicals(numbers[order[i]], cycle[-1]):
                    cycle.append(n)
        # Trim non-6 element lists
        cyclical_groups = [c for c in cyclical_groups if (len(c) == 6)]
        # See if all elements are cyclical (also checks first and last elements' cycle)
        # For some reason the find_cyclicals function returns non-cyclical combinations
        cyclical_groups = [c for c in cyclical_groups if all([is_cyclical(c[i], c[i + 1]) for i in range(-1, 5)])]
        for c in cyclical_groups:
            possibilities.append(c)
    # Sum possibilities and return the set (only unique value)
    print(set([sum(p) for p in possibilities]))

if __name__ == '__main__':
    main()
