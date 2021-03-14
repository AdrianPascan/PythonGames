'''
Created on Feb 18, 2019

@author: Adrian
'''
from Square import Square
from random import choice
import pickle


class Game():
    '''
    
    '''


    def __init__(self, board):
        '''
        Constructor for Game class
        '''
        self._board = board
        self._placements = 0
        
    
    def round(self, row, column):
        '''
        Plays a round of the game. 
        In: row, column - strings
        Exception: ValueError - if indexes are not valid
        '''
        
        self._validateSquare(row, column)
        square = Square(int(row), int(column))
        
        if self._placements < 4:
            self._placementRound(square)
        
        else:
            self._movementRound(square)
            
        self._placements += 1
            
    
    def _placementRound(self, square):
        '''
        Plays a round of the placement phase.
        In: square - instance of Square class
        Exception: BoardException, GameException
        '''
        
        self._board.store(square, "X", True)
        
        if self._board.isWon(square):
            raise GameException("Game over! User wins.")
                
        emptySquares = self._board.getSquares()
        
        for available in emptySquares:
            self._board.store(available, "0")
            
            if self._board.isWon(available):
                raise GameException("Game over! Computer wins.")
            self._board.store(available, " ")
                    
        done = False
        
        for available in emptySquares:
            self._board.store(available, "X")
            
            if self._board.isWon(available):
                self._board.store(available, "0")
                done = True
                break
            else:
                self._board.store(available, " ")                
                
        if not done:
            self._board.store(choice(emptySquares), "0")
        
        
    def _movementRound(self, square):
        '''
        Plays a round of the movement phase.
        In: square - instance of Square class
        Exception: BoardException, GameException
        '''
        
        if not self._board.checkSymbol(square, "X"):
            raise ValueError("You can only move an X.")
        
        emptySquare = self._board.getSquares()[0]
        
        if not self._adjacent(square, emptySquare):
            raise ValueError("Can only move an X which is next to the empty square.")
        
        self._board.store(emptySquare, "X")
        self._board.store(square, " ")
                
        if self._board.isWon(emptySquare):
            raise GameException("Game over! User wins.")
        
        zeroSquares = self._board.getSquares("0")
        okSquares = [zeroSquare for zeroSquare in zeroSquares if self._adjacent(zeroSquare, square)]
        
        self._board.store(square, "0")
        
        for current in okSquares:
            
            self._board.store(current, " ")
            
            if self._board.isWon(square):
                raise GameException("Game over! Computer wins.")
            
            self._board.store(current, "0")
        
        self._board.store(choice(okSquares), " ")
    
    
    def _adjacent(self, square1, square2):
        '''
        Checks if two squares are adjacent.
        '''
        if (square1.row == square2.row and square1.column == square2.column) or \
            abs(square1.row - square2.row) > 1 or abs(square1.column - square2.column) > 1:
            return False
        
        return True
                    
    
    def _validateSquare(self, row, column):
        '''
        Validates the indexes of a square of the board.
        In: row, column - strings
        Out: row, column - integers
        Exception: ValueError, if indexes are not valid
        '''
        
        try:
            row = int(row)
            column = int(column)
        except ValueError:
            raise ValueError("Indexes of the square must be integers.")
        
        if row not in [0,1,2] or column not in [0,1,2]:
            raise ValueError("Indexes of the square must be in range [0,2].")
    
    
    def save(self):
        
        with open("board.pickle", "wb") as file:
            pickle.dump(self._board, file)
            
        with open("game.pickle", "wb") as file:
            pickle.dump(self, file)
    
    
    @property
    def message(self):
        if self._placements < 4: 
            return "Placement phase..."
        else:
            return "Movement phase..."
    
    
    @property
    def board(self):
        return str(self._board)
    
    
class GameException(Exception):
    pass
