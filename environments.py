from array import *

# I converted my dictionary maps into lists.
# A fight will be on hostile tiles.

hostile = [
  'H Neighbourhood',
  'H Business District',
  'H Open Field'
  ]

# Neutral tiles are blank.

neutral = [
  'N Neighbourhood',
  'N Business District',
  'N Open Field'
    ]

# Friendly neighbourhoods give cash, which can be spent 
# on friendly business districts.

friendly = [
  'F Neighbourhood',
  'F Business District',
  ]

# There's also a start and end tile.
start = 'Neighbourhood'
end = 'Open Field'

# Creating map
map = []

# This map is intended to be a 3 by 9. This creates 25
# Open Field tiles,
for tile in range(0, 26):
  map.insert(tile, neutral[2])

# This replaces every six Open Fields with Friendly
# Businesses, 
for tile in range(5, 25, 6):
  del map[tile]
  map.insert(tile, friendly[1])

# and this replaces every four tiles with enemy tiles.
for tile in range(2, 22, 4):
  del map[tile]
  map.insert(tile, hostile[tile // 7])

# Create the start tile
del map[25]
map.insert(25, start)

# Create the end tile
del map[0]
map.insert(0, end)

# A low-level map design that will change when making the actual game. The maps are ordered in rows of 3.
map1 = [map[0], map[1], map[2]]
map2 = [map[3], map[4], map[5]]
map3 = [map[6], map[7], map[8]]
map4 = [map[9], map[10], map[11]]
map5 = [map[12], map[13], map[14]]
map6 = [map[15], map[16], map[17]]
map7 = [map[18], map[19], map[20]]
map8 = [map[21], map[22], map[23]]
map9 = [map[24], map[25]]

# Because organizing the maps into one variable takes
# too much space for one line, they're separated in two.
organizedmap1 = [map1, map2, map3, map4]
organizedmap2 = [map5, map6, map7, map8, map9]
