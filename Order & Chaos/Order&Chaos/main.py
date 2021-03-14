'''
Created on Feb 21, 2019

@author: Adrian
'''
from Repository import Repository
from Controller import Controller
from Console import Console
import pickle


if __name__ == '__main__':
    
    print("1. Start a new game")
    print("2. Load an existing game")
    
    while True:
        
        command = input(">> ")
        
        if command == "1":
            repository = Repository()
            controller = Controller(repository)
            break
            
        elif command == "2":
            with open("save.pickle", "rb") as file:
                controller = pickle.load(file)
            break
                
        else:
            print("Invalid command.")
        
    console = Console(controller)
    
    console.start()