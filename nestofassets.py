# Course: CS 30
# Quint: 4
# Date created: 13/04/2021
# Date last modified: 13/04/2021
# Name: Mark Luu
# Description: Nested dictionaries of RPG assets

"""Inventory"""
# Dictionary of inventory

resources = {
  'Shul': {
    1: 'cash',
    2: 'medkit',
  },
  'Kali': {
    1: 'cash',
    2: 'medkit',
  },
  'Rey': {
    1: 'cash',
    2: 'knife',
  },
}

# Testing inventory

for target, goods in resources.items():
    print()
    print(target + " has these goods: ")
    for good in goods:
        print(goods[good])

"""Characters"""

# Dictionaries of character stats
charm = {
    'Shul': 'Kensei',
    'Kali': 'Data Wizard',
    'Rey': 'Barrier Jacket'
}

stamina = {
    'Shul': '2',
    'Kali': '2',
    'Rey': '4'
}

identity = {
    'Shul': 'Bryan Blodgett',
    'Kali': 'Anna Addison',
    'Rey': 'Nicko Scoops'
}

# Shul's character sheet

char0 = {
  'Shul': {
        'Charm': charm['Shul'],
        'Stamina': stamina['Shul'],
        'Identity': identity['Shul']
  }
}

# Testing Shul's stats
for target, stats in char0.items():
    print()
    print(target + "'s stats")
    for stat in stats.keys():
        print(stat + ": " + stats[stat])

# Kali's character sheet
char1 = {
    'Kali': {
        'Charm': charm['Kali'],
        'Stamina': stamina['Kali'],
        'Identity': identity['Kali']
    }
}

# Testing Kali's stats
for target, stats in char1.items():
    print()
    print(target + "'s stats")
    for stat in stats.keys():
        print(stat + ": " + stats[stat])

# Rey's character sheet
char2 = {
  'Rey': {
    'Charm': charm['Rey'],
    'Stamina': stamina['Rey'],
    'Identity': identity['Rey']
  }
}

# Testing Rey's stats
for target, stats in char2.items():
    print()
    print(target + "'s stats")
    for stat in stats.keys():
        print(stat + ": " + stats[stat])

"""Areas"""
# Dictionary of areas
location = {
  'Hostile': [
    'Neighbourhood',
    'Business District',
    'Open Field'
    ],
  'Neutral': [
    'Neighbourhood',
    'Business District',
    'Open Field'
    ],
  'Friendly': [
    'Neighbourhood',
    'Business District',
    ]
}

# Testing areas
for safety, spots in location.items():
    print()
    for spot in spots:
        print("You've landed in a " + safety + " " +
              spot + ".")
