'''
Created on Feb 20, 2019

@author: Adrian
'''
from Reservation import Reservation
import datetime

class Controller():
    '''
    
    '''


    def __init__(self, repository):
        '''
        Constructor for Controller class
        '''
        self._repository = repository
        
    
    def createReservation(self, roomType, familyName, guestsNumber, arrival, departure):
        '''
        Validates and creates a reservation.
        '''
        
        reservation = Reservation(None, None, familyName, guestsNumber, arrival, departure)
        self._validateReservation(roomType, reservation)
        
        return self._repository.createReservation(roomType, reservation)
        
    
    def _validateReservation(self, roomType, reservation):
        '''
        Validates the current reservation.
        '''
        
        errors = ""
        
        if roomType not in [1,2,4]:
            errors += "Room types are: 1,2,4.\n"
            
        if reservation.familyName == "":
            errors += "Family name cannot be empty.\n"
            
        if reservation.guestsNumber not in [1,2,3,4]:
            errors += "Number of guests must be in range [1,4].\n"
            
        if roomType < reservation.guestsNumber:
            errors += "Number of guests greater than the room type.\n"
            
        try:
            (reservation.arrival, reservation.departure) = self._validateTimeInterval(reservation.arrival, reservation.departure)
        except ValueError as message:
            errors += str(message) + "\n"
        
        if not errors == "":
            raise ControllerError(errors)
        
        
    def _validateTimeInterval(self, arrival, departure):
        '''
        Validates a time interval corresponding to an accomodation.
        '''
        
        try:
            
            arrival = datetime.datetime.strptime(arrival + ".2018", "%d.%m.%Y")
            departure = datetime.datetime.strptime(departure + ".2018", "%d.%m.%Y")
            if arrival >= departure:
                raise ValueError
            return (arrival, departure)
            
        except ValueError:
            raise ValueError("Invalid arrival or/and departure date.")
        
        
    def deleteReservation(self, ID):
        '''
        Removes the reservation with the given ID.
        '''
        
        return self._repository.deleteReservation(ID)
    
    
    def availableRooms(self, arrival, departure):
        '''
        Returns a list of the available rooms for the given interval.
        '''
        
        (arrival, departure) = self._validateTimeInterval(arrival, departure)
        
        return self._repository.availableRooms(arrival, departure)
        
    
    def monthlyReport(self):
        '''
        Returns a list of the months sorted in descending order by the number of the reservation days.
        '''
        
        return self._repository.monthlyReport()
    
    
    def dayOfWeekReport(self):
        '''
        Returns a list of the days of the week sorted in descending order by the total number of reserved rooms for that day.
        '''
        
        return self._repository.dayOfWeekReport()
    
    
    def getReservations(self):
        '''
        Returns a list of the stored reservations.
        '''
        return self._repository.getReservations()
    

class ControllerError(Exception):
    pass 
    
    
