# -*- coding: utf-8 -*-
"""Project Euler: Problem 89

Find the number of characters saved by writing each of the Roman
numerals in the input in their minimal form.

https://projecteuler.net/problem=89
"""
from typing import List


def import_text() -> List[List[int]]:
    """Reads file to list.

    Retuns:
        2-dimensional list of elements
    """
    M = open("089Input.txt").read()
    M = M.splitlines()
    return M


def roman(n: str) -> str:
    """Finds the minimum representation of a Roman numeral

    Args:
        n: Roman numeral to minimise, must be already in valid format

    Returns:
        Minimum representation of n
    """
    pairs = {"DCCCC": "CM", "CCCC": "CD", "LXXXX": "XC", "XXXX": "XL", "VIIII": "IX", "IIII": "IV"}
    for old in pairs:
        while old in n:
            n = n.replace(old, pairs[old])
    return n


def main():
    original = import_text()
    new = [roman(n) for n in original]
    print(len("".join(original)) - len("".join(new)))


if __name__ == "__main__":
    main()
