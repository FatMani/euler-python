# -*- coding: utf-8 -*-
"""Project Euler: Problem 55

How many Lychrel numbers are there below 10,000?

https://projecteuler.net/problem=55
"""


def rev(n: int) -> int:
    """ Reverses an integer, e.g. 47 becomes 74

    Args:
        n: integer to reverse

    Returns:
        Reverse of digits of integer
    """
    return int(str(n)[::-1])


def is_Lychrel(n: int, depth: int = 50) -> bool:
    """ Finds if number is a Lychrel number

    Lychrel numbers is a number that doesn't form a palindrome by adding it
    to its reverse. The process can be repeated multiple steps, up to
    the required depth.

    Args:
        n: number to check
        depth: number of iterations to allow for check; default 50

    Returns:
        False is number eventually produces a palindrome, True otherwise
    """
    for i in range(depth + 1):
        n += rev(n)
        if n == rev(n):
            return False
    return True


def main():
    print(sum([is_Lychrel(n) for n in range(10001)]))


if __name__ == "__main__":
    main()
