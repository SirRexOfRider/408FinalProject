from Ship import ship
from Board import board

class player:
    
    #Data Attributes
    __my_ships = []
    __my_ship_board = [[]]
    __my_guess_board = [[]]
    
    def __init__(self):
        self.set_my_ships([ship("ACC", 5), ship("BAT", 4), ship("DST", 3), ship("SUB", 3), ship("PTR", 2)])
        self.set_my_ship_board(board())
        self.set_my_guess_board(board())
        
    #Helpers
    #============================= GET USER INPUT =================================================================================
    def get_user_input(self, prompt):
        """Get user input for selecting tiles. Validate that it matches options available on the board"""
        
        #Also make sure it's valid
        valid = False
        
        while (not valid):
            
            #Get input
            ui = input(prompt)
            
            #If user input is two characters long and is valid
            if (len(ui) == 2 and ui[1].isnumeric()):
                
                #If input is found within the board margins
                #Switch the first character to uppercase, just in case... get it... in.. case because.... i'm tired....
                if ((ui[0].upper() in self.get_my_ship_board().get_column_markers()) and (int(ui[1]) in self.get_my_ship_board().get_row_markers())):
                    valid = True
                    
                #Otherwise
                else:
                    print("ERROR: String not found within board limits")
                    
            #Because user can input A10, we need to check if the user input is 2 or three characters long
            #If the number ever goes above 10, it will just be defaulted to 10 
            elif (len(ui) == 3 and ui[1].isnumeric() and ui[2].isnumeric()):
                
                #If input is found within the board margins
                if (ui[0].upper() in self.get_my_ship_board().get_column_markers() and int(ui[1]) == 1 and int(ui[2]) == 0):
                    valid = True
                    
                #Otherwise
                else:
                    print("ERROR: String not found within board limits")
                    
            #If initial input is bad
            else:
                print("ERROR: Input not within Board bounds")
                
        #Return validated user input
        return ui
    
    
    # ======================================= DETERMINE SHOT =======================================================
    def determine_shot(self, quadrant):
        """A shot will be taken on this player's board to determine if it hits a ship"""
        
        #Get User Input will help verify this before it runs into this function
        coordinates = self.get_my_ship_board().convert_input(quadrant)
        updated_grid = self.get_my_ship_board().get_grid()
        current_tile = self.get_my_ship_board().get_grid()[coordinates[0]][coordinates[1]]
        
        #IF MISS
        if (current_tile == None or current_tile == "~0~~"):
            print("\n\t\t ~~~ M ~~~ M ~~~ M~~~ MISS ~~~ M ~~~ M ~~~ M ~~~")
            updated_grid[coordinates[0]][coordinates[1]] = "~0~~"
        
        #IF RE-HIT
        elif (current_tile == "~X~~"):
            print("\n\t\t    ??? ?? DAMAGED PART WAS HIT.. AGAIN ?? ???")
        
        #IF HIT
        else:
            print("\n\t\t! ! ! ! ! ! ! ! ! ! | HIT ! | ! ! ! ! ! ! ! ! ! !")

            #Find the name of the ship that was hit
            current_ship_index = 0
            
            current_ship = self.get_my_ships()[current_ship_index]
            
            #While we haven't found the name of the ship that was hit, keep iterating until we do
            while current_ship.get_name() != current_tile.get_part_of():
                current_ship_index += 1
                current_ship = self.get_my_ships()[current_ship_index]
            
            current_ship.hit_ship_section(-current_ship.find_distance_to_stern(current_tile))
            
            #If the current ship just sunk, also print that out to the user
            if (current_ship.get_is_sunk()):
                print("\t\t~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`")
                print("\t\t  S          U          N          K           !")
                print("\t\t~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`")
            
            #Modifided ship list
            modified_ship_list = self.get_my_ships()
            modified_ship_list[current_ship_index] = current_ship
            self.set_my_ships(modified_ship_list)

            updated_grid[coordinates[0]][coordinates[1]] = "~X~~"
            
        self.get_my_ship_board().set_grid(updated_grid)
    #===============================================================================================================================
    
    #Getters
    def get_my_ships(self):
        return self.__my_ships
    
    def get_my_ship_board(self):
        return self.__my_ship_board
    
    def get_my_guess_board(self):
        return self.__my_guess_board
    
    
    #Setters
    def set_my_ships(self, ships):
        self.__my_ships = ships
        
    def set_my_ship_board(self, msb):
        self.__my_ship_board = msb
        
    def set_my_guess_board(self, mgb):
        self.__my_guess_board = mgb