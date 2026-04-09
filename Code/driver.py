from Game_engine import game_engine

def main():
    game = game_engine()
    #game.set_player_board()
    #game.set_bot_board()
    #print(game.get_bot().get_my_ship_board())
    #print(game.get_bot().get_my_guess_board())
    game.get_bot().generate_search_space_static()
    
if __name__ == "__main__":
    main()