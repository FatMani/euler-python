# -*- coding: utf-8 -*-
"""Project Euler: Problem 96

Find the sum of first three digits of 50 sudoku puzzles.

https://projecteuler.net/problem=96
"""
from typing import List, Tuple


def is_row_ok(grid: List[List[int]], row: int, number: int) -> bool:
    """Checks if number doesn't already appear in row of grid

    Args:
        grid: 2D sudoku grid
        row: row number, 0 indexed
        number: number to check against

    Returns:
        True if number doesn't appear in row, false otherwise
    """
    return all([number != grid[row][col] for col in range(9)])


def is_column_ok(grid: List[List[int]], col: int, number: int) -> bool:
    """Checks if number doesn't already appear in row of grid

    Args:
        grid: 2D sudoku grid
        col: column number, 0 indexed
        number: number to check against

    Returns:
        True if number doesn't appear in column, false otherwise
    """
    return all([number != grid[row][col] for row in range(9)])


def is_square_ok(grid: List[List[int]], row: int, col: int, number: int) -> bool:
    """Checks if number doesn't already appear in 3x3 square of grid

    Args:
        grid: 2D sudoku grid
        row: row number, 0 indexed
        col: column number, 0 indexed
        number: number to check against

    Returns:
        True if number doesn't appear in square, false otherwise
    """
    square_first_row, square_first_column = 3 * (row // 3), 3 * (col // 3)
    for i in range(square_first_row, square_first_row + 3):
        for j in range(square_first_column, square_first_column + 3):
            if grid[i][j] == number:
                return False
    return True


def is_position_valid(grid: List[List[int]], row: int, col: int, number: int) -> bool:
    """Checks if number can be placed in position and grid remain valid

    Args:
        grid: 2D sudoku grid
        row: row number, 0 indexed
        col: column number, 0 indexed
        number: number to check against

    Returns:
        True if number doesn't appear in square, false otherwise
    """
    if is_row_ok(grid, row, number) and is_column_ok(grid, col, number) and is_square_ok(grid, row, col, number):
        return True
    return False


def find_next_position_to_fill(grid: List[List[int]], row: int, col: int) -> Tuple[int, int]:
    """Finds the next x-y position to attempt to fill with number

    Args:
        grid: 2D sudoku grid
        row: row number, 0 indexed
        col: column number, 0 indexed

    Returns:
        x, y coordinate tuple. (-1, -1) if all positions have been filled
    """
    # Look from (row, col) position forward first
    for x in range(row, 9):
        for y in range(col, 9):
            if not grid[x][y]:
                return x, y

    # If no positions can be filled ahead, check rest of grid
    for x in range(9):
        for y in range(9):
            if not grid[x][y]:
                return x, y

    return -1, -1


def solve_sudoku(grid: List[List[int]], row: int = 0, col: int = 0) -> bool:
    """Solves a sudoku.

    Args:
        grid: Sudoku grid
        row: row to start solving at
        col: column to start solving at

    Returns:
        True if sudoku has been solved, False otherwise
    """
    x, y = find_next_position_to_fill(grid, row, col)
    # If all positions have been filled
    if x == -1:
        return True

    # Otherwise check which number can be placed into cell and try to solve sudoku with it
    for number in range(1, 10):
        if is_position_valid(grid, x, y, number):
            grid[x][y] = number
            if solve_sudoku(grid, x, y):
                return True
            # If sudoku can't be solved with this number, undo
            grid[x][y] = 0

    # If solution can't be found
    return False

def import_text() -> List[List[List[int]]]:
    """Reads file to array of sudoku arrays.

    Retuns:
        1-dimensional list of 2-dimensional elements
    """
    L = []
    P = []
    M = open("096Input.txt").read()
    M = M.splitlines()
    for puzzle in range(50):
        L.append(M[10*puzzle+1:10*puzzle+10])

    for puzzle in L:
        P.append([])
        for row in puzzle:
            P[-1].append([int(n) for n in row])
    return P

sudokus = import_text()
s = 0
for sudoku in sudokus:
    grid = sudoku   
    if solve_sudoku(grid):
        s += int(str(grid[0][0]) + str(grid[0][1]) + str(grid[0][2]))

print(s)