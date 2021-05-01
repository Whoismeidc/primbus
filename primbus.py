# Course: CS 30
# Quint: 4
# Date created: 26/04/2021
# Date last modified: 30/04/2021
# Name: Mark Luu
# Description: Husk of a text-based RPG.

from assets import *


# Player will eventually have 100 map movements to win
# the game.

moves = 100

# Establish which tile is the player tile.
bigmap.establish_tile()
print_map(goodmap)
while moves >= 0:
    # Checks which tile the player is on.
    bigmap.check_tile()
    print("Where would you like to go?")
    print("Up, Down, Left, or Right?")
    move = input("Or inventory? Perhaps stats?")
    # The player can move in the four directions, in lower
    # and upper case.
    goodmoves = ['Up', 'Down', 'Left', 'Right']
    medkits = ['Medkit', 'Potion', 'Ambrosia']
    if move.title() in goodmoves:
        print("Going " + move + ".")
        # If the player goes up, the player tile is 3 tiles
        # less. If the player goes up, the player tile is 1
        # tile less. Opposite for down and right.
        bigmap.adjust_place(move.title())
        bigmap.move_place()
        moves = moves - 1
        update_map()
    elif move.title() == 'Inventory':
        # Checks inventory.
        activeplayer.check_inventory()
        # If there's a medkit in here, it gets used.
    elif move.title() in medkits:
        activeplayer.medkit_use()
    elif move.title() == 'Stats':
        activeplayer.show_stats()

    else:
        print("I don't understand.")
