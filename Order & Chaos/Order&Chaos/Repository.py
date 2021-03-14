'''
Created on Feb 21, 2019

@author: Adrian
'''
from texttable import Texttable
from Domain import Square


class Repository(object):
    '''
    
    '''
        
    def __init__(self):
        '''
        Constructor for Repository class
        '''
        
        self._data = []
        for row in range(7):
            self._data.append([1] * 7)
            
        self._code = {" ": 1, "O": 2, "X": 3}
        self._symbol = {1: " ", 2: "O", 3: "X"}
    
    
    def store(self, square, symbol, validate = False):
        
        if validate == True:
            if self._data[square.row][square.column] != 1:
                raise RepoError("Square not empty.")
        
        self._data[square.row][square.column] = self._code[symbol]
        
        
    def isWon(self, square):
        '''
        Checks if there are 5 same symbols in line relative to a given square.
        '''
        
        product = 1   
             
        for column in range(1,7):
            product *= self._data[square.row][column]
        
        if product // self._data[square.row][1] in [2 ** 5, 3 ** 5] or product // self._data[square.row][6] in [2 ** 5, 3 ** 5]:
            return True
        
        
        product = 1   
             
        for row in range(1,7):
            product *= self._data[row][square.column]
        
        if product // self._data[1][square.column] in [2 ** 5, 3 ** 5] or product // self._data[6][square.column] in [2 ** 5, 3 ** 5]:
            return True
        
        
        if square.row == square.column:
            
            product = 1   
             
            for index in range(1,7):
                product *= self._data[index][index]
            
            if product // self._data[1][1] in [2 ** 5, 3 ** 5] or product // self._data[6][6] in [2 ** 5, 3 ** 5]:
                return True
        
        
        if square.row == square.column - 1:
            
            product = 1   
             
            for index in range(2,7):
                product *= self._data[index][index-1]
            
            if product in [2 ** 5, 3 ** 5]:
                return True
        
        
        if square.row + square.column == 7:
            
            product = 1   
             
            for index in range(1,7):
                product *= self._data[index][7-index]
            
            if product // self._data[1][6] in [2 ** 5, 3 ** 5] or product // self._data[6][1] in [2 ** 5, 3 ** 5]:
                return True
        
        
        if square.row + square.column == 8:
            
            product = 1   
             
            for index in range(2,7):
                product *= self._data[index][8 - index]
            
            if product in [2 ** 5, 3 ** 5]:
                return True
            
            
        return False
                            
    
    def getSquares(self, symbol = " "):
        '''
        Returns a list of the squares containing the given symbol.
        '''
        
        code = self._code[symbol]
        matching = []
        
        for row in range(1,7):
            for column in range(1,7):
                if self._data[row][column] == code:
                    matching.append( Square(row, column) )
                    
        return matching     
    
    
    def __str__(self):
        
        board = Texttable()
        
        for _row in range(1,7):
            
            symbolRow = []
            
            for _column in range(1,7):
                symbolRow.append(self._symbol[self._data[_row][_column]])
                
            board.add_row(symbolRow)
            
        return board.draw()


class RepoError(Exception):
    pass

            
            