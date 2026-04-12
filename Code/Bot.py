from Player import player

class bot(player):
    
    #DA
    __search_space = []
    __previous_misses = []
    
    #Innit
    def __init__(self):
        super().__init__()
        
    
    #Helpers
    def generate_search_space_static(self):
        """Generate a seach space for the bot."""
        temp_space = []
        
        count = 0
        column_counter = 0
        
        #For the first half of quadrants (5 x 10)
        for x in range(5):
            for y in range(10):
                #Add them to the search space
                temp_space.append(f"{str(self.get_my_ship_board().get_column_markers()[(x + y + column_counter) % 10])}" + f"{str(self.get_my_ship_board().get_row_markers()[(x + y - count) % 10])}")
                
            count += 1
            column_counter += 1
            
        count = 0
        column_counter = 1

        #For the second half of the quadrants (5 x 10)
        for x in range(5):
            for y in range(10):
                #Add them to the search space
                temp_space.append(f"{str(self.get_my_ship_board().get_column_markers()[(x + y + column_counter) % 10])}" + f"{str(self.get_my_ship_board().get_row_markers()[(x + y - count) % 10])}")
                
            count += 1
            column_counter += 1
                
        #print(temp_space)
        self.set_search_space(temp_space)
    
    #Getters
    def get_search_space(self):
        return self.__search_space
    
    def get_previous_misses(self):
        return self.__previous_misses
    
    #Setters
    def set_search_space(self, ss):
        self.__search_space = ss
        
    def set_previous_misses(self, pm):
        self.__previous_misses = pm