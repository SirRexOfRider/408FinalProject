from Game_engine import game_engine
import pygame
import sys

pygame.init()


#===== WINDOW ====================

width = 1200
height = 800

grid_size = 10
cell_size = 48

board_width = grid_size * cell_size
board_height = grid_size * cell_size

fps = 60

#screen = pygame.display.set_mode((width, height))
#pygame.display.set_caption("BATTLESHIP!")

clock = pygame.time.Clock()

#============= STYYYLLLEEEE ======================
bg = (5,10, 25)

grid_blue = (40, 140, 255)
grid_dark = (15, 40, 80)

red = (255, 60, 60)
green = (80, 255, 140)

white = (230, 230, 230)

ship = (120, 130, 150)
miss = (180, 220, 255)
hit = (255, 80, 80)

title_font = pygame.font.SysFont("consolas", 48, bold = True)
ui_font = pygame.font.SysFont("consolas", 24)
small_font = pygame.font.SysFont("consolas", 18)

#======= BOARD ======================================
px = 80
py = 180
bx = 640
by = 180

#==== DRAW TO SCREEN ================================


def main():
    
    #Flag to determine who wins the game
    who_won = -1
    game = game_engine()
    game.set_player_board()
    game.set_bot_board()
    #print(game.get_bot().get_my_guess_board())
    
    game.get_bot().generate_search_space_static()
    
    count = 0
    
    is_running = True
    #While the game is running
    while is_running:
        
        count += 1
        #================ PLAYER ================================
        ui = game.get_player().get_user_input("Enter a Quadrant [A5, B10, etc]: ")
        shot_determination = game.get_bot().determine_shot(ui)
        game.get_player().update_guess_board(ui, shot_determination)
        
        print(game.get_player().get_my_guess_board())
        
        #Get string
        output_string = game.end_game(game.determine_winner())
        
        #Determine if player won
        if output_string != "":
            
            is_running = False
            print(output_string)
            continue
        
        #================== BOT =================================
        
        #Determine current state of bot
        
        #If hunting
        if (game.get_bot().get_is_hunting()):
            bot_guess = game.ship_hunt_static()
            shot_determination = game.get_player().determine_shot(bot_guess)
            
            #This will determine whether the bot keeps hunting or switches back to searching
            game.get_bot().update_hunt_queue(shot_determination)
                
        #If searching
        elif (not game.get_bot().get_is_hunting()):
            bot_guess = game.ship_search_static()
            shot_determination = game.get_player().determine_shot(bot_guess)
            
            #If the bot hits a ship, switch to hunting mode
            if shot_determination == 3:
                game.get_bot().set_is_hunting(True)
                game.get_bot().update_hunt_queue(shot_determination)
        
        
        game.get_bot().update_guess_board(bot_guess, shot_determination)
             
        print(game.get_player().get_my_ship_board())
    
        #Get string
        output_string = game.end_game(game.determine_winner())
        
        #Determine if bot won
        if output_string != "":
            
            is_running = False
            print(output_string)
            print(count)
            continue
            
        
#If main, main 
if __name__ == "__main__":
    main()