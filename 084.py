# -*- coding: utf-8 -*-
"""Project Euler: Problem 84

Find the three most likely fields to land on in a game of Monopoly
which uses two 4-sided dice instead of 6-sided.

https://projecteuler.net/problem=84
"""
import random
from typing import Tuple


def roll2d4() -> Tuple[int, int]:
    """Rolls two 4-sided dice.

    Returns:
        Tuple containing two results of the roll
    """
    return (random.randint(1, 4), random.randint(1, 4))


def chance(loc: int, ch: int) -> Tuple[int, int]:
    """Picks a card from the Chance stack.

    Args:
        loc: current location of token
        ch: card which needs to be drawn

    Returns:
        Tuple of the new location and next card to draw in the form
        (loc, ch)
    """
    R = sorted([5, 15, 25, 35] + [loc])
    U = sorted([12, 28] + [loc])
    next_R = R[(R.index(loc) + 1) % len(R)]
    next_U = U[(U.index(loc) + 1) % len(U)]
    new_loc = ([0, 10, 11, 24, 39, 5, next_R, next_R, next_U, loc - 3] + [loc] * 6)[ch]
    new_ch = (ch + 1) % 16
    return new_loc, new_ch


def community_chest(loc: int, cc: int) -> Tuple[int, int]:
    """Picks a card from the Community Chest stack.

    Args:
        loc: current location of token
        cc: card which needs to be drawn

    Returns:
        Tuple of the new location and next card to draw in the form
        (loc, cc)
    """
    return ([0, 10] + [loc] * 14)[cc], (cc + 1) % 16


def main():
    # Initialise values
    loc, cc, ch = 0, 0, 0
    repeats = 1_000_000
    visits = [0] * 40
    doubles = [False, False]

    for _ in range(repeats):
        r = roll2d4()
        doubles.append(r[0] == r[1])
        loc = (loc + sum(r)) % 40

        if sum(doubles[-3:]) == 3 or loc == 30:
            # 3 consecutive doubles of G2J square
            loc = 10
        if loc in [7, 22, 36]:
            # Chance cards
            loc, ch = chance(loc, ch)
        if loc in [2, 17, 33]:
            # Community chest cards
            loc, cc = community_chest(loc, cc)
        visits[loc] += 1

    frequency = [(100 * visit_count / repeats, square) for square, visit_count in enumerate(visits)]
    print(sorted(frequency, reverse=True)[:3])


if __name__ == "__main__":
    main()
