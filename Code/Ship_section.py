
#This Defines a section of the ship
#This will be an object that is stored within a list of objects,
#Which combined together will be a ship
#Adding a next DA so I can implement this like a linked list
class ship_section:
    
    __is_hit = False
    __next = None
    
    #This will the same name as the ship that makes it
    __part_of = ""
    
    #Every ship part generated will be defaulted as not hit
    #This value will only change once the game starts running
    #So I'm just going to hard set it to False
    def __init__(self, ship_name):
        self.set_is_hit(False)
        self.set_next(None)
        self.set_part_of(ship_name)
    
    #Getters
    def get_is_hit(self):
        return self.__is_hit
    
    def get_next(self):
        return self.__next
    
    def get_part_of(self):
        return self.__part_of
    
    #Setters
    def set_is_hit(self, bool_value):
        self.__is_hit = bool_value
        
    def set_next(self, next):
        self.__next = next
        
    def set_part_of(self, po):
        self.__part_of = po
        
    #To String
    def __str__(self):
        return f"\nPart of: {self.get_part_of()}\nHit?: {self.get_is_hit()}"