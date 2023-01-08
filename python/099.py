# -*- coding: utf-8 -*-
"""Project Euler: Problem 99

Find the largest numerical number on a list

https://projecteuler.net/problem=99
"""
from typing import List
from math import log


def import_text() -> List[str]:
    """Reads file to list of words.

    Returns:
        List of words
    """
    text = open("099Input.txt").read()
    text = text.splitlines()
    numbers = [entry.split(",") for entry in text]
    return numbers


def main():
    """This problem can be simplified by using logarithms.
    We know that if:
        a^b > c^d
    then:
        b*log(a) > c*log(d)
    Therefore all the numbers can be converted to logarithmic values
    and the maximum found that way.
    """
    pairs = import_text()
    numeric_value = []
    for base, exponent in pairs:
        numeric_value.append(int(exponent) * log(int(base)))
    # +1 needed to convert from 0-indexed list to 1-indexed line number
    print(numeric_value.index(max(numeric_value)) + 1)

if __name__ == '__main__':
    main()
