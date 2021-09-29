"""Sliding Puzzle
Prof. O and _____
2021-09-16 first draft

A Sliding Puzzle is represented by a string
whose length is a perfect square
of an integer in [2, 6] (i.e., 4, 9, 16, 25, or 36).
It contains only digits (0-9) and capital letters (A-Z),
exactly ONE of which (typically 0) is "empty"
and is represented by a hyphen (-).

On screen, however, the layout is an NxN square.
Legal moves consist of sliding a tile
up, down, left, or right (but never diagonally)
into the empty spot (-).

The puzzle is in the "solved" state when
all its digits and letters are in ascending order
(with digits before letters, as in ASCII and Unicode)
and the empty spot is at the beginning or end
(never in the middle).

References:
https://mathworld.wolfram.com/15Puzzle.html
https://lorecioni.github.io/fifteen-puzzle-game/
https://15puzzle.netlify.app/
"""

from typing import Tuple

def rows_from_puzzle(puzzle : str) -> str:
    """Returns a string with a newline between rows of the puzzle.
    """
    return puzzle # TODO: write tests and replace this stub

def is_solved(puzzle : str) -> bool:
    """Determines whether puzzle is solved (as defined above).
    """
    return False # TODO: write tests and replace this stub

def is_legal_move(puzzle : str, tile_to_move : str) -> bool:
    """Determines whether it is possible to move tile_to_move into the empty spot.
    """
    return tile_to_move != "-" # TODO: write tests and replace this stub

def puzzle_with_move(puzzle : str, tile_to_move : str) -> str:
    """Move tile_to_move into the empty slot (-).
    """
    return puzzle # TODO: write tests and replace this stub

def space_puzzle(puzzle : str) -> str:
    return " " + " ".join(rows_from_puzzle(puzzle))

def play_puzzle(puzzle : str) -> None:
    moves = 0
    while not is_solved(puzzle):
        print(f"\nCurrent puzzle state:\n{space_puzzle(puzzle)}")
        tile_to_move = "-"
        moves += 1
        print(f"Move #{moves}")
        while not is_legal_move(puzzle, tile_to_move):
            tile_to_move = input("Which tile would you like to move into the empty spot? ")
        puzzle = puzzle_with_move(puzzle, tile_to_move)
    print(f"\nSolved!\n{space_puzzle(puzzle)}")
    print(f"You solved the puzzle in {moves} moves!")

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    play_puzzle("1-32")
