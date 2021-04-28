from tabulate import tabulate

# Shop tiles for the final project.
class FriendlyBusiness:
    def __init__(store, amount):
        store.items = []
        store.amount = 3
  
    def additems(store, *items):
        for item in items:
            store.items.append(item)

class FriendlyNeighborhood:
    def __init__(home, money):
        home.money = []
  
    def addmoney(home, money):
        home.money.append(money)

# Blank tiles that waste the player's time.

class Tile:
    def __init__(tile, name):
        tile.name = name

# Tile that spawns enemies.

class HostileTile(Tile):
    def __init__(tile, name, enemy):
        super().__init__(name)
        tile.enemy = enemy

class Map:
    # Row is how wide the map is. Column is how tall the
    # map is. The coordinate starts at the last tile.
    def __init__(scroll, row, column):
        scroll.row = row
        scroll.column = column
        scroll.tiles = []
        scroll.coord = scroll.row * scroll.column - 1
        scroll.playertile = 0

  # Adds tiles named after the tile name.
    def make_map(scroll, tile):
        for i in range(scroll.row):
            for i in range (scroll.column):
                scroll.tiles.append(tile.name)
  
    # Replaces tiles with meaningful ones.
    def replace_tile(scroll, tile, beats, lastindex):
        for spot in range(0, int(lastindex), beats):
            del scroll.tiles[spot]
            scroll.tiles.insert(spot, tile.name)
  
    # Places sections of map in a list for use in an
    # array.
    def move_map(scroll, submap, firstindex, lastindex):
        for spot in range(firstindex, lastindex):
            submap.insert(spot, scroll.tiles[spot])

    def basic_print_map(scroll):
        print(scroll.tiles)

    # Check the name of the tile the player is on.
    def check_tile(scroll):
        print(scroll.tiles[scroll.coord])

    # Removes the tile player was on, replaces it with a
    # tile the player was not on, and indicates their next
    # position.
    def adjust_place(scroll, direction):
        del scroll.tiles[scroll.coord]
        scroll.tiles.insert(scroll.coord,
        scroll.playertile)
        if direction.title() == 'Up':
            scroll.coord = scroll.coord - 3
        elif direction.title() == 'Down':
            scroll.coord = scroll.coord + 3
        elif direction.title() == 'Left':
            scroll.coord = scroll.coord - 1
        elif direction.title() == 'Right':
            scroll.coord = scroll.coord + 1
    
  
    # Puts the player on the next position.
    def move_place(scroll):
        scroll.playertile = scroll.tiles.pop(scroll.coord)
        scroll.tiles.insert(scroll.coord,
        f"{scroll.playertile}*")
        return goodmap
  
    # Creates the player tile.
    def establish_tile(scroll):
        scroll.playertile = scroll.tiles[scroll.coord]

# Creates a 3 by 8 map of open field.

bigmap = Map(3, 8)

field = Tile('Open Field')

bigmap.make_map(field)

# Replaces every five tiles with bad neighbourhoods.
slum = HostileTile('Bad Neighbourhood', 'Goon')

bigmap.replace_tile(slum, 5, 24)

# Replaces start and end of map with Start and End tiles.
start = Tile('Start')

end = HostileTile('End', 'Boss')

bigmap.replace_tile(start, 23, 24)
bigmap.replace_tile(end, 24, 24)
bigmap.basic_print_map()

# bigmap.print_map()

# The map array is not equipped for modularity.
map1 = []
map2 = []
map3 = []
map4 = []
map5 = []
map6 = []
map7 = []
map8 = []
# Steals sections of three tiles from bigmap.
bigmap.move_map(map1, 0, 3)
bigmap.move_map(map2, 3, 6)
bigmap.move_map(map3, 6, 9)
bigmap.move_map(map4, 9, 12)
bigmap.move_map(map5, 12, 15)
bigmap.move_map(map6, 15, 18)
bigmap.move_map(map7, 18, 21)
bigmap.move_map(map8, 21, 24)

goodmap = [map1, map2, map3, map4, map5, map6, map7, map8]

# Copies the above process.
def update_map():
    map1 = []
    map2 = []
    map3 = []
    map4 = []
    map5 = []
    map6 = []
    map7 = []
    map8 = []
    bigmap.move_map(map1, 0, 3)
    bigmap.move_map(map2, 3, 6)
    bigmap.move_map(map3, 6, 9)
    bigmap.move_map(map4, 9, 12)
    bigmap.move_map(map5, 12, 15)
    bigmap.move_map(map6, 15, 18)
    bigmap.move_map(map7, 18, 21)
    bigmap.move_map(map8, 21, 24)
    goodmap = [map1, map2, map3, map4,
    map5, map6, map7, map8]
    print_map(goodmap)
    # If player is standing on end tile, they win.
    if 'End*' in map1:
        print("You win!")

# Prints the map neatly, according to the list array.
# Because there are eight maps, each of which has 3 tiles,
# it prints a 3 by 8.
def print_map(scroll):
    """print out each city map generated"""
    # format the maps in rows and columns
    print(tabulate(scroll, tablefmt="plain"))
    print("\n")
