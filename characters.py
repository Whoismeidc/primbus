from resources import *

# Dictionaries of character stats.
charm = {
    'Shul': 'Kensei',
    'Kali': 'Data Wizard',
    'Rey': 'Barrier Jacket'
}

# Character health is determined by stamina + 5.
charstamina = {
    'Shul': '2',
    'Kali': '2',
    'Rey': '4'
}

# A holdover from the original tabletop that serves no
# meaning here.
identity = {
    'Shul': 'Bryan Blodgett',
    'Kali': 'Anna Addison',
    'Rey': 'Nicko Scoops'
}

# Items can be found in resources dot py. Resource[0]
# is cash, healing[0] is a medkit, and weapon[0] is
# a knife.
items = {
    'Shul': [resource[0], healing[0]],
    'Kali': [resource[0], healing[0]],
    'Rey': [resource[0], weapon[0]]
}
# Shul's character sheet

char0 = {
  'Shul': {
        'Charm': charm['Shul'],
        'Stamina': charstamina['Shul'],
        'Identity': identity['Shul']
  }
}

# Kali's character sheet
char1 = {
    'Kali': {
        'Charm': charm['Kali'],
        'Stamina': charstamina['Kali'],
        'Identity': identity['Kali']
    }
}

# Rey's character sheet
char2 = {
  'Rey': {
    'Charm': charm['Rey'],
    'Stamina': charstamina['Rey'],
    'Identity': identity['Rey']
  }
}
