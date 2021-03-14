'''
Created on Feb 18, 2019

@author: Adrian
'''

class Square():
    '''
    
    '''


    def __init__(self, row, column):
        '''
        Constructor for Square class
        '''
        self._row = row
        self._column = column
        
        
    @property
    def row(self):
        return self._row
    
    
    @property
    def column(self):
        return self._column
    
    
    def __str__(self):
        return "<" + str(self._row) + "," + str(self._column) + ">"
        