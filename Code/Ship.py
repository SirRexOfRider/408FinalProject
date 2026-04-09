#Import sections of the ship
from Ship_section import ship_section


#This will be made into ship objects that can be used by the player and code/AI/Bot
class ship:
    
    #Data Attributes
    __length = -1
    __name = "error"
    __is_sunk = None
    
    #Header/tail values
    __bow = None
    __stern = None
    
    #This will be filled with section ship objects from a helper function
    #I know this is kinda redundant if I'm implementing this like a linked list, BUT this should allow me
    #iterate through a ship to check it's sections without having to keep track of all of the indexes it resides at
    #Since I could just go to the next segment using .get_next()
    __ship_sections = []
    
    #Init
    def __init__(self, name = "", length = 0):
        self.set_name(name)
        self.set_length(length)
        self.set_is_sunk(False)
        self.build_ship()
          
    #Helpers
    #============================= BUILD SHIP OBJECT ========================================================
    def build_ship(self):
        """Build Ship object using pre-defined name and length when Initializing object"""
        
        #List that will be set to the ship_sections
        ship_sections = []
        
        #For as many ship parts that are needed
        for x in range(self.get_length()):
            #Make new parts and add them to the ship list
            ship_sections.append(ship_section(self.get_name()))
            
        #Set the beginning of the ship as the bow and the end as the stern
        self.set_bow(ship_sections[0])
        
        self.set_stern(ship_sections[self.get_length() - 1])
        
        #After building, link sections together using the next DA in ship sections
        current_index = 0
        while (current_index < self.get_length() - 1):
            ship_sections[current_index].set_next(ship_sections[current_index + 1])
            current_index+=1
            
        #After building and setting ship sections, set ship
        self.set_ship_sections(ship_sections)
            
    #============================== HIT SHIP SECTION ======================================================
    def hit_ship_section(self, index):
        """Change the value of a ship section to be True (hit)"""
        modified_ship = self.get_ship_sections()
        modified_ship[index].set_is_hit(True)
        
        #After ship is hit, do a check to see if it has been sunk
        self.check_if_sunk()
        
        self.set_ship_sections(modified_ship)
    
    
    #========================== CHECK IF SUNK =================================================================
    def check_if_sunk(self):
        """Check to see if all sections of the ship are hit"""
        #Sentinel value
        sunk = True
        
        #Get head of ship section (bow)
        current_section = self.get_bow()
        
        #This is where I'm implementing the next DA so I can say I implemented a linked list.. of sorts...
        while (current_section != None):
            
            #If the section hasn't been hit yet, then the whole ship hasn't sunk yet either
            if (current_section.get_is_hit() != True):
                sunk = False
                
            #Go to the next part of the ship
            current_section = current_section.get_next()
                
        #Set sunk boolean value
        self.set_is_sunk(sunk)
        
    #========================= FIND DISTANCE TO STERN ==================================================
    def find_distance_to_stern(self, ship_segment):
        """Find the amount of steps needed to hit the stern of the ship given a ship segment"""
        
        #Distance value that will be returned
        distance = 0
        
        #Current segment
        current_segment = ship_segment
        
        #While we haven't gone past the tail
        while (current_segment != None):
            distance += 1
            current_segment = current_segment.get_next()
            
        return distance
         
    #Getters
    def get_length(self):
        return self.__length
    
    def get_name(self):
        return self.__name
    
    def get_is_sunk(self):
        return self.__is_sunk
    
    def get_ship_sections(self):
        return self.__ship_sections
    
    def get_bow(self):
        return self.__bow
    
    def get_stern(self):
        return self.__stern
    
    #Setters
    def set_length(self, l):
        self.__length = l
        
    def set_name(self, n):
        self.__name = n
        
    def set_is_sunk(self, is_sunk):
        self.__is_sunk = is_sunk
        
    def set_ship_sections(self, ship_sections):
        self.__ship_sections = ship_sections
        
    def set_bow(self, b):
        self.__bow = b
        
    def set_stern(self, s):
        self.__stern = s
    
    #To string
    def __str__(self):
        temp = ""
        temp += f"\n#--- SHIP NAME: {self.get_name()}\n#------ Length: {self.get_length()}\n#------- Sunk?: {self.get_is_sunk()}\n========================\n"
        
        temp += "BOW"
        
        #For the length of the ship
        for x in range(self.get_length()):
            temp += f" -> |S{x}: {self.get_ship_sections()[x].get_is_hit()}|"
            
        temp += " <- Stern"
            
        return temp
    
