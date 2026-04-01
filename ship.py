#Import sections of the ship
import ship_section


#This will be made into ship objects that can be used by the player and code/AI/Bot
class Ship:
    
    #DA
    __length = 0
    __name = ""
    __is_sunk = False
    
    #This will be filled with section ship objects from a helper function
    __ship_sections = []
    
    #Init
    #Some varaibles will be hard set because it would be redundant to bring them into the init call
    def __init__(self, name, length):
        
        self.set_name(name)
        self.set_length(length)
        
        
    #Helpers
    def build_ship(name, length):
        
        #List that will be set to the ship_sections
        ship_sections = []
        
        for x in range(length):
            ship_sections.append(ship_section)
    
    
    #Getters
    def get_length(self):
        return self.__length
    
    def get_name(self):
        return self.__name
    
    def get_is_sunk(self):
        return self.__is_sunk
    
    def get_ship_sections(self):
        return self.__ship_sections
    
    #Setters
    def set_length(self, l):
        self.__length = l
        
    def set_name(self, n):
        self.__name = n
        
    def set_is_sunk(self, is_sunk):
        self.__is_sunk = is_sunk
        
    def set_ship_sections(self, ship_sections):
        self.__ship_sections = ship_sections
    
    
    
    
