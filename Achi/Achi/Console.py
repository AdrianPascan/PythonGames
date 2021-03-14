'''
Created on Feb 18, 2019

@author: Adrian
'''
from Game import GameException
from Board import BoardException
import pickle

class Console():
    '''
    Console-based UI
    '''


    def __init__(self, game):
        '''
        Constructor for Console class
        '''
        self._game = game     
        
        
    def start(self): 
        '''
        Starts the application.
        '''  
        
        try:
            while True:
                
                try:
                    
                    print(self._game.board)
                    print(self._game.message)
                    
                    command = input("\t>> ").strip()
                    
                    if command == "save":
                        self._game.save()
                            
                    elif len(command) != 2:
                        print("Invalid command!")
                        
                    else:
                        self._game.round(command[0], command[1])
                        
                except (ValueError, BoardException) as error:
                    print(str(error))
        
        except GameException as message:
            print(str(message))
            print(self._game.board)
            
            
            
            
            
            
        