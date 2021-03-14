'''
Created on Feb 20, 2019

@author: Adrian
'''
import unittest
from Repository import Repository, RepoError
from Controller import Controller, ControllerError
from random import choice


class Test(unittest.TestCase):


    def setUp(self):
        self.repository = Repository("Test_rooms.txt")
        self.controller = Controller(self.repository)


    def tearDown(self):
        del self


    def test2(self):
        
        self.controller.createReservation(4, "Popescu", 3, "25.05", "26.05")
        
        reservation = list(self.repository._reservations.values())[0]
        assert int(reservation.ID) in range(0, 10000)
        assert reservation.roomNumber in [5,6]
        assert reservation.familyName == "Popescu"
        assert reservation.guestsNumber == 3
        assert reservation.arrival.day == 25
        assert reservation.arrival.month == 5
        assert reservation.departure.day == 26
        assert reservation.departure.month == 5
        
        self.controller.createReservation(4, "Popescu", 3, "25.05", "26.05")
        self.assertRaises(RepoError, self.controller.createReservation, 4, "Popescu", 3, "24.05", "26.05")
        
        self.assertRaises(ControllerError, self.controller.createReservation, 5, "Popescu", 3, "25.05", "26.05")
        self.assertRaises(ControllerError, self.controller.createReservation, 0, "Popescu", 3, "25.05", "26.05")
        self.assertRaises(ControllerError, self.controller.createReservation, 4, "Popescu", 0, "25.05", "26.05")
        self.assertRaises(ControllerError, self.controller.createReservation, 4, "Popescu", 5, "25.05", "26.05")
        self.assertRaises(ControllerError, self.controller.createReservation, 4, "", 3, "25-05", "26-05")
        self.assertRaises(ControllerError, self.controller.createReservation, 4, "Popescu", 3, "26.05", "25.05")
        
    
    def test3(self):
        
        self.controller.createReservation(4, "Popescu", 3, "25.05", "26.05")
        self.controller.createReservation(2, "Popescu", 2, "25.05", "26.05")
        self.controller.createReservation(1, "Popescu", 1, "25.05", "26.05")
        ID = choice(list(self.repository._reservations.keys()))
        self.controller.deleteReservation(ID)
        assert ID not in self.repository._reservations.keys()


if __name__ == "__main__":
    unittest.main()