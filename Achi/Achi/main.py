'''
Created on Feb 18, 2019

@author: Adrian
'''
from Board import Board
from Game import Game
from Console import Console
import pickle

if __name__ == '__main__':
    
    print("1. Start a new game \n2. Load an existing game")
        
    while True:
        
        command = input(">> ")
        
        if command == "1":
            board = Board()
            game = Game(board)
            break
            
        elif command == "2":
            with open("board.pickle", "rb") as file:
                board = pickle.load(file)
            with open("game.pickle", "rb") as file:
                game = pickle.load(file)
            break
        
        else:
            print("Invalid command!")
    
    console = Console(game)
    
    console.start()