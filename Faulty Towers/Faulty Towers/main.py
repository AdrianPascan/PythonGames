'''
Created on Feb 20, 2019

@author: Adrian
'''

from Repository import Repository
from Controller import Controller
from Console import Console


if __name__ == '__main__':
    
    repository = Repository("rooms.txt", "reservations.txt")
    controller = Controller(repository)
    console = Console(controller)
    
    console.start()