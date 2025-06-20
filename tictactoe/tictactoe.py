"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    O_count = sum(row.count("O") for row in board)
    X_count = sum(row.count("X") for row in board)

    return O if O_count < X_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row in range(len(board)):
        for col in range(len(board)):
            if (board[row][col] == EMPTY):
                actions.add((row, col))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardstate = copy.deepcopy(board)
    i, j = action
    if action not in actions(board):
        raise Exception("you can't do that move")
    boardstate[i][j] = player(board)
    return boardstate


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    players = [X, O]
    for player in players:
        if horizontal_win(board, player) or vertical_win(board, player) or diagonal_win(board, player):
            return player
    return None


# winning functions
def horizontal_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    return False


def vertical_win(board, player):
    column = []
    for row in range(3):
        for col in range(3):
            column.append(board[col][row])
        if column.count(player) == 3:
            return True
        else:
            column = []
    return False


def diagonal_win(board, player):
    diagonal1, diagonal2, diagonal, checks = [], [(2, 0), (1, 1), (0, 2)], [], 0

    for row in range(3):
        diagonal1.append((row, row))

    while checks <= 2:
        for coord in diagonal1:
            diagonal.append(board[coord[0]][coord[1]])
        if diagonal.count(player) == 3:
            return True
        else:
            diagonal1 = diagonal2
            diagonal = []
            checks += 1
    return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    empty_cells = sum(row.count(EMPTY) for row in board)
    return not empty_cells


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]

    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]


def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
