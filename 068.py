# -*- coding: utf-8 -*-
"""Project Euler: Problem 68

What is the maximum 16-digit string for a "magic" 5-gon ring?

https://projecteuler.net/problem=68
"""
import itertools


def main():
    """This is a brute force method of solving this problem. This can
    be solved analytically. Firstly, we know that the string must be
    maximised and has 16-digits. This means the outer numbers must be
    6, 7, 8, 9, 10. Therefore the inner repeating digits are 1, 2, 3,
    4 and 5. Each of these numbers appears twice in two different arms.
    """
    fixed = [6, 10, 9, 8, 7]
    perms = [p for p in itertools.permutations([1, 2, 3, 4, 5] * 2)]
    nums = []
    for p in perms:
        n = [(fixed[i], p[2 * i], p[2 * i + 1]) for i in range(0, 5)]
        # Check all triplets have the same value
        if len(set([sum(sub) for sub in n])) == 1:
            # Check the triplet ordering lines up
            if all([n[i - 1][2] == n[i][1] for i in range(5)]):
                nums.append(n)

    # Flatten list and find the string of highest value
    numstr = []
    for n in nums:
        numstr.append("".join(str(char) for tup in n for char in tup))
    print(max(numstr))


if __name__ == "__main__":
    main()
