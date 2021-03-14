'''
Created on Feb 21, 2019

@author: Adrian
'''
import unittest
from Repository import Repository
from Controller import Controller
from Domain import Square
  
class Test(unittest.TestCase):
 
 
    def tearDown(self):
        del self
 
 
    def test4(self):
        
        self.repository = Repository()
        self.controller = Controller(self.repository)
        
        self.repository.store(Square(1,1), "X")
        self.repository.store(Square(2,2), "X")
        self.repository.store(Square(3,3), "X")
        self.repository.store(Square(4,4), "X")
        self.repository.store(Square(5,5), "X")
        self.repository.store(Square(6,6), "O")
        
        assert self.repository.isWon(Square(3,3)) == True
        
        self.repository.store(Square(2,6), "O")
        self.repository.store(Square(3,5), "O")
        self.repository.store(Square(4,4), "O")
        self.repository.store(Square(5,3), "O")
        self.repository.store(Square(6,2), "O")
        
        assert self.repository.isWon(Square(2,6)) == True
        
        self.repository = Repository()
        self.controller = Controller(self.repository)
        
        self.repository.store(Square(4,1), "X")
        self.repository.store(Square(4,3), "X")
        self.repository.store(Square(4,5), "X")
        
        self.controller.round(4, 4, "X")
        
        assert self.repository._data[4][2] == self.repository._code["O"]
 
 
if __name__ == "__main__":
    unittest.main()