'''
Created on Feb 22, 2019

@author: Adrian
'''
from Repository import Repository
from Controller import Controller
from Console import Console


if __name__ == '__main__':
    
    repository = Repository()
    controller = Controller(repository)
    console = Console(controller)
    
    console.start()