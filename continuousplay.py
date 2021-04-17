# Course: CS 30
# Quint: 4
# Date created: 16/04/2021
# Date last modified: 16/04/2021
# Name: Mark Luu
# Description: Demonstration of continuous play

# Dummy number to start the loop
check = 0

# Start the loop
while check >= 0:
    """Instructions for the player, for movement"""

    print("Where would you like to go?")

    print("North, east, west, or south?")

    print("Or would you like to use the menu?")

    # move = input should accept the compass directions
    # as well as the menu and quit inputs
    # regardless of capitalization. It'll also take the
    # first letter of the move.

    move = input("Use quit to move on to the next loop.")

    if move.title() == 'North' or move.title() == 'N':
        print("Going north.")

    elif move.title() == 'East' or move.title() == 'E':
        print("Going east.")

    elif move.title() == 'West' or move.title() == 'W':
        print("Going west.")

    elif move.title() == 'South' or move.title() == 'S':
        print("Going south.")

    elif move.title() == 'Menu' or move.title() == 'M':
        print("Pulling up the menu.")

    elif move.title() == 'Quit' or move.title() == 'Q':
        print("Shutting down.")
        break

    # This plays when you use an unavailable input.
    else:
        print("What is that?")

# There's a new loop when the first one is broken.
while check >= 0:
    """More instructions for the player, for combat."""

    # The amount of commands to use items is too long,
    # so they're in a list.

    items = ['Use Items', 'Use', 'Items', 'U', 'I']

    # Much like movement, combat takes the full word in
    # any capitalization, or the first letter in any
    # captialization.

    print("What would you like to do?")

    print("Defend, use items, or run away?")

    move = input("Use quit to end the assignment.")

    if move.title() == 'Defend' or move.title() == 'D':
        print("Guarding!")

    # Calling on the list from before.

    elif move.title() in items:
        print("Checking your inventory.")

    elif move.title() == 'Run' or move.title() == 'R':
        print('Running!')

    elif move.title() == 'Quit' or move.title() == 'Q':
        print('Shutting down.')
        break

    # For invalid inputs.
    else:
        print("What is that?")
