from Game_engine import game_engine
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

#Load this to play music :)
import pygame


#This will help make pauses in the game
import time

#I had to look up how to do most of this
#Now's a great time to mention I'm NOT a front-end person lol
class GUI:
    def __init__(self, root):

        #Declare root for the GUI window
        self.__root = root
        self.__root.title("Braxton's Battleship")
        self.__root.geometry("1000x600")

        #Declare the game engine and initialize the bot board
        self.__engine = game_engine()
        self.__engine.set_bot_board()
        self.__engine.get_bot().generate_search_space_static()

        #This will help with setting up the ships initially
        #The ship index is used to find which ship we are currently placing from the player's ships
        self.__current_ship_index = 0
        
        #This is a flag value that determines whether the current input should be classified as a quadrant value or an axis value
        self.__input_flag = "q"
        
        #Another flag value to determine what to do with the input itself
        self.__ships_set = False
    

        #===================== GUI TIME!!! =====================================
        self.__main_frame = ttk.Frame(self.__root)
        self.__main_frame.pack(fill=tk.BOTH, expand=True)

        self.__main_frame.columnconfigure(0, weight=10)
        self.__main_frame.columnconfigure(1, weight=0)
        self.__main_frame.columnconfigure(2, weight=10)
        self.__main_frame.rowconfigure(0, weight=5)

        #Left window
        left_frame = ttk.LabelFrame(self.__main_frame, text="Player Board")
        left_frame.grid(row=0, column=0, sticky="nsew")
        self.__left_window = ScrolledText(left_frame, wrap=tk.WORD, font=("Arial", 12))
        self.__left_window.pack(fill=tk.BOTH, expand=True)

        #Center window
        center_frame = ttk.LabelFrame(self.__main_frame, text="Game Messages")
        center_frame.grid(row=0, column=1, sticky="nsew")
        self.__center_window = ttk.Label(center_frame, anchor="center", justify="center", font=("Arial", 12, "bold"), wraplength=250)
        self.__center_window.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        #Right window
        right_frame = ttk.LabelFrame(self.__main_frame, text="Guess Board")
        right_frame.grid(row=0, column=2, sticky="nsew", padx=5)
        self.__right_window = ScrolledText(right_frame, wrap=tk.WORD, font=("Arial", 12))
        self.__right_window.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        #Input
        input_frame = ttk.Frame(self.__root, padding=(10, 20, 10, 10))
        input_frame.pack(fill=tk.X)
        self.__input_var = tk.StringVar()
        self.__user_input = ttk.Entry(input_frame, textvariable=self.__input_var, font=("Arial", 12))
        self.__user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.__submit_button = ttk.Button(input_frame, text="Submit", command=self.submit_input)
        self.__submit_button.pack(side=tk.RIGHT)
        self.__user_input.bind("<Return>", lambda event: self.submit_input())

        #Set up the initial boards (should just be blank)
        self.update_left_window(self.__engine.get_player().get_my_ship_board())
        self.update_right_window(self.__engine.get_player().get_my_guess_board())

        #BEGIN PLACEMENT
        self.ask_for_quadrant()

    #============= UPDATE FUNCTIONS ========================

    #Update the left window using an incoming board object (player ship board)
    def update_left_window(self, board):
        self.__left_window.delete(1.0, tk.END)
        self.__left_window.insert(tk.END, board.__strGUI__())

    #Update the right window using an incoming board object (player guess board)
    def update_right_window(self, board):
        self.__right_window.delete(1.0, tk.END)
        self.__right_window.insert(tk.END, board.__strGUI__())

    #Update the center window to display what is going on
    def update_message(self, text):
        self.__center_window.config(text=text)

    
    #====================== SET PLAYER SHIPS ========================================
    def ask_for_quadrant(self):
        ship = self.__engine.get_player().get_my_ships()[self.__current_ship_index]
        self.__input_flag = "q"
        self.update_message(f"Enter quadrant for [{ship.get_name()}]\n(Example: A5, G6)")

    def ask_for_axis(self):
        self.__input_flag = "a"
        self.update_message(f"Enter axis:\n0 = Horizontal\n1 = Vertical")

    
    #Get the input from the input frame
    def submit_input(self):

        #INPUT IS USED TO SET SHIPS ON PLAYER BOARD
        if (self.__ships_set == False):
            
            #Get the string from the input
            ui = self.__input_var.get().strip()

            #If there's nothing there, don't do anything
            if not ui:
                return

            #Clear the input bar
            self.__input_var.set("")

            #Save input as a quadrant
            if self.__input_flag == "q":
                self.__current_quadrant = ui
                self.ask_for_axis()

            # ================= AXIS INPUT =================
            elif self.__input_flag == "a":

                #Try and catch for converting the integer to a string
                try:
                    axis = int(ui)

                    #If the axis isn't a 0 or 1
                    if axis != 0 and axis != 1:
                        raise ValueError

                    #Place the ship and check if there was an error
                    error = self.__engine.get_player().get_my_ship_board().set_ship_on_grid(self.__engine.get_player().get_my_ships()[self.__current_ship_index], self.__current_quadrant, axis)
                    
                    #If there was an error with placing the ship (anything but 0), don't increment and ask again
                    if (error == 0):
                        print("HERE")
                        self.update_left_window(self.__engine.get_player().get_my_ship_board())
                        self.__engine.get_player().get_my_ship_board()
                        self.__current_ship_index += 1

                    #Can't get this to print to the center window even with sleep :(
                    else:
                        self.update_message("ERROR WITH INPUT! TRY AGAIN")
                        

                    #If all of the ships have been placed, then the actual game can start
                    #THIS IS WHERE THE FLAG VALUE CHANGES
                    if self.__current_ship_index >= len(self.__engine.get_player().get_my_ships()):

                        self.update_message("Input quadrants to fire at!")
                        self.__ships_set = True

                    #Keep asking for quadrants until all ships are placed
                    else:
                        self.ask_for_quadrant()

                #Catch an axis error
                except ValueError:
                    self.update_message("Invalid axis.\nEnter 0 or 1.")
            
        #INPUT IS NOW USED TO FIRE DA GUNS
        #If you couldn't tell by my comments, I am heavily sleep deprived while writing this
        elif (self.__ships_set):
            
            #================ PLAYER ================================
            #Get the string from the input
            ui = self.__input_var.get().strip()

            #If there's nothing there, don't do anything
            if not ui:
                return

            #Clear the input bar
            self.__input_var.set("")
            
            shot_determination = self.__engine.get_bot().determine_shot_GUI(ui)
            self.__engine.get_player().update_guess_board(ui, shot_determination)
            
            print(self.__engine.get_player().get_my_guess_board())
            #Update the player guess board to GUI
            self.update_right_window(self.__engine.get_player().get_my_guess_board())
            
            #Get string
            output_string = self.__engine.end_game(self.__engine.determine_winner())
            
            #Determine if player won
            if output_string != "":
                
                #This sounds way cooler than it actually is haha
                self.__root.destroy()
                
                print(output_string)
            
            #Add a pause
            time.sleep(0.5)
            
            #================== BOT =================================
            
            #Determine current state of bot
            print(f"CURRENT BOT SEARCH QUEUE: {self.__engine.get_bot().get_search_space()}")
            #If hunting
            if (self.__engine.get_bot().get_is_hunting()):
                bot_guess = self.__engine.ship_hunt_static()
                shot_determination = self.__engine.get_player().determine_shot_GUI(bot_guess)
                
                #This will determine whether the bot keeps hunting or switches back to searching
                self.__engine.get_bot().update_hunt_queue(shot_determination)
                    
            #If searching
            elif (not self.__engine.get_bot().get_is_hunting()):
                bot_guess = self.__engine.ship_search_static()
                shot_determination = self.__engine.get_player().determine_shot(bot_guess)
                
                #If the bot hits a ship, switch to hunting mode
                if shot_determination == 3:
                    self.__engine.get_bot().set_is_hunting(True)
                    self.__engine.get_bot().update_hunt_queue(shot_determination)
            
            
            self.__engine.get_bot().update_guess_board(bot_guess, shot_determination)
                
            #print(self.__engine.get_player().get_my_ship_board())
            #Update the player's ship board
            self.update_left_window(self.__engine.get_player().get_my_ship_board())
        
            #Get string
            output_string = self.__engine.end_game(self.__engine.determine_winner())
            
            #Determine if bot won
            if output_string != "":
                
                #This sounds way cooler than it actually is haha
                self.__root.destroy()
                
                print(output_string)
                
            #Add a pause
            time.sleep(0.5)

    #Yoinked this from the black jack project from 150
    #Gambling does pay off!!!      
    def init_music(self):
        #Add music
        theme = 'Code\Bop.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(theme)
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.fadeout(2)
        
        #Negative 1 makes it infinite loop for the music
        pygame.mixer.music.play(-1)


#If main, main
if __name__ == "__main__":

    #Initialize the GUI
    root = tk.Tk()
    gui = GUI(root)
    gui.init_music()

    #Runnit
    root.mainloop()