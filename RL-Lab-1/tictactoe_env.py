# tictactoe_env.py
#
# This is the "environment" part of the RL assignment.
# It just knows the rules of tic tac toe and keeps track of the board.
# It does NOT contain any learning / training logic - that's not part
# of this lab.
#
# Basic idea (from class notes):
#   agent gives an action -> environment updates -> environment gives
#   back next_state, reward, done
#
# Board is stored as a list of 9 numbers:
#   0 = empty cell
#   1 = X (agent)
#  -1 = O (opponent)
#
# cell numbers on the board look like this:
#   0 1 2
#   3 4 5
#   6 7 8


class TicTacToeEnv:

    # all the ways someone can win (rows, cols, diagonals)
    win_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    def __init__(self):
        self.board = [0] * 9
        self.turn = 1          # 1 = X goes, -1 = O goes
        self.game_over = False
        self.winner = None

    def reset(self):
        # start a fresh game (this is basically the "initial state")
        self.board = [0] * 9
        self.turn = 1
        self.game_over = False
        self.winner = None
        return self.get_state()

    def get_state(self):
        # returning a copy so nobody can mess with self.board from outside
        return self.board[:]

    def get_valid_actions(self):
        # only empty cells count as valid moves
        empty_cells = []
        for i in range(9):
            if self.board[i] == 0:
                empty_cells.append(i)
        return empty_cells

    def check_winner(self, player):
        # checks if "player" has 3 in a row somewhere
        for (a, b, c) in self.win_lines:
            if self.board[a] == player and self.board[b] == player and self.board[c] == player:
                return True
        return False

    def board_full(self):
        return 0 not in self.board

    def step(self, action):
        # this is the main function. agent calls this with the cell
        # number it wants to play, and we update everything.

        info = {}

        if self.game_over:
            # shouldn't happen if reset() is called properly
            raise Exception("Game already finished, call reset() first")

        # check if move is not allowed (cell taken / bad index)
        if action < 0 or action > 8 or self.board[action] != 0:
            self.game_over = True
            info["result"] = "illegal move"
            return self.get_state(), -10, self.game_over, info

        # place the mark
        self.board[action] = self.turn

        # did this move win the game?
        if self.check_winner(self.turn):
            self.game_over = True
            self.winner = self.turn
            if self.turn == 1:
                reward = 1
                info["result"] = "win"
            else:
                reward = -1
                info["result"] = "loss"

        # or is it a draw (board full, no winner)
        elif self.board_full():
            self.game_over = True
            reward = 0
            info["result"] = "draw"

        # game still going
        else:
            reward = 0
            info["result"] = "ongoing"

        # switch turn to other player for next step
        self.turn = self.turn * -1

        return self.get_state(), reward, self.game_over, info

    def render(self):
        # prints the board so we can actually see what's happening
        symbols = []
        for cell in self.board:
            if cell == 1:
                symbols.append("X")
            elif cell == -1:
                symbols.append("O")
            else:
                symbols.append("-")

        print(symbols[0], "|", symbols[1], "|", symbols[2])
        print("---------")
        print(symbols[3], "|", symbols[4], "|", symbols[5])
        print("---------")
        print(symbols[6], "|", symbols[7], "|", symbols[8])
        print()
