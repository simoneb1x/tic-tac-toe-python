# Importing Libraries
import math
import random

""" 
Base Player class.
This will identify the player by the letter (X or O)
"""
class Player:
    def __init__(self, letter):
        # Letter can be X or O
        self.letter = letter

    # The following function make the player available to get the next move
    def get_move(self, game):
        pass


"""
For inheritance, there's another class for computer
"""
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # Gets a random spot for the next move
        square = random.choice(game.available_moves())
        return square 

"""
For inheritance, there's another class for human player
"""
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9)')
            """ 
            Checks if the value is correct.
            If the value isn't an integer, then it's invalid.
            Elif the spot is not available on the board, then it's invalid.
            """
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError("The move is not available!")
                valid_square = True
            except ValueError:
                print("Invalid square, please try again.")
        return val