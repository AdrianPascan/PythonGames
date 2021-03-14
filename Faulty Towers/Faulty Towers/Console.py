'''
Created on Feb 20, 2019

@author: Adrian
'''
from Controller import ControllerError
from Repository import RepoError

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
        Starts the application.
        '''
        
        print("FAULTY TOWERS")
        print("1. Create reservation")
        print("2. Delete reservation")
        print("3. Available rooms")
        print("4. Monthly report")
        print("5. Day of week report")
        print("6. List reservations")
        print("0. Close application")
        
        while True:
            
            command = input(">> ")
            
            try:
                
                if command == "0":
                    print("Application closed.")
                    return
                
                elif command == "1":
                    self._createReservation()
                    
                elif command == "2":
                    self._deleteReservation()
                    
                elif command == "3":
                    self._availableRooms()
                    
                elif command == "4":
                    self._monthlyReport()
                    
                elif command == "5":
                    self._dayOfweekReport()
                
                elif command == "6":
                    self._printReservations()
                
                else:
                    print("Invalid command!")
            
            except (ValueError, ControllerError, RepoError) as error:
                print(str(error))
    
    
    def _createReservation(self):
        
        familyName = input("Family name: ")
        roomType = int(input("Room type: "))
        guestsNumber = int(input("Number of guests: "))
        arrival = input("Arrival: ")
        departure = input("Departure: ")
        
        print(self._controller.createReservation(roomType, familyName, guestsNumber, arrival, departure))
        
    
    def _deleteReservation(self):
        
        ID = input("ID: ")
        print(self._controller.deleteReservation(ID))
        
    
    def _availableRooms(self):
        
        time = input("Time interval: ").split("-")
        
        if len(time) != 2:
            raise ValueError("Invalid input data.")
        
        print(self._controller.availableRooms(time[0], time[1]))
        
    
    def _monthlyReport(self):
        
        print(self._controller.monthlyReport())
        
        
    def _dayOfweekReport(self):
        
        print(self._controller.dayOfWeekReport())
        
    
    def _printReservations(self):
        
        for reservation in self._controller.getReservations():
            print(str(reservation))
    
    