'''
Created on Feb 18, 2019

@author: Adrian
'''
import texttable
from Square import Square

class Board():
    '''
    
    '''


    def __init__(self):
        '''
        Constructor for Board class
        '''
        self._data = [[0] * 3] + [[0] * 3] + [[0] * 3]
        self._symbol = {0: " ", 1: "X", 2: "0"}
        self._code = {" ": 0, "X": 1, "0": 2}
    
    
    def store(self, square, symbol, empty = False):
        '''
        Places the given symbol on a square
        '''
        
        if empty:
            if self._data[square.row][square.column] != 0:
                raise BoardException("Square not empty.")
            
        self._data[square.row][square.column] = self._code[symbol]
    
    
    def isWon(self, square):
        '''
        Checks if there's a won relative to a given square (3 similar symbols are lined up).
        In: square - instance of Square class
        '''
        
        row = square.row
        column = square.column
        
        if (self._data[row][0] * self._data[row][1] * self._data[row][2]) in [1,8]:
            return True
        
        if (self._data[0][column] * self._data[1][column] * self._data[2][column]) in [1,8]:
            return True
        
        if row == column:
            if (self._data[0][0] * self._data[1][1] * self._data[2][2]) in [1,8]:
                return True
            
        if row + column == 2:
            if (self._data[0][2] * self._data[1][1] * self._data[2][0]) in [1,8]:
                return True
            
        return False
            
    
    def getSquares(self, symbol = " "):
        '''
        Returns a list of the squares containing the symbol.
        '''
        
        code = self._code[symbol]
        squares = []
        
        for _row in [0,1,2]:
            for _column in [0,1,2]:
                if self._data[_row][_column] == code:
                    squares.append( Square(_row, _column) )
                    
        return squares
    
    
    def checkSymbol(self, square, symbol):
        '''
        Checks if the square contains the given symbol.
        '''
        if self._data[square.row][square.column] == self._code[symbol]:
            return True
        return False
    
        
    def __str__(self):
        
        board = texttable.Texttable()
        
        for row in self._data:
            
            symbolRow = []
            
            for code in row:
                symbolRow.append(self._symbol[code])
            
            board.add_row(symbolRow)
            
        return board.draw()
    
    
class BoardException(Exception):
    pass
