# -*- coding: utf-8 -*-
import math
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
    if not x & 1:  # Excludes all even numbers
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


# Eratosthenes sieve
# Returns all positive primes less than upperLimit
def primes_less_than(upper_limit):
    sieve = [True for _ in range(upper_limit + 1)]
    sieve[0:1] = [False, False]
    for start in range(2, upper_limit + 1):
        if sieve[start]:
            for i in range(2 * start, upper_limit + 1, start):
                sieve[i] = False
    primes = []
    for i in range(2, upper_limit + 1):
        if sieve[i]:
            primes.append(i)
    return primes


# Number of divisors
# Finds the number of divisors for a given integer, including itself and 1
def number_of_divisors(n):
    divisor_count = 0
    upper_bound = int(math.sqrt(n))
    for i in range(1, upper_bound + 1):
        if n % i == 0:
            divisor_count = divisor_count + 2
    # Check for perfect squares
    if upper_bound ** 2 == n:
        divisor_count = divisor_count + 1
    return divisor_count


# Sum of divisors
# Finds the sum of an integer's whole divisors, not including itself
def sum_of_divisors(n):
    divisor_sum = 0
    upper_bound = int(n / 2)
    for i in range(1, upper_bound + 1):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum


# nth Fibonacci number
def fibonacci(n, _cache={}):
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, fibonacci(n - 1) + fibonacci(n - 2))
    else:
        return n


# Pandigital check
# Checks if a number n is pandigital to the number of specified digits, excl. 0
def is_pandigital_excl_zero(n, digits_to_check):
    if len(str(n)) > digits_to_check or digits_to_check > 9:
        return False
    else:
        count = 0
        while n > 0 and n % 10 != 0:
            count += 1 << ((n % 10) - 1)
            n //= 10
        if count == (2 ** digits_to_check - 1):
            return True
        else:
            return False


# Counts string value where A = 1, B = 2, C = 3, etc. case independent
# Might not work with punctuation or accented letters
def count_string_value(string):
    return sum(ord(c) - ord("A") + 1 for c in string.upper())
