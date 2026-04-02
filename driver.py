from Ship import ship
from Board import board
from Player import player

me = player()
me.get_my_ship_board().set_ship_on_grid(me.get_my_ships()[0], "A1", 0)
me.get_my_ship_board().set_ship_on_grid(me.get_my_ships()[1], "C4", 1)

print(me.get_my_ship_board())
#print(me.get_user_input())

#me.get_my_ship_board().remove_ship_from_grid(me.get_my_ships()[0].get_name())
print(me.determine_shot("A1"))
print(me.determine_shot("B1"))
print(me.determine_shot("C1"))
print(me.determine_shot("D1"))
print(me.determine_shot("E1"))
print(me.get_my_ships()[0])


