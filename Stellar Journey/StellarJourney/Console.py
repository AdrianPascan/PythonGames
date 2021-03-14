'''
Created on Feb 22, 2019

@author: Adrian
'''
from Controller import GameOver
from Repository import RepoError
from Domain import Square

class Console():
    '''
    Console-based UI class
    '''


    def __init__(self, controller):
        '''
        Constructor for Console class
        '''
        self._controller = controller
    
    
    def start(self):
        
        print(self._controller.getGrid())
        
        try:
            
            while True:
                                
                command = input(">> ").strip(" ")
                
                if command == "cheat":
                    
                    print(self._controller.cheat())
                
                elif command == "stop":
                    
                    print("Application closed.")
                    return
                
                else:
                    
                    try:
                        
                        parameters = command.split(" ")
                        
                        if len(parameters) == 2 and parameters[0] == "warp" and len(parameters[1]) == 2:
                            
                            self._controller.warp( Square(parameters[1][0], int(parameters[1][1])) )
                        
                        elif len(parameters) == 2 and parameters[0] == "fire" and len(parameters[1]) == 2:
                            
                            self._controller.fire( Square(parameters[1][0], int(parameters[1][1])) )
                        
                        else:
                            print("Invalid command.")
                            
                        print(self._controller.getGrid())
                    
                    except (ValueError, RepoError) as error:
                        print(str(error))
        
        except GameOver as message:
            print(self._controller.cheat())
            print(str(message))
    