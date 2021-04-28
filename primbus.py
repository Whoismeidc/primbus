# Course: CS 30
# Quint: 4
# Date created: 26/04/2021
# Date last modified: 28/04/2021
# Name: Mark Luu
# Description: Classes for a text-based RPG.

from characters import *
from environments import *
from resources import *

# Player will eventually have 100 map movements to win
# the game.

moves = 100

# Establish which tile is the player tile.
bigmap.establish_tile()

while moves >= 0:
    # Bug testing: checks which tile the player is on.
    bigmap.check_tile()
    print("Where would you like to go?")
    move = input("Up, Down, Left, or Right?")
    # The player can move in the four directions, in lower
    # and upper case.
    goodmoves = ['Up', 'Down', 'Left', 'Right']

    if move.title() in goodmoves:
        print("Going " + move + ".")
        # If the player goes up, the player tile is 3 tiles
        # less. If the player goes up, the player tile is 1
        # tile less. Opposite for down and right.
        bigmap.adjust_place(move.title())
        bigmap.move_place()
        update_map()

    else:
        print("I don't understand.")
