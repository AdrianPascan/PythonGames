'''
Created on Feb 19, 2019

@author: Adrian
'''
import texttable

class Repository():
    '''
    
    '''


    def __init__(self):
        '''
        Constructor for Repository class
        '''
        self._data = []
        for row in range(8):
            self._data.append( [" "] * 8 )
    
    
    def storePattern(self, name, x, y):
        '''
        Stores the pattern on the grid relative to the coordinates of the upper-left corner <x,y>.
        In: name, x, y - strings
        Exceptions: RepoError
        '''
        
        pattern = self._getPattern(name)
        
        if pattern == None:
            raise RepoError("Pattern does not exist.")
        
        self._validatePattern(pattern, x, y)
        
        for liveCell in pattern[3:]:
            self._data[x + int(liveCell[0])][y + int(liveCell[1])] = "X"
    
    
    def _getPattern(self, name):
        '''
        Gets the pattern with the given name from the text file where they are stored and returns it as a list.
        '''
        
        with open("patterns.txt", "r") as file:
            patterns = file.read().split("\n")
                    
        for pattern in patterns:
            if pattern.split(";")[0] == name:
                return pattern.split(";")
            
        return None
    
    
    def _validatePattern(self, pattern, x, y):
        '''
        Validates the current pattern so that it does not go outside the board or overlaps already existing live cells.
        '''
        
        if x + int(pattern[1]) -1 >= 8 or y + int(pattern[2]) -1 >= 8: 
            raise RepoError("Live cells of the pattern go outside the board.")
        
        for liveCell in pattern[3:]:
            if self._data[x + int(liveCell[0])][y + int(liveCell[1])] == "X":
                raise RepoError("Live cells of the pattern overlap already existing ones.")
                
    
    def __str__(self):
        '''
        Returns the current grid as a string.
        '''
        grid = texttable.Texttable()
        
        for row in self._data:
            grid.add_row(row)
            
        return grid.draw()
    
    
    def nextState(self):
        '''
        Advances the state.
        '''
        
        toDelete = []
        toAdd = []
        
        for row in range(8):
            for column in range(8):
                
                number = self._getNumberOfNeighbors(row, column)
                
                if self._data[row][column] == "X":
                    if number not in [2,3]:
                        toDelete.append((row,column))
                
                else:
                    if number == 3:
                        toAdd.append((row,column))
                        
        for liveCell in toDelete:
            self._data[liveCell[0]][liveCell[1]] = " "
            
        for deadCell in toAdd:
            self._data[deadCell[0]][deadCell[1]] = "X"
            
    
    def _getNumberOfNeighbors(self, x, y):
        '''
        Returns the number of live cells which are neighbors to the cell having coordinates x,y.
        '''
        
        number = 0
        
        row = [0]
        column = [0]
        
        if x < 7:
            row.append(1)
        if x > 0:
            row.append(-1)
        
        if y < 7:
            column.append(1)
        if y > 0:
            column.append(-1)
            
        for _row in row:
            for _column in column:
                if self._data[x+_row][y+_column] == "X":
                    number += 1
                    
        if self._data[x][y] == "X":
            number -= 1
                    
        return number
    
    
class RepoError(Exception):
    pass
