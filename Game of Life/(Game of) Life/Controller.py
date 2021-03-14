'''
Created on Feb 19, 2019

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
    
    
    def addPattern(self, name, x, y):
        '''
        Adds the pattern on the grid relative to the coordinates of the upper-left corner <x,y>.
        In: name - string; x, y - integers
        Exceptions: ValueError, RepositoryError
        '''
        
        if not (x in range(8)) or not (y in range(8)):
            raise ValueError("Invalid indexes for upper-left corner.")
        
        self._repository.storePattern(name, x, y)
        
        
    def tick(self, n = 1):
        '''
        Advances the state with n (=1, by default) generations.
        '''
        
        if n < 1:
            raise ValueError("n must be a strictly positive integer.")
        
        for next in range(n):
            self._repository.nextState()
        
    
    @property
    def grid(self):
        return str(self._repository)
    
        