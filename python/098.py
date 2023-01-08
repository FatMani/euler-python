# -*- coding: utf-8 -*-
"""Project Euler: Problem 98

If we replace letters in words with their numbers, some will be square.
Some of these numbers can be anagrammed into other words. Find all the
square anagram word pairs.

https://projecteuler.net/problem=98
"""
from typing import Dict, List


def import_text() -> List[str]:
    """Reads file to list of words.

    Returns:
        List of words
    """
    text = open("098Input.txt").read()
    text = text.split(",")
    text = [word.strip('"') for word in text]
    return text


def is_anagram(word: str, check_word: str) -> bool:
    """Checks if two words are anagrams.

    Args:
        word: first word to check against
        check_word: word to compare

    Returns:
        True if both are anagrams of each other
    """
    return sorted(word) == sorted(check_word)


def find_anagram_pairs(words: List[str]) -> List[List[str]]:
    """Finds the list of anagram pairs

    Args:
        words: list of words to search

    Returns:
        List of anagram pairs"""
    pairs = []
    for n, word in enumerate(words):
        pair = [word]
        for check_word in words[n + 1:]:
            if is_anagram(word, check_word):
                pair.append(check_word)
        if len(pair) > 1:
            pairs.append(pair)
    return pairs


def find_squares(maximum: int) -> List[int]:
    """Finds the list of squares up to the maximum

    Args:
        maximum: maximum number to square

    Returns:
        List of n**2 for n < maximum
    """
    return [n**2 for n in range(int(maximum**0.5) + 1)]


def find_mapping_dict(square: int, word: str) -> Dict[str, str]:
    """Finds the dictionary to be used for mapping word values

    Args:
        square: square to map onto word
        word: word to map into dict

    Returns:
        Dictionary with value - letter mapping
    """
    values = {}
    for n, digit in enumerate(str(square)):
        letter = word[n]
        # If the letter is in dictionary with a different value, square won't work
        if digit in values and values[digit] != letter:
            return {}
        values[digit] = letter
    return {v: k for k, v in values.items()}


def find_word_value(mapping_dictionary: Dict[str, str], word: str) -> str:
    """Finds the word value by converting letters to digits using given mapping dictionary

    Args:
        mapping_dictionary: dictionary of letter-value pairs
        word: word to convert

    Returns:
        Value of word using the mapping
    """
    value = ""
    for letter in word:
        value += mapping_dictionary[letter]
    return value


def find_solution(words: List[str], squares: List[int]) -> List[int]:
    """Finds the anagramic square pair, if it exists.

    Args:
        words: pair of words to compare
        squares: list of squares to search through

    Returns:
        Anagramic squares if a solution exists, empty list otherwise
    """
    for square in squares:
        # If the squares match in length
        if len(str(square)) == len(words[0]):
            # Map the number onto string, if possible. Then convert second word using same key
            mapping_dictionary = find_mapping_dict(square, words[0])
            if mapping_dictionary:
                second_word_value = find_word_value(mapping_dictionary, words[1])
                if second_word_value[0] != "0" and int(second_word_value) in squares:
                    return [square, int(second_word_value)]
    return []


def main():
    words = import_text()
    pairs = find_anagram_pairs(words)
    # Longest word is 9 letters long, so no square will be bigger than 1bn
    squares = find_squares(1_000_000_000)
    solutions = []
    for p in pairs:
        solutions.extend(find_solution(p, squares))
    print(max(solutions))

if __name__ == '__main__':
    main()
