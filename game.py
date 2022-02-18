"""
Defining a class for the game.
By definition, it will have a 3x3 board represented by a single list.
"""

from random import Random
from player import HumanPlayer, RandomComputerPlayer


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
    
    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] ---> [(0, 'x'), (1, 'x') (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board # boolean
    
    def num_empty_squares(self):
        return self.board.count(' ') # number of spaces in the board

    def make_move(self, square, letter):
        # if the move is valid, then make it
        # if invalid, return false

        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    # If 3 in a row anywhere, it's a winner
    def winner(self, square, letter):
        # let's check the rows
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # it's possible to win with diagonals
        # only if the square is an even number
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all the checks fail we don't have a winner
        return False


"""
Returns the winner of the game or None for a tie
"""
def play(game, x_player, o_player, print_game):
    if print_game:
        game.print_board_nums()

    # Starting letter
    letter = 'X'

    """
    There will be an iteration till the game has empty squares.
    The winner will be returned when the loop will be broken
    """

    while game.empty_squares():
        # getting the move from the correct player
        if letter == '0':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # making the move
        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to squrare {square}')
                game.print_board()
                print('')

        if game.current_winner:
            if print_game:
                print(letter + ' wins!')
            return letter
        
        # alterning letters after the move
        if letter == 'X':
            letter == 'O'
        else:
            letter == 'X'
        
        if print_game:
            print("It's a tie.")

if __name__  == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)