'''
Created on Feb 18, 2019

@author: Adrian
'''
import unittest
from Board import Board, BoardException
from Game import Game
from Square import Square


class Test(unittest.TestCase):


    def tearDown(self):
        del self


    def testBoard(self):
        
        self.board = Board()
        
        assert self.board._data == [[0,0,0],[0,0,0],[0,0,0]]
        
        self.board.store(Square(0,0), "X", True)
        assert self.board._data[0][0] == 1
        
        self.board.store(Square(0,1), "X", True)
        self.board.store(Square(0,2), "X", True)
        assert self.board.isWon(Square(0,1)) == True
        self.board.store(Square(1,1), "X", True)
        self.board.store(Square(2,2), "X", True)
        assert self.board.isWon(Square(2,2)) == True
        
        assert self.board.isWon(Square(2,1)) == False
        
        self.assertRaises(BoardException, self.board.store, Square(0,0), "X", True)
        
        emptySquares = self.board.getSquares()
        assert len(emptySquares) == 4
        assert emptySquares[3].row == 2 and emptySquares[3].column == 1
        
        
    def testGame(self):
        
        self.board = Board()
        self.game = Game(self.board)
        
        self.assertRaises(ValueError, self.game.round, "1", "5")
        
        self.game.round("0", "0")
        assert self.board._data[0][0] == 1
        xSquares = self.board.getSquares("X")
        assert len(xSquares) == 1
        assert xSquares[0].row == 0 
        assert xSquares[0].column == 0
        zeroSquares = self.board.getSquares("0")
        assert len(zeroSquares) == 1
        assert not (zeroSquares[0].row == 0 and zeroSquares[0].column == 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()