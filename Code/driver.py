from Game_engine import game_engine

def main():
    game = game_engine()
    #game.set_player_board()
    #game.set_bot_board()
    #print(game.get_bot().get_my_ship_board())
    #print(game.get_bot().get_my_guess_board())
    
    game.get_bot().generate_search_space_static()
    
    while True:
        game.get_player().determine_shot(game.ship_search_static())
        print(game.get_player().get_my_ship_board())
        ui = input("Test")
    
    
if __name__ == "__main__":
    main()