'''
Created on Feb 19, 2019

@author: Adrian
'''
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
        Starts the application
        '''
        
        print(self._controller.grid)
        print("GAME OF LIFE")
        print("Available commands:")
        print("\t> place <name> <x,y> (place a pattern)")
        print("\t> tick [n] (advance the state with n generations, n=1 by default)")
        print("\t> load <filename>")
        print("\t> save <filename>")
        print("\t> stop (close the application)")
        
        while True:
            
            try:
                
                command = input(">> ").strip().split(" ")
                length = len(command)
                
                if command[0] == "stop" and length == 1:
                    print("Application closed.")
                    return
                
                elif command[0] == "place" and length == 3 and len(command[2].split(",")) == 2:
                    name = command[1]
                    x = int(command[2].split(",")[0])
                    y = int(command[2].split(",")[1])
                    self._controller.addPattern(name, x, y)
                
                elif command[0] == "tick" and length <= 2:
                    if length == 1:
                        self._controller.tick()
                    else:
                        self._controller.tick(int(command[1]))
                
                elif command[0] == "load" and length == 2:
                    try:
                        with open(command[1], "rb") as file:
                            self._controller = pickle.load(file)
                    except Exception as error:
                        print("An error occured - " + str(error))
                
                elif command[0] == "save" and length == 2:
                    try:
                        with open(command[1], "wb") as file:
                            pickle.dump(self._controller, file)
                    except Exception as error:
                        print("An error occured - " + str(error))
                
                else:
                    print("Invalid command.")
            
            except (ValueError, RepoError) as error:
                print(str(error))
                
            print(self._controller.grid)
    
    
    