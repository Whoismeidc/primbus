# Course: CS 30
# Quint: 4
# Date created: 2021/03/17
# Date last modified: 2021/03/17
# Name: Mark Luu
# Description: Numbered lists for RPG inventories.

# Set of lists.
equipment = ['Levinbolt', 'Barrier Jacket', 'Data Wizard']
upgrades = ['Spread', 'Quality', 'Adamant', 'Pushing', 'Lasting']
environments = ['Neighbourhood', 'Business District', 'Open Field']

# Prints equipment in numerical loop.
print("Available charms:")
for point in range(0, 3, 1):
    print(str(point + 1) + ". " + equipment[point])
# Prints upgrades in numerical loop.
print("Available upgrades:")
for point in range(0, 5, 1):
    print(str(point + 1) + ". " + upgrades[point])
# Prints maps in numerical loop.
print("Available maps:")
for point in range(0, 3, 1):
    print(str(point + 1) + ". " + environments[point])
