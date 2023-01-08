# -*- coding: utf-8 -*-
"""Useful functions for Project Euler

This module contains useful functions for completing Project Euler challenges,
including finding prime numbers, factorisation, checking palindromicity, etc.

Project Euler: https://projecteuler.net/
"""
import collections
import math
import re
from typing import List


def lcm(x: int, y: int) -> int:
    """Finds the least common multiple of two integers.

    Args:
        x: First integer
        y: Second integer

    Returns:
        Least common multiple of x and y
    """
    return (x * y) // math.gcd(x, y)


def is_prime(x: int) -> bool:
    """Checks if integer is prime.

    Args:
        x: integer to check for primality

    Returns:
        True if number is prime, False otherwise.
    """
    x = abs(x)
    if x <= 1:
        return False
    if x == 2:
        return True
    if not x & 1:
        # Excludes all even numbers
        return False

    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def first_n_primes(n: int) -> List[int]:
    """Returns the first n positive prime numbers.

    Args:
        n: count of primes to be generated

    Returns:
        List of prime integers.
    """
    prime_list = [2]
    potential_prime = 3
    while len(prime_list) < n:
        if is_prime(potential_prime):
            prime_list.append(potential_prime)
        potential_prime += 2
    return prime_list


def nth_prime(n: int) -> int:
    """Returns the nth positive prime.

    Args:
        n: index of prime to return (1-indexed)

    Returns:
        nth prime number.
    """
    return first_n_primes(n)[-1]


def primes_less_than(n: int) -> List[int]:
    """Returns primes lower than specified number.

    Args:
        n: upper limit of primes to be found (exclusive)

    Returns:
        List of primes lower than n
    """
    sieve = [True for _ in range(n)]
    sieve[0:1] = [False, False]
    for i in range(2, n):
        if sieve[i]:
            for j in range(2 * i, n, i):
                sieve[j] = False

    primes = []
    for k in range(2, n):
        if sieve[k]:
            primes.append(k)
    return primes


def all_prime_factors(n: int) -> List[int]:
    """Finds prime factors of n

    Args:
        n: number to factorise

    Returns:
        List of prime factors (repetitions allowed)
    """
    factors = []
    i = 2
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def unique_prime_factors(n: int) -> List[int]:
    """Finds unique prime factors of n

    Args:
        n: number to factorise

    Returns:
        List of prime factors (no repetitions)
    """
    return list(set(all_prime_factors(n)))


def divisors(n: int) -> List[int]:
    """Finds all divisors of n

    Depends on the commutative property of multiplication, i.e. 5*2 = 2*5.
    Finds all the divisors below the square root of N and then divides
    N by them to find the pairs.

    Args:
        n: number to find divisors of

    Returns:
        List of divisors of n
    """
    divisors = []
    temp_divisors_list = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
    for j in divisors[::-1]:
        # Exclude square, as it is already in list
        if j ** 2 != n:
            temp_divisors_list.append(n // j)
    divisors.extend(temp_divisors_list)
    return divisors


def count_of_divisors(n: int) -> int:
    """Find the number of unique divisors of a number, including itself and 1

    Args:
        n: number to find the count of divisors of

    Returns:
        Count of divisors of n
    """
    return len(divisors(n))


def sum_of_divisors(n: int) -> int:
    """Finds the sum of all divisors of a number, including itself and 1

    Args:
        n: number to find the sum of divisors of

    Returns:
        Sum of divisors of n
    """
    return sum(divisors(n))


def fibonacci(n: int, _cache={}) -> int:
    """Finds the n-th Fibonacci number.

    Assumes the first number of the sequence is F0 = 0, F1 = 1.

    Args:
        n: index of the Fibonacci number to be found
        _cache: internal memoization dictionary

    Returns:
        n-th Fibonacci number.
    """
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, fibonacci(n - 1) + fibonacci(n - 2))
    else:
        return n


def is_pandigital(n: int, digits_to_check: int = 9) -> bool:
    """ Checks if number contains all digits from 1 to digits_to_check exactly once

    Args:
        n: number to check
        digits: number of digits to check, 10 means 0-inclusive

    Returns:
        True if number contains all digits from 1 to digits_to_check only once
    """
    bit_sum = 0
    for i in str(n):
        bit_sum |= 1 << int(i)
    expected_sum = (2 ** digits_to_check - 1) if (digits_to_check == 10) else (2 ** (digits_to_check + 1) - 2)
    return bit_sum == expected_sum


def string_alphabetic_value(string: str) -> int:
    """Counts the case-insensitive string alphabetic value, where A = 1, B = 2, etc.

    Args:
        string: word for which the value is to be calculated

    Returns:
        Sum of alphabetic value of each string
    """
    string = re.sub("[^A-Z]", "", string.upper())
    return sum(ord(c) - ord("A") + 1 for c in string)


def is_permutation(a: int, b: int) -> bool:
    """Checks if two numbers are permutations of each other.

    Args:
        a: first number to be checked
        b: second number to be checked

    Returns:
        True if both numbers are permutations of each other.
    """
    d = collections.defaultdict(int)
    # Convert numbers to lists
    x, y = [int(i) for i in str(a)], [int(i) for i in str(b)]
    for i in x:
        d[i] += 1
    for i in y:
        d[i] -= 1
    return not any(d.values())
