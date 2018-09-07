# -*- coding: utf-8 -*-
"""Project Euler: Problem 83

Find the minimal path sum, in an 80 by 80 matrix, from the top-left to
the bottom-right column by moving left, right, up or down.

https://projecteuler.net/problem=83
"""
from typing import List
import networkx


def import_text() -> List[List[int]]:
    """Reads file to list.

    Retuns:
        2-dimensional list of elements
    """
    M = open("083Input.txt").read()
    M = M.splitlines()
    M = [i.split(",") for i in M]
    M = [[int(j) for j in i] for i in M]
    return M


def main():
    M = import_text()
    G = networkx.DiGraph()

    for i in range(len(M)):
        for j in range(len(M)):
            near = [
                (i + dx, j + dy)
                for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]
                if (0 <= (i + dx) < len(M)) and (0 <= (j + dy) < len(M))
            ]
            for (x, y) in near:
                G.add_edge((i, j), (x, y), weight=M[x][y])
    # Based on Dreamshire solution - M[0][0] must be added as path doesn't consider first node's weight
    print(networkx.dijkstra_path_length(G, (0, 0), (len(M) - 1, len(M) - 1)) + M[0][0])

if __name__ == "__main__":
    main()
