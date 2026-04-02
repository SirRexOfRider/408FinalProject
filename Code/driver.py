from Ship import ship
from Board import board
from Player import player

me = player()
me.get_my_ship_board().set_ship_on_grid(me.get_my_ships()[0], "A1", 0)
me.get_my_ship_board().set_ship_on_grid(me.get_my_ships()[1], "C4", 1)

print(me.get_my_ship_board())
#print(me.get_user_input())

#me.get_my_ship_board().remove_ship_from_grid(me.get_my_ships()[0].get_name())

#So anyways, I started blasting
while (True):
    ui = me.get_user_input()
    me.determine_shot(ui)
    print(me.get_my_ship_board())

#print(me.get_my_ships()[0])


