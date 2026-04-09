
class board:
    
    #Data attributes
    __grid = [[]]
    __row_markers = []
    __column_markers = []
    
    #Init
    def __init__(self):
        
        #10 X 10 board
        #Will have ships placed in areas where there is null space
        self.set_grid([[None for _ in range(10)] for _ in range(10)])
        self.set_column_markers(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.set_row_markers([1,2,3,4,5,6,7,8,9,10])
        
    #Helpers
    #================== CONVERT USER INPUT ====================================================
    def convert_input(self, quadrant):
        
        #While we aren't on the same row as the starting_index
        column_index = 0
        
        while (self.get_column_markers()[column_index] != quadrant[0].upper()):
            column_index += 1
        
        #Set starting position of the ship
        #These values are technically swapped from A6 to 6A (row -> column)
       
        #If the length of the string is 3 (meaning the number value is 10)
        if (len(quadrant) == 3):
            coordinates = [10 - 1, column_index]
            
            
        #If the length of the string is 2 (A6)
        elif (len(quadrant) == 2):
            coordinates = [int(quadrant[1]) - 1, column_index]
            
        #Otherwise
        else:
            coordinates = [-1]
            
        return coordinates
    
    #============================= SET SHIP ON GRID =========================================================
    def set_ship_on_grid(self, ship = None, quadrant = "", axis = 0):
        """Take in a ship object and try to place it on the grid using the starting index and axis\n
        For the starting index, it will be a string that will be parsed (A6)\n
        For the axis value, 0 is horizontal and 1 is vertical"""
        
        #Firstly, find the exact coordinates of the ship using the starting index
        #Assume that the starting index is within the bounds of the board (player object will handle verifying that)
        
        #Coordinate values that will be determined
        coordinates = self.convert_input(quadrant)
        
        #Flag to help determine success of ship placement
        error_value = 0
        
        #If no errors so far
        if (coordinates[0] != -1):
            #If the ship is horizontal
            if (axis == 0):
                
                #Flag value to see if the ship positioning is good
                valid = True
                
                #Check if there's enough room for the ship horizontally
                #Because the ship is occupying the first space, we can go up to ten
                #Another way to say this is if we subtracted 1 from ship length and it was greater than 9
                if (coordinates[1] + ship.get_length() > 10):
                    print("ERROR: Ship is out of bounds of Board Horizontally")
                    error_value = 1
                    valid = False
                
                if valid:
                    #Check to see if all tiles are open horizontally (not None)
                    for x in range(ship.get_length()):
                        
                        if (self.get_grid()[coordinates[0]][coordinates[1] + x] != None):
                            print("ERROR: Ship collides with another entity")
                            error_value = 2
                            valid = False
                            
                #IF after both checks valid is true, place the ship on the grid
                if valid:
                    updated_grid = self.get_grid()
                    for x in range(ship.get_length()):
                        updated_grid[coordinates[0]][coordinates[1] + x] = ship.get_ship_sections()[x]
                        
                    self.set_grid(updated_grid)
            
            elif (axis == 1):
                
                #Flag value to see if the ship positioning is good
                valid = True
                
                # Check if there's enough room for the ship horizontally
                # print(coordinates[0])
                # print(ship.get_length())
                # print()
                
                if (coordinates[0] + ship.get_length() > 10):
                    print("ERROR: Ship is out of bounds of Board Vertically")
                    error_value = 1
                    valid = False
                
                if valid:
                    
                    #Check to see if all tiles are open vertically (not None)
                    for x in range(ship.get_length()):
                        
                        if (self.get_grid()[coordinates[0] + x][coordinates[1]] != None):
                            print("ERROR: Ship collides with another entity")
                            error_value = 2
                            valid = False
                            pass
                            
                #IF after both checks valid is true, place the ship on the grid
                if valid:
                    updated_grid = self.get_grid()
                    
                    for x in range(ship.get_length()):
                        
                        # print(coordinates[0] + x)
                        # print(coordinates[1])
                        # print("COORDS: \n")
                        updated_grid[coordinates[0] + x][coordinates[1]] = ship.get_ship_sections()[x]
                        
                    self.set_grid(updated_grid)
        
          
        #Should return 0 if successfull
        return error_value
    
    #======================== REMOVE SHIP FROM GRID ==============================================================
    def remove_ship_from_grid(self, ship_name):
        """Remove a ship from the board using the name of the ship that was last hit"""
        #Using the ship part that was last hit and destroyed, remove all other ship parts of the same name from the grid
        for x in range(10):
            for y in range(10):
                #If there's a ship on this tile and it's the same name as the destroyed ship
                if (self.get_grid()[x][y] != None):
                    
                    if (self.get_grid()[x][y].get_part_of() == ship_name):
                        updated_grid = self.get_grid()
                        updated_grid[x][y] = "~#~~"
                        self.set_grid(updated_grid)
                            
    #Getters
    def get_grid(self):
        return self.__grid
    
    def get_row_markers(self):
        return self.__row_markers
    
    def get_column_markers(self):
        return self.__column_markers
    
    #Setters
    def set_grid(self, g):
        self.__grid = g
        
    def set_row_markers(self, rm):
        self.__row_markers = rm
        
    def set_column_markers(self, cm):
        self.__column_markers = cm
    
    def __str__(self):
        temp = "\n\t\t=================================================\n"
        temp += "\t\t=================================================\n"
        
        temp += "\t\t|   | A | B | C | D | E | F | G | H | I | J  |  |"
        
        #For every row
        for x in range(10):
            #If at the end of the rows, this line requires a bit of modifying
            if (x == 9):
                temp += f"\n\t\t|1 0|"
            else:      
                temp += f"\n\t\t| {self.get_row_markers()[x]} |"
            #For every column in row
            for y in range(10):
                
                #If the current tile is None
                if (self.get_grid()[x][y] == None):
                    temp += "~~~~"
                    
                #If this tile is currently flagged as hit
                elif (self.get_grid()[x][y] == "~X~~"):
                    temp += "~X~~"
                    
                #If the tile is currently flagged as a miss
                elif (self.get_grid()[x][y] == "~0~~"):
                    temp += "~0~~"
                    
                #If there's a ship at this tile
                else:
                    temp += f"{self.get_grid()[x][y].get_part_of()}~"
                    
            temp += "|  |"
                    
        temp += "\n\t\t=================================================\n"
        
        return temp