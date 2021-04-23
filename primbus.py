# Course: CS 30
# Quint: 4
# Date created: 10/03/2021
# Date last modified: 23/03/2021
# Name: Mark Luu
# Description: A demonstration of the application of
# modules, complete with the creation of a map.

from environments import *

from resources import *

from characters import *

from enemies import *


# Test characters and resources
print(items['Shul'])

# Test environments
for map in organizedmap1:
  print(f"{str(map)}")

for map in organizedmap2:
  print(f"{str(map)}")

# Test resources
print(weapon[1])

# Test enemies
print(goon)
