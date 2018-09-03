# -*- coding: utf-8 -*-
"""Project Euler: Problem 80

For the first one hundred natural numbers, find the total of the
digital sums of the first one hundred decimal digits for all the
irrational square roots.

https://projecteuler.net/problem=80
"""


def sqr_exp(n: int, d: int) -> int:
    """Calculates the d digits long decimal expansion of a square root of n.

    Based on the algorithm used for calculating the square root of any
    integer (Based on: https://en.wikipedia.org/wiki/
    /Methods_of_computing_square_roots#Digit-by-digit_calculation):
        1. Find the floor of the sqr(n). This is the first digit of the
           expansion (e).
        2. Subtract the square of this number to find the remainder.
        3. Append "00" to this remainder (i.e. multiply by 100); this
           is the division term
        4. Find a number x such that (2*e) concatenated with x, 
           multiplied by x (i.e. [20*e + x]*x) is as close as possible
           to the division term
        5. Append x to the expansion
        6. Subtract [20*e + x]*x from the division term. Append "00".
           This is the new division term
        7. Repeat steps 4 - 6 as needed

    Example for sqrt(2):
        1. Floor(sqrt(2)) = 1 (floor of 1.414...), therefore "e" starts
           with 1.
        2. 2 - 1^2 = 1
        3. Division term is therefore 100
        4. 20*e = 20, therefore check 20*0, 21*1, 22*2, 23*3, etc.
           Largest number below 100 is 24*4 = 96
        5. Next expansion term is 4, hence e = 14
        6. 100 - 96 = 4, so next division term is 400
        7. 20*e = 280, so check 280*0, 281*1, etc. until the largest
           number below 400 is found. This is 281*1.
        8. Hence e = 141
        9. 400 - 281 = 119, so next division term is 11900
        10. Continue as needed

    Args:
        n: number of which the root is to be computed
        d: number of digits in expansion

    Returns:
        String containing the decimal expansion of the root. Includes
        the ones digit.
    """
    # Perfect squares
    if int(n ** 0.5) == n ** 0.5:
        return int(n ** 0.5)

    # Other numbers


def main():
    pass


if __name__ == "__main__":
    main()

