"""
Defining a class for the game.
By definition, it will have a 3x3 board represented by a single list.
"""

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None # tracking of the winner

    def print_board(self):
        # Getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        # This is telling us what number corresponds to what box
        # It gives what indeces are in the rows for each of the rows
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |") 
             