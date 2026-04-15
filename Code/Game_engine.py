from Player import player
from Bot import bot
from random import randint

class game_engine:
    
    #DATA ATTRIBUTES
    __player = None
    __bot = None
    __game_over = 0
    
    #Init
    def __init__(self):
        self.set_player(player())
        self.set_bot(bot())
        self.set_game_over(0)

    #Helpers
    #========================= SET PLAYER BOARD ================================================================
    def set_player_board(self):
        """Player will set ships on their grid using user input"""
        
        #Kepp track of what ship we're on
        iteration_count = 0
        
        #For as many ships in their ship_list
        while (iteration_count < len(self.get_player().get_my_ships())):
            
            #Determine which way the ship will be placed
            axis = -1
            
            #Get quadrant from user
            ui = self.get_player().get_user_input(f"Enter quadrant to place ship |{self.get_player().get_my_ships()[iteration_count].get_name()}|: ")
            
            try:
                #Ask for axis
                axis = int(input("Axis? (0 Horiz, 1 Vert): "))
                
            except Exception as e:
                pass
                
            #If axis is vaild
            if (axis == 0 or axis == 1):
                
                #Try setting the ship at that tile, return error value
                error_value = self.get_player().get_my_ship_board().set_ship_on_grid(self.get_player().get_my_ships()[iteration_count], ui, axis)
                
                #If there was an error, don't set ship
                if (error_value != 0):
                    pass
                    
                #Otherwise, set ship and go to the next in the list
                else:
                
                    self.set_player(self.get_player())
                    print(self.get_player().get_my_ship_board())
                    iteration_count += 1
                
            #Otherwise
            else:
                print("ERROR: AXIS ERROR")
                
    #========================= SET BOT BOARD ==========================================
    def set_bot_board(self):
        """Bot will set ships on their grid using randomly generated input"""
        
        #Kepp track of what ship we're on
        iteration_count = 0
        
        
        #For as many ships in their ship_list
        while (iteration_count < len(self.get_player().get_my_ships())):
            
            #Determine which way the ship will be placed
            axis = -1
            
            #Generate random numbers and make a random quadrant
            num1 = randint(0,9)
            num2 = randint(0,9)
            axis = randint(0,1)
            
            gen_quadrant = f"{str(self.get_bot().get_my_ship_board().get_column_markers()[num1])}" + f"{str(self.get_bot().get_my_ship_board().get_row_markers()[num2])}"
            
            #If axis is vaild
            if (axis == 0 or axis == 1):
                
                #Try setting the ship at that tile, return error value
                error_value = self.get_bot().get_my_ship_board().set_ship_on_grid(self.get_bot().get_my_ships()[iteration_count], gen_quadrant, axis)
                
                #If there was an error, don't set ship
                if (error_value != 0):
                    pass
                    
                #Otherwise, set ship and go to the next in the list
                else:
                    
                    self.set_player(self.get_bot())
                    #print(self.get_bot().get_my_ship_board())
                    iteration_count += 1
                
            #Otherwise
            else:
                print("ERROR: AXIS ERROR")
                
    #========================================== BOT GAME LOGIC ==============================================================                
    def ship_search_static(self):
        """Search in diagonal lines to find player ships, return a quadrant to shoot"""
        
        #Search the space diagonally and update the search space list for the bot
        search_space = self.get_bot().get_search_space()
        guess = search_space.pop(0)
        self.get_bot().set_search_space(search_space)
        
        #Also add the guess to the previously guessed list
        temp_list = self.get_bot().get_previous_guesses()
        temp_list.append(guess)
        self.get_bot().set_previous_guesses(temp_list)
        
        #Return the guess
        return guess
    
    def ship_hunt_static(self):
        """Hunt down a ship once one is detected, return a quadrant to shoot"""
        
        #Search the surrounding quadrants
        hunt_queue = self.get_bot().get_hunt_queue()
        guess = hunt_queue.pop(0)
        self.get_bot().set_hunt_queue(hunt_queue)
        
        #Also add these guesses to the previously guessed list
        temp_list = self.get_bot().get_previous_guesses()
        temp_list.append(guess)
        self.get_bot().set_previous_guesses(temp_list)
        
        #Finally, remove this guess from the static search list
        search_space = self.get_bot().get_search_space()
        search_space.remove(guess)
        self.get_bot().set_search_space(search_space)
        
        
        return guess
          
    #======================= PLAY GAME =========================================================          
    def play_game(self):
        pass

    #Getters
    def get_player(self):
        return self.__player

    def get_bot(self):
        return self.__bot
    
    def get_game_over(self):
        return self.__game_over

    #Setters
    def set_player(self, p):
        self.__player = p

    def set_bot(self, b):
        self.__bot = b

    def set_game_over(self, go):
        return self.__game_over