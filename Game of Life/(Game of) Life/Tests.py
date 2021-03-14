'''
Created on Feb 19, 2019

@author: Adrian
'''
import unittest
from Repository import Repository, RepoError
from Controller import Controller


class Test(unittest.TestCase):


    def tearDown(self):
        del self


    def test2(self):
        
        self.repository = Repository()
        self.controller = Controller(self.repository)
        
        block = self.repository._getPattern("block")
        assert len(block) == 7
        assert block[0] == "block"
        assert block[1] == block[2] == "2"
        assert block[6] == "11"
        
        no = self.repository._getPattern("name")
        assert no == None
        
        self.repository.storePattern("block", 1, 1)
        assert self.repository._data[1][1] == self.repository._data[1][2] == self.repository._data[2][1] \
                == self.repository._data[2][2] == "X"
                
        self.assertRaises(RepoError, self.repository.storePattern, "blinker", 7, 6)
        
        self.assertRaises(RepoError, self.repository.storePattern, "blinker", 2, 2)
        
        self.assertRaises(ValueError, self.controller.addPattern, "name", 0, -1)
        
    
    def test3(self):
        
        self.repository = Repository()
        self.controller = Controller(self.repository)
        
        self.repository.storePattern("spaceship", 0, 0)
        
        assert 1 == self.repository._getNumberOfNeighbors(2, 0)
        assert 2 == self.repository._getNumberOfNeighbors(2, 2)
        assert 3 == self.repository._getNumberOfNeighbors(1, 0)
        assert 5 == self.repository._getNumberOfNeighbors(1, 1)
        
        self.repository.nextState()
                
        assert self.repository._data[1][0] == "X"
        assert self.repository._data[1][2] == "X"
        assert self.repository._data[2][1] == "X"
        assert self.repository._data[2][2] == "X"
        assert self.repository._data[3][1] == "X"
        
        assert self.repository._data[0][1] == " "
        assert self.repository._data[2][0] == " "
        
        self.assertRaises(ValueError, self.controller.tick, -1)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()