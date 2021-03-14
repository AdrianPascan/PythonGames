'''
Created on Feb 20, 2019

@author: Adrian
'''
from random import randint, choice
import datetime
from Reservation import Reservation
from calendar import monthrange, month_name, day_name
from datetime import timedelta

class Repository():
    '''
    
    '''


    def __init__(self, roomsFile, reservationsFile = None):
        '''
        Constructor for Repository class
        '''
        self._rooms = self._loadRooms(roomsFile)
        
        if reservationsFile == None:
            self._reservations = {}
        else:
            self._reservations = self._loadReservations(reservationsFile)
            
        self._saveFile = reservationsFile
    
    
    def createReservation(self, roomType, reservation):
        '''
        Creates a reservation.
        '''
        matching = self._rooms[roomType][:]
        
        for current in self._reservations.values():
            if current.roomNumber in matching:
                if self._datesOverlap(reservation, current):
                    matching.remove(current.roomNumber)
        
        if matching == []: 
            raise RepoError("No available rooms of this type.")
        
        reservation.roomNumber = choice(matching)
        
        ID = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
        while ID in self._reservations.keys():
            ID = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
        reservation.ID = ID
        
        self._reservations[ID] = reservation
        
        self._saveReservations(self._saveFile)
        
        return str(reservation)
             
        
    def _datesOverlap(self, reservation1, reservation2):
        '''
        Checks if the time interval of reservation1 intersects the one of reservation2.
        '''
        
        if (reservation1.arrival >= reservation2.arrival and reservation1.arrival < reservation2.departure) \
            or (reservation1.departure <= reservation2.departure and reservation1.departure > reservation2.arrival) \
            or (reservation1.arrival < reservation2.arrival and reservation1.departure > reservation2.departure):
            return True
        
        return False
    
    
    def deleteReservation(self, ID):
        '''
        Removes the reservation with the given ID.
        '''
        
        if ID not in self._reservations.keys():
            raise RepoError("Reservation with ID " + str(ID) + " does not exist.")

        del self._reservations[ID]
        
        self._saveReservations(self._saveFile)

        return "Reservation with ID " + str(ID) + " deleted."
    
    
    def availableRooms(self, arrival, departure):
        '''
        Returns a list of the available rooms for the given interval.
        '''
        
        matching = []
        matching.extend(self._rooms[1])
        matching.extend(self._rooms[2])
        matching.extend(self._rooms[4])
        
        supposed = Reservation(None, None, None, None, arrival, departure)
        
        for reservation in self._reservations.values():
            if reservation.roomNumber in matching:
                if self._datesOverlap(reservation, supposed):
                    matching.remove(reservation.roomNumber)
        
        if matching == []: 
            raise RepoError("No available rooms of this type.")
        
        matching.sort()
        
        return matching
    
    
    def monthlyReport(self):
        '''
        Returns a list of the months sorted in descending order by the number of the reservation days.
        '''
        
        monthDays = []
        
        for month in range(1,13):
            
            monthDays.append([month, 0])
            
            start = datetime.datetime (year = 2018, month = month, day = 1)
            end = datetime.datetime(year = 2018, month = month, day = monthrange(2018, month)[1])
            supposed = Reservation(None, None, None, None, start, end)
            
            for reservation in self._reservations.values():
                if self._datesOverlap(reservation, supposed):
                    
                    relativeStart = reservation.arrival
                    relativeEnd = reservation.departure
                    
                    if relativeStart < start:
                        relativeStart = start
                    
                    if relativeEnd > end:
                        relativeEnd = end
                        
                    monthDays[month-1][1] += (relativeEnd-relativeStart).days
                    
        monthDays.sort(key= lambda element: element[1], reverse=True)
        
        results = []
        
        for element in monthDays:
            results.append( str(month_name[element[0]]) + ": " + str(element[1]) )
            
        return results
    
    
    def dayOfWeekReport(self):
        '''
        Returns a list of the days of the week sorted in descending order by the total number of reserved rooms for that day.
        '''
        
        weekDays = [ [0,0], [1,0], [2,0], [3,0], [4,0], [5,0], [6,0] ]
        
        for reservation in self._reservations.values():
            
            current = reservation.arrival + timedelta(days=0)
            
            while current < reservation.departure:
                
                weekDays[current.weekday()][1] += 1
                current += timedelta(days=1)
        
        weekDays.sort(key= lambda element: element[1], reverse=True)
        
        return [ ( str(day_name[element[0]]) + ": " + str(element[1]) ) for element in weekDays ]
    
    
    def getReservations(self):
        '''
        Returns a list of the stored reservations.
        '''
        return self._reservations.values()
    
    
    def _loadRooms(self, fileName):
        '''
        Loads from '<fileName>' the numbers of the rooms and their type
        '''
        
        with open(fileName, "r") as file:
            data = file.read().strip("\n").split("\n")
        
        rooms = {1:[], 2:[], 4:[]}  
        for room in data:
            current = room.strip().split(";")
            _number = int(current[0])
            _type = int(current[1])
            rooms[_type].append(_number)
            
        for _type in [1,2,4]:
            if len(rooms[_type]) < 2:
                raise RepoError("There are less than two rooms of this type: " + str(type))
        
        return rooms
    
    
    def _loadReservations(self, fileName):
        '''
        Loads from '<fileName>' the reservations
        '''
        
        with open(fileName, "r") as file:
            data = file.read().strip("\n").split("\n")
    
        reservations = {}
        for current in data:
            parameters = current.split(",")
            ID = parameters[0].strip(" ")
            roomNumber = int(parameters[1].strip(" "))
            familyName = parameters[2].strip(" ")
            guestsNumber = int(parameters[3].strip(" "))
            arrival = datetime.datetime.strptime(parameters[4].strip(" ") + ".2018", "%d.%m.%Y")
            departure = datetime.datetime.strptime(parameters[5].strip(" ") + ".2018", "%d.%m.%Y")
            reservations[ID] = Reservation(ID, roomNumber, familyName, guestsNumber, arrival, departure)
                    
        return reservations
    
    
    def _saveReservations(self, fileName):
        '''
        Stores the reservations in '<fileName>'.
        '''
        
        if fileName != None:
            
            with open(fileName, "w") as file:
                
                for reservation in self._reservations.values():
                                                    
                    file.write(reservation.ID + ", " + str(reservation.roomNumber) + ", " + \
                               reservation.familyName + ", " + str(reservation.guestsNumber) + ", " + \
                               str(reservation.arrival.day) + "." + str(reservation.arrival.month) + "," + \
                               str(reservation.departure.day) + "." + str(reservation.departure.month) + "\n")
            
            
class RepoError(Exception):
    pass
