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
        pass

"""
For inheritance, there's another class for human player
"""
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass
