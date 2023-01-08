# -*- coding: utf-8 -*-
"""Project Euler: Problem 51

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an
eight prime value family.

https://projecteuler.net/problem=51
"""
import euler
from typing import List


def eight_prime_family(patterns: List[str], fixed_digits: List[str]) -> str:
    """Returns the first member of an eight-prime family where 3 digits are repeated.

    Args:
        patterns: patters of fixed and changing digits
        fixed_digits: digits to fill in the fixed spots in the pattern

    Returns:
        first found prime
    """
    for pattern in patterns:
        for fixed in fixed_digits:
            prime_family = []
            for repeated_digit in range(0, 10):
                candidate = ""
                fixed_digit_index = 0
                for c in pattern:
                    if c == "0":
                        candidate += fixed[fixed_digit_index]
                        fixed_digit_index += 1
                    else:
                        candidate += str(repeated_digit)
                # Check that first number isn't a 0 and that candidate is prime
                if candidate[0] != 0 and euler.is_prime(int(candidate)):
                    prime_family.append(candidate)
                # If prime family grows to 8 elements, print out the first one
                if len(prime_family) == 8:
                    return prime_family[0]


def main():
    """Calculates the minium prime.

    We know that a number is divisible by 3 if the sum of its digits is
    divisible by 3. Knowing this, and looking at the mod value of
    repeated digits, we can find that 3 digits must be repeated.
    Additionally, the last digit cannot be repeated - numbers ending
    with 2, 4, 5, 6, 8, 0 are not prime, so we couldn't get an eight
    prime family.
    """
    # Define digit change patterns.
    patterns = ["001110", "010110", "011010", "011100", "100110", "101010", "101100", "110010", "110100", "111000"]
    # Generate 1,2,3-digit combinations for fixed numbers, trim ones ending in 5 or divisible by 3
    fixed_digits = [str(n).zfill(3) for n in range(0, 1000) if n % 3 != 0 and n % 5 != 0]
    print(eight_prime_family(patterns, fixed_digits))


if __name__ == "__main__":
    main()
