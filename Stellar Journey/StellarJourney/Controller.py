'''
Created on Feb 22, 2019

@author: Adrian
'''

class Controller():
    '''
    
    '''


    def __init__(self, repository):
        '''
        Constructor for Controller class
        '''
        self._repository = repository
    
    
    def getGrid(self):
        
        return self._repository.grid()
    
    
    def cheat(self):
        
        return self._repository.grid(False)
    
    def warp(self, square):
        '''
        Executes the wrap command.
        In: square - Square instance
        Exceptions: ValueError, if square not valid
                    RepoError, if a star is in this square
                    GameOver, if a blingon is in this square
        '''
        
        self._validateSquare(square)
        
        if not self._repository.sameLine(square):
            raise ValueError("Square not on the same rank, file or diagonal.")
        
        if self._repository.isSymbol(square, "*"): 
            raise ValueError("Star in the way.")
        
        if self._repository.isSymbol(square, "B"):
            raise GameOver("computer")
        
        self._repository.moveEndeavour(square)
    
    
    def _validateSquare(self, square):
        '''
        Validates the given square.
        In: square - Square instance
        Exceptions: ValueError
        '''
        
        errors = ""
        
        if square.row not in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            errors += "Row must be one of the letters: A, B, C, D, E, F, G, H.\n"
            
        if square.column not in range(1, 9):
            errors += "Column must be in range [1,8]."
            
        if errors != "":
            raise ValueError(errors)
        
        
    def fire(self, square):
        
        self._validateSquare(square)
        
        self._repository.fire(square)
        
        
class GameOver(Exception):
    
    def __str__(self, *args, **kwargs):
        return "Game over! " + Exception.__str__(self, *args, **kwargs).capitalize() + " wins."