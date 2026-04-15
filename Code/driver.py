from Game_engine import game_engine

def main():
    game = game_engine()
    game.set_player_board()
    #game.set_bot_board()
    #print(game.get_bot().get_my_guess_board())
    
    game.get_bot().generate_search_space_static()
    
    #print(game.get_player().get_my_guess_board())
    print(game.get_player().get_my_ship_board())
    
    #While the game is running
    while True:
        
        
        #================ PLAYER ================================
        #ui = game.get_player().get_user_input("Enter a Quadrant [A5, B10, etc]: ")
        #shot_determination = game.get_bot().determine_shot(ui)
        #game.get_player().update_guess_board(ui, shot_determination)
        #print(game.get_player().get_my_guess_board())
        
        #================== BOT =================================
        
        #Determine current state of bot
        #If hunting
        if (game.get_bot().get_is_hunting()):
            bot_guess = game.ship_hunt_static()
            shot_determination = game.get_player().determine_shot(bot_guess)
            
            #If a ship has been fully destroyed, swtich to search mode and clear the hunting queue
            if shot_determination == 4:
                game.get_bot().update_hunt_queue(shot_determination)
                
                
            #Otherwise, update the hunting queue
            else:
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
        #print(game.get_bot().get_my_guess_board())
        test = input("Test")
            
        
        
        
    
#If main, main 
if __name__ == "__main__":
    main()