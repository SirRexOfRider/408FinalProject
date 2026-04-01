
#This Defines a section of the ship
#This will be an object that is stored within a list of objects,
#Which combined together will be a ship
class ship_section:
    
    __is_hit = False
    
    #Every ship part generated will be defaulted as not hit
    #This value will only change once the game starts running
    #So I'm just going to hard set it to False
    def __init__(self):
        self.__is_hit = False
    
    #Getters
    def get_is_hit(self):
        return self.__is_hit
    
    #Setters
    def set_is_hit(self, bool_value):
        self.__is_hit = bool_value
        
    #ToString
    def __str__(self):
        print(f"Is current section hit?: {self.get_is_hit}")