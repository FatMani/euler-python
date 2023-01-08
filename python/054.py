# -*- coding: utf-8 -*-
"""Project Euler: Problem 54

In a set of poker hands, how many games does the first player win?

https://projecteuler.net/problem=54

Solution based on Gareth Rees' solution from:
https://codereview.stackexchange.com/a/95075/
"""
from collections import Counter
from enum import IntEnum, unique
from typing import List, Tuple


def hands_from_txt() -> List[str]:
    """ Loads list of hands from input file.

    Returns:
        List of cards in hand 1 and in hand 2
    """
    raw_input = open("054Input.txt", "r").readlines()
    output = []
    for line in raw_input:
        output.append(line.split())
    return output


@unique
class Quality(IntEnum):
    """Quality of a poker hand. Higher values beat lower values."""

    high_card = 1
    pair = 2
    two_pairs = 3
    three = 4
    straight = 5
    flush = 6
    full_house = 7
    four = 8
    straight_flush = 9


def canonical(hand: List[str]) -> Tuple[int, List[int]]:
    """Return the canonical form of the poker hand.

    Returns the hand as a tuple (q, r) where q is a value from the Quality
    enumeration, and r is a list of the distinct card ranks in the hand
    (from 1=low ace to 14=high ace), ordered in descreasing order by
    frequency and then by rank. These canonical forms can be compared to
    see who wins. The hand must b a sequence of five cards given as
    two-character strings in the form 2H, TS, JC etc.

    Args:
        hand: list of in the form of [value][suit], e.g. 2H, JC, KS

    Returns:
        A tuple containing the quality of the card, and then the list of
        cards by decreasing frequency
    """
    # Convert hand's ranks to list
    ranks = sorted("--23456789TJQKA".find(rank) for rank, _ in hand)
    # Check if there's only one suit in hand, if yes, it's a flush
    flush = len(set(suit for _, suit in hand)) == 1
    # Find ace-low straight and convert to sequential format
    if ranks == [2, 3, 4, 5, 14]:
        ranks = [1, 2, 3, 4, 5]
    # If ranks are from (lowest) to (lowest + 5), it's a straight
    straight = ranks == list(range(ranks[0], ranks[0] + 5))
    # Returns sorted list of card frequencies, from least to most
    card_counter = Counter(ranks)
    counts = sorted(card_counter.values())
    # List of cards ordered first by frequency, then by card value
    distinct_ranks = sorted(card_counter, reverse=True, key=lambda v: (card_counter[v], v))
    # Assign quality
    if flush and straight:
        q = Quality.straight_flush
    elif counts == [1, 4]:
        q = Quality.four
    elif counts == [2, 3]:
        q = Quality.full_house
    elif flush:
        q = Quality.flush
    elif straight:
        q = Quality.straight
    elif counts == [1, 1, 3]:
        q = Quality.three
    elif counts == [1, 2, 2]:
        q = Quality.two_pairs
    elif counts == [1, 1, 1, 2]:
        q = Quality.pair
    else:
        q = Quality.high_card
    return q, distinct_ranks


def main():
    hands = hands_from_txt()
    # True if P1 wins. Sums it all up for total P1 wins.
    player_1_wins = sum([canonical(cards[:5]) > canonical(cards[5:]) for cards in hands])
    print(player_1_wins)


if __name__ == "__main__":
    main()
