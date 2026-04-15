from Player import player

class bot(player):
    
    #DA
    __search_space = []
    __hunt_queue = []
    
    #Previous guesses list
    __previous_guesses = []
    
    __is_hunting = False
    
    #Innit
    def __init__(self):
        super().__init__()
        self.set_search_space([])
        self.set_hunt_queue([])
        self.set_previous_guesses([])
        self.set_is_hunting(False)
        
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
        
    def update_hunt_queue(self, shot_determination):
        """Update the hunting queue based on the shot determination"""
        
        #If the last shot missed a ship
        #If I had more time, this would be where I would implement something to track previous guess determinations
        #So the bot would be able to determine if a ship is vertical or horizontal based on the first couple of guesses
        #Maybe if I have time I'll come back to implement this, who knows :/
        
        if (shot_determination == 0):
            pass
            
        #Else if the last shot hit a ship
        elif (shot_determination == 3):
            
            #Grab the previous guess
            previous_guess = self.get_previous_guesses()[-1]
            
            #Get the surrounding quadrants of the previous guess and try to add them to the hunting queue
            #Add quadrants to hunt queue [L - T - R - B]
            left = self.get_my_ship_board().convert_input(previous_guess)
            top = self.get_my_ship_board().convert_input(previous_guess)
            right = self.get_my_ship_board().convert_input(previous_guess)
            bottom = self.get_my_ship_board().convert_input(previous_guess)

            #Modify the coordinates
            left[1] = left[1] - 1
            top[0] = top[0] - 1
            right[1] = right[1] + 1
            bottom[0] = bottom[0] + 1
            
            # print(self.get_my_ship_board().convert_input(previous_guess))
            # print(left)
            # print(top)
            # print(right)
            # print(bottom)
            
            #Temporary list to collect the valid quadrants
            temp_queue = self.get_hunt_queue()
            
            # == Verify to make sure the coordinates aren't out of bounds of the board or already haven't been guessed ==
            #Warning: Because I confused myself with the indexing of the board, this is technically backwards so...
            
            #If the left quadrant is valid and hasn't been searched yet AND not currently in the queue
            left_quadrant = f"{str(self.get_my_ship_board().get_column_markers()[left[1]])}" + f"{str(self.get_my_ship_board().get_row_markers()[left[0]])}"
            if ((left[1] >= 0 ) and (self.get_my_guess_board().get_grid()[left[0]][left[1]] == None) and (left_quadrant not in self.get_hunt_queue())):
                temp_queue.append(left_quadrant)
                
                
            #If the top quadrant is valid and hasn't been searched yet AND not currently in the queue
            top_quadrant = f"{str(self.get_my_ship_board().get_column_markers()[top[1]])}" + f"{str(self.get_my_ship_board().get_row_markers()[top[0]])}"
            if ((top[0] >= 0) and (self.get_my_guess_board().get_grid()[top[0]][top[1]] == None) and (top_quadrant not in self.get_hunt_queue())):
                temp_queue.append(top_quadrant)
                
            #If the right quadrant is valid and hasn't been searched yet AND not currently in the queue
            right_quadrant = f"{str(self.get_my_ship_board().get_column_markers()[right[1]])}" + f"{str(self.get_my_ship_board().get_row_markers()[right[0]])}"
            if ((right[1] <= 9) and (self.get_my_guess_board().get_grid()[right[0]][right[1]] == None) and (right_quadrant not in self.get_hunt_queue())):
                temp_queue.append(right_quadrant)
                
            #If the bottom quadrant is valid and hasn't been searched yet AND not currently in the queue
            bottom_quadrant = f"{str(self.get_my_ship_board().get_column_markers()[bottom[1]])}" + f"{str(self.get_my_ship_board().get_row_markers()[bottom[0]])}"
            if ((bottom[0] <= 9) and (self.get_my_guess_board().get_grid()[bottom[0]][bottom[1]] == None) and (bottom_quadrant not in self.get_hunt_queue())):
                temp_queue.append(bottom_quadrant)
                
            
            #Troubleshooting  
            # print(f"Left: {str(self.get_my_ship_board().get_column_markers()[left[1]])}" + f"{str(self.get_my_ship_board().get_row_markers()[left[0]])}")
            # print(f"Top: {str(self.get_my_ship_board().get_column_markers()[top[1]])}" + f"{str(self.get_my_ship_board().get_row_markers()[top[0]])}")
            # print(f"Right: {str(self.get_my_ship_board().get_column_markers()[right[1]])}" + f"{str(self.get_my_ship_board().get_row_markers()[right[0]])}")
            # print(f"Bottom: {str(self.get_my_ship_board().get_column_markers()[bottom[1]])}" + f"{str(self.get_my_ship_board().get_row_markers()[bottom[0]])}")
            # print(f"Queue: {temp_queue}")
            
            self.set_hunt_queue(temp_queue)
            

        #If we're done hunting
        elif (shot_determination == 4):
            
            #Set the hunting state to false and clear the hunting queue
            self.set_is_hunting(False)
            self.set_hunt_queue([])
            
        #Otherwise
        else:
            print(f"ERROR: Bot does not know how to handle shot determination of [{shot_determination}]")
    
    #Getters
    def get_search_space(self):
        return self.__search_space
    
    def get_hunt_queue(self):
        return self.__hunt_queue
    
    def get_previous_guesses(self):
        return self.__previous_guesses
    
    def get_is_hunting(self):
        return self.__is_hunting
    
    
    #Setters
    def set_search_space(self, ss):
        self.__search_space = ss
        
    def set_hunt_queue(self, hq):
        self.__hunt_queue = hq
        
    def set_previous_guesses(self, pm):
        self.__previous_guesses = pm
        
    def set_is_hunting(self, h):
        self.__is_hunting = h