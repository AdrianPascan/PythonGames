'''
Created on Feb 21, 2019

@author: Adrian
'''

class Square():
    '''
    
    '''


    def __init__(self, row, column):
        '''
        Constructor
        '''
        self._row = row
        self._column = column
    

    @property
    def row(self):
        return self._row
    
    @property
    def column(self):
        return self._column
    
    
    def __eq__(self, square):
        
        if self.row == square.row and self.column == square.column:
            return True
        
        return False
    
    
    def __str__(self):
        
        return "<" + str(self._row) + "," + str(self._column) + ">"
    
    
