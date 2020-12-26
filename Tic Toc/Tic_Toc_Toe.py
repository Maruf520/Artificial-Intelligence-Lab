from math import inf
import sys, os

HUMAN = 1
COMP = -1

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

MSG = ""


def evaluate(state):
    """
    Perform heuristic evaluation from board.
    Heuristic - allow the computer to discover the solution
    of some problems by itself.
    """
    if wins(state, COMP):
        score = -1
    elif wins(state, HUMAN):
        score = 1
    else:
        score = 0

    return score

def empty_cells(state):
    """Extract the remainder of board"""
    cells = [] # it contains all empty cells

    # Use enumerate for easy indexing
    for i, row in enumerate(state):
        for j, col in enumerate(row):
            if state[i][j] == 0:
                cells.append([i, j])

    return cells