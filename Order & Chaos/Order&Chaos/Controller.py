'''
Created on Feb 21, 2019

@author: Adrian
'''
from Domain import Square
from random import choice
from Repository import RepoError

class Controller():
    '''
    
    '''


    def __init__(self, repository):
        '''
        Constructor for Controller class
        '''
        self._repository = repository
        self._moves = 0
        self._lastX = Square(0,0)
        self._lastO = Square(0,0)
    
    
    def round(self, row, column, symbol):
        
        square = Square(row, column)
        self._validate(square, symbol)
        
        self._play(square, symbol)
        
        self._moves += 2
        
        if self._tie():
            raise GameException("chaos")
        
    
    def _validate(self, square, symbol):
        
        errors = ""
        
        if square.row not in range(1,7) or square.column not in range(1,7):
            errors += "Row / column must be in range [1,6].\n"
        
        if symbol not in ["X", "O"]:
            errors += "Invalid symbol.\n"
            
        if self._moves == 0 and symbol == "O":
            errors += "First moves 'order'.\n"
            
        if not errors == "":
            raise ValueError(errors)
    
    
    def _play(self, square, symbol):
        '''
        Plays a round of the game in which the user made a move with the given symbol.
        '''
        
        other = "O"
        if symbol == "O":
            other = "X"
        
        self._repository.store(square, symbol, True)
        
        if self._repository.isWon(square):
            raise GameException("order")
        
        if symbol == "X":
            self._lastX = square
        else:
            self._lastO = square
        
                
        options = self._repository.getSquares()
        
        for current in options:
                            
            self._repository.store(current, symbol)
            
            if self._repository.isWon(current):
                
                self._repository.store(current, other)
                
                if self._repository.isWon(current):
                    options.remove(current)
                else:
                    return
            
            self._repository.store(current, " ")
        
        option = choice(options)
        self._repository.store(option, other)


    def _tie(self):
        '''
        Checks if the board is full.
        '''
        
        if self._moves == 36:
            return True
        
        return False
    
    
    def __str__(self):
        return str(self._repository)
    

class GameException(Exception):
    
    def __str__(self, *args, **kwargs):
        return "Game over! " + Exception.__str__(self, *args, **kwargs).capitalize() + " wins."
        
        