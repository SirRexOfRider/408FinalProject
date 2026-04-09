from Player import player

class bot(player):
    
    #DA
    __search_space = []
    
    #Innit
    def __init__(self):
        super().__init__()
        #self.set_search_space()
    
    #Helpers
    def generate_search_space_static(self):
        """Generate a seach space for the bot. The search space will make the bot search diagonally"""
        temp_space = []
        
        #For all quadrants (10 x 10)
        for x in range(10):
            for y in range(10):
                
                #Add them to the search space
                temp_space.append(f"{str(self.get_my_ship_board().get_column_markers()[x])}" + f"{str(self.get_my_ship_board().get_row_markers()[y])}")
                
        print(temp_space)
    
    #Getters
    def get_search_space(self):
        return self.__search_space
    
    #Setters
    def set_search_space(self, ss):
        self.__search_space = ss