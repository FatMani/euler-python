# -*- coding: utf-8 -*-
"""Project Euler: Problem 59

Find the sum of the ASCII values in the original text, given its
ciphertext and knowing the XOR key is a three-letter lowercase word.

https://projecteuler.net/problem=59
"""
from typing import List


def read_ciphertext() -> List[int]:
    """Reads ciphertext to a list of integers

    Returns:
        List of integers listed in the input file
    """
    string_list = open("059Input.txt").read().split(",")
    return [int(n) for n in string_list]


def xor_decode(ciphertext: List[int], key: List[int]) -> List[int]:
    """Decodes ciphertext based on key.

    Args:
        ciphertext: list of integers in ciphertext
        key: arbitrary length key

    Returns:
        List of integers for plaintext
    """
    plainint_list = []
    for i in range(len(ciphertext)):
        plainint_list.append(ciphertext[i] ^ key[i % len(key)])
    return plainint_list


def ascii_decode(plainint: List[int]) -> str:
    """Converts list of integers to ASCII.

    Args:
        plainint: list of integers representing plaintext ascii codes

    Returns:
        String representing ASCII values of plainint
    """
    return "".join([chr(n) for n in plainint])


def main():
    ciphertext = read_ciphertext()
    alphabet_range = range(ord("a"), ord("z") + 1)
    keys = [(a, b, c) for a in alphabet_range for b in alphabet_range for c in alphabet_range]

    for key in keys:
        plainint_guess = xor_decode(ciphertext, key)
        plaintext_guess = ascii_decode(plainint_guess)
        if plaintext_guess.find(" the ") > 0 and plaintext_guess.find(" and ") > 0:
            print(sum(plainint_guess))
            break


if __name__ == "__main__":
    main()
