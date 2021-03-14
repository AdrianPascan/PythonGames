'''
Created on Feb 21, 2019

@author: Adrian
'''
from Controller import GameException
from Repository import RepoError
import pickle


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
        '''
        Starts the application.
        '''
        
        print("ORDER & CHAOS\n")
        
        try:
            
            while True:
                
                print(str(self._controller))
                
                command = input(">> ")
                
                if command == "stop":
                    print("Application closed.")
                    return
                
                elif command == "save":
                    with open("save.pickle", "wb") as file:
                        pickle.dump(self._controller, file)
                
                else:
                    
                    try:
                        
                        parameters = command.split(",")
                        
                        if len(parameters) == 3:
                            self._controller.round( int(parameters[0]), int(parameters[1]), parameters[2] )
                        else:
                            print("Invalid command.")
                    
                    except (ValueError, RepoError) as error:
                        print(str(error))
                
        except GameException as message:
            print(str(message))
            print(str(self._controller))
            return
    
    
        