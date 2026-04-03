from Player import player
from Bot import bot

class game_engine:
    
    #DATA ATTRIBUTES
    __player = None
    __bot = None
    
    #Init
    def __init__(self):
        self.set_player(player())
        self.set_bot(bot())


    #Helpers
    #========================= SET PLAYER BOARD ================================================================
    def set_player_board(self):
        """Player will set ships on their grid using user input"""
        
        #Determine which way the ship will be placed
        axis = 0
        
        #Kepp track of what ship we're on
        iteration_count = 0
        
        #For as many ships in their ship_list
        while (iteration_count < len(self.get_player().get_my_ships())):
            
            #Get quadrant from user
            ui = self.get_player().get_user_input(f"Enter quadrant to place ship |{self.get_player().get_my_ships()[iteration_count].get_name()}|: ")
            
            #Ask for axis
            axis = int(input("Axis? (0 Horiz, 1 Vert): "))
            
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
                
                #To make sure we don't go into negative indexing
                if (iteration_count == 0):
                    pass
                
                else:
                    iteration_count -= 1
          
    #======================= PLAY GAME =========================================================          
    def play_game(self):
        pass

    #Getters
    def get_player(self):
        return self.__player

    def get_bot(self):
        return self.__bot

    #Setters
    def set_player(self, p):
        self.__player = p

    def set_bot(self, b):
        self.__bot = b
