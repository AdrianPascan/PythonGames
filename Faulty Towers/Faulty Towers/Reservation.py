'''
Created on Feb 20, 2019

@author: Adrian
'''

class Reservation():
    '''
    
    '''


    def __init__(self, ID, roomNumber, familyName, guestsNumber, arrival, departure):
        '''
        Constructor for Reservation class
        '''
        self.__ID = ID
        self.__roomNumber = roomNumber
        self.__familyName = familyName
        self.__guestsNumber = guestsNumber
        self.__arrival = arrival
        self.__departure = departure

    def get_id(self):
        return self.__ID


    def get_room_number(self):
        return self.__roomNumber


    def get_family_name(self):
        return self.__familyName


    def get_guests_number(self):
        return self.__guestsNumber


    def get_arrival(self):
        return self.__arrival


    def get_departure(self):
        return self.__departure


    def set_id(self, value):
        self.__ID = value


    def set_room_number(self, value):
        self.__roomNumber = value


    def set_family_name(self, value):
        self.__familyName = value


    def set_guests_number(self, value):
        self.__guestsNumber = value


    def set_arrival(self, value):
        self.__arrival = value


    def set_departure(self, value):
        self.__departure = value

    ID = property(get_id, set_id, None, None)
    roomNumber = property(get_room_number, set_room_number, None, None)
    familyName = property(get_family_name, set_family_name, None, None)
    guestsNumber = property(get_guests_number, set_guests_number, None, None)
    arrival = property(get_arrival, set_arrival, None, None)
    departure = property(get_departure, set_departure, None, None)
    
    
    def __str__ (self):
        
        string = "reservation " + str(self.ID) + ": "
        string += "room_number = " + str(self.roomNumber) + " ; "
        string += "family_name = " + str(self.familyName) + " ; "
        string += "number_of_guests = " + str(self.guestsNumber) + " ; "
        string += "arrival / departure = " + str(self.arrival.day) + "." + str(self.arrival.month) + "-" + \
                str(self.departure.day) + "." + str(self.departure.month)
        
        return string