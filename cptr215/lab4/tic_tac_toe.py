"""Tic Tac Toe
A tic-tac-toe (TTT) board is represented internally as a string
whose length is a perfect square of an integer in [3,10].
"""

from typing import List

SIDE_FROM_LEN = { n*n: n for n in range(3, 11) }

def simple_print(board: str) -> None:
    """
    >>> simple_print("XOXOXOXOX")
    XOX
    OXO
    XOX
    """
    for pos in range(len(board)):
        print(board[pos], end="")
        if (pos + 1) % 3 == 0:
            print()

def list_from_string(board: str) -> List[List[str]]:
    """
    >>> list_from_string("XOXOXOXOX")
    [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
    >>> list_from_string("X   O   X   O  X")
    [['X', ' ', ' ', ' '], ['O', ' ', ' ', ' '], ['X', ' ', ' ', ' '], ['O', ' ', ' ', 'X']]
    """
    size = SIDE_FROM_LEN[len(board)]
    return [list(board[start_pos:start_pos+size]) \
            for start_pos in range(0, len(board), size)]

def pretty_string_from_board(board: str) -> str:
    """
    >>> print(pretty_string_from_board("XOXOXOXOX"))
     X | O | X
    ---+---+---
     O | X | O
    ---+---+---
     X | O | X
    <BLANKLINE>
    >>> pretty_string_from_board("XOXOXOXOX")
    ' X | O | X \\n---+---+---\\n O | X | O \\n---+---+---\\n X | O | X \\n'
    """
    divider = "+".join([ "---" for _ in range(SIDE_FROM_LEN[len(board)]) ]) + "\n"
    board = list_from_string(board)
    return divider.join([ "|".join([ f" {piece} " for piece in row ]) + "\n" for row in board])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
