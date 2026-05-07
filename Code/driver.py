from Game_engine import game_engine

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
             
        #Get string
        output_string = game.end_game(game.determine_winner())
        
        #Determine if bot won
        if output_string != "":
            
            is_running = False
            print(output_string)
            print(count)
            continue
            
        print(game.get_player().get_my_ship_board())
        print(game.get_player().get_my_guess_board())
        
#If main, main 
if __name__ == "__main__":
    main()