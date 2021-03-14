'''
Created on Feb 22, 2019

@author: Adrian
'''
import unittest
from Repository import Repository
from Controller import Controller, GameOver
from Domain import Square


class Test(unittest.TestCase):


    def tearDown(self):
        del self


    def testWrap(self):
        
        self.repository = Repository()
        self.controller = Controller(self.repository)
        
        self.repository._data = []
        for row in range(9):
            self.repository._data.append([0] * 9)
            
        self.repository._data[5][5] = self.repository._code["E"]
        self.repository._endeavour = Square("E", 5)
        
        self.repository._data[3][3] = self.repository._code["*"]
        
        self.repository._data[5][1] = self.repository._code["B"]
                
        self.assertRaises(ValueError, self.controller.warp, Square("C", 1)) # not the same line
        
        self.assertRaises(ValueError, self.controller.warp, Square("C", 3)) # star
        
        self.assertRaises(GameOver, self.controller.warp, Square("E", 1)) # computer wins
        
        self.controller.warp, Square("C", 7)
        
        self.controller.warp, Square("G", 7)
        
        self.controller.warp, Square("E", 5)


if __name__ == "__main__":
    unittest.main()