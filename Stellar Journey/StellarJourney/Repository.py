'''
Created on Feb 22, 2019

@author: Adrian
'''
from texttable import Texttable
from Domain import Square
from random import choice
from Controller import GameOver

class Repository():
    '''
    
    '''
    

    def __init__(self):
        '''
        Constructor for Repository class
        '''
        
        self._data = []
        for row in range(9):
            self._data.append( [0] * 9 )
            
        self._rowSymbol = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
        self._rowCode = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
        
        self._symbol = {0: " ", 1: "*", 2: "B", 3: "E"}
        self._code = {" ": 0, "*": 1, "B": 2, "E": 3}
        
        self._placeStars()
        
        self._endeavour = self._placeEndeavour()
        
        self._blingons = self._placeBlingon(3)
    
        
    def grid(self, hide = True):
        
        grid = Texttable()
        
        header = []
        
        for column in range(9):
            header.append(column)
                    
        grid.header(header)
        
        for row in range(1,9):
            
            symbolRow = []
            symbolRow.append(self._rowSymbol[row])
            
            for column in range(1, 9):
                
                symbolRow.append(self._symbol[self._data[row][column]])
                
                if hide == True:
                    if self._data[row][column] == 2:
                        if not self._adjacent(self._endeavour, Square(self._rowSymbol[row], column)):
                            symbolRow[len(symbolRow) - 1] = " "
                
            grid.add_row(symbolRow)
            
        return grid.draw()            
    
    
    def getSquares(self, symbol = " "):
        
        code = self._code[symbol]
        
        matching = []
        for row in range(1,9):
            for column in range(1,9):
                if self._data[row][column] == code:
                    matching.append(Square(self._rowSymbol[row],column))
                    
        return matching
            
        
    def _adjacent(self, square, square2):
        
        if abs( self._rowCode[square.row] - self._rowCode[square2.row] ) <= 1 and \
            abs( square.column - square2.column ) <= 1 and not square == square2:
            return True
        
        return False
    
    
    def _overlap(self, square, square2):
         
        if square == square2:
            return True
         
        return False
    
    
    def _placeStars(self):
        
        options = self.getSquares()
        
        stars = []
        
        for star in range(10):
            
            current = choice(options)
            
            while True:
                
                index = 0
                
                while index < len(stars):
                    if self._overlap(current, stars[index]) and self._adjacent(current, stars[index]):
                        break
                    index += 1
                
                options.remove(current)
                
                if index == len(stars):
                    break
                else:
                    current = choice(options)
                    
            stars.append(current)
            self._data[self._rowCode[current.row]][current.column] = 1
            
    
    def _placeEndeavour(self):
        
        square = choice(self.getSquares())
        
        self._data[self._rowCode[square.row]][square.column] = 3
        
        return square
        
        
    def _placeBlingon(self, number):
        
        options = self.getSquares()
        blingons = []
        
        for blingon in range(number):
            
            current = choice(options)
            
            self._data[self._rowCode[current.row]][current.column] = 2
            
            blingons.append(current)
            
            options.remove(current)
            
        return blingons
    
    
    def _deleteBlingon(self):
        
        for blingon in self._blingons:
            self._data[self._rowCode[blingon.row]][blingon.column] = 0
    
            
    def sameLine(self, square):
        '''
        Checks if the square is on the same rank, file or diagonal relative to the Endeavour position.
        In: square, Square instance
        Out: True / False
        '''
        
        row = self._rowCode[self._endeavour.row]
        column = self._endeavour.column
        
        rowSquare = self._rowCode[square.row]
        columnSquare = square.column
        
        if row == rowSquare or column == columnSquare or \
                row - rowSquare == column - columnSquare or \
                (row + column == rowSquare + columnSquare):
            return True
        
        return False
    
    
    def isSymbol(self, square, symbol):
        '''
        Checks if there is the given symbol in the square.
        In: square - Square instance, symbol - string
        Out: True / False
        '''
        
        if self._data[self._rowCode[square.row]][square.column] == self._code[symbol]:
            return True
        
        return False
    
    
    def moveEndeavour(self, square):
        '''
        Moves Endeavour in the given Square
        In: square - Square instance
        '''
        
        self._data[self._rowCode[self._endeavour.row]][self._endeavour.column] = 0
        
        self._data[self._rowCode[square.row]][square.column] = 3
        
        self._endeavour = square
        
    
    def fire(self, square):
        
        if not self._adjacent(square, self._endeavour):
            raise RepoError("Square not adjacent.")
        
        if not self.isSymbol(square, "B"):
            raise RepoError("Not a Blingon ship here.")
        
        # self._data[self._rowCode[square.row]][square.column] = 0
        self._deleteBlingon()
        
        if len(self._blingons) == 1:
            raise GameOver("user")
        
        self._blingons = self._placeBlingon( len(self._blingons) - 1 )
        

class RepoError(Exception):
    
    def __str__(self, *args, **kwargs):
        return "Repository error - " + Exception.__str__(self, *args, **kwargs)
        

        