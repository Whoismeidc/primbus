from resources import *

# The enemy list is a template that does nothing.
enemy = ['Goon', 'Monster', 'Boss', 'Overlord']

# Like characters, this decides health.

enstamina = {
    'Goon': '2',
    'Monster': '6',
    'Boss': '10',
    'Overlord': '14'
}

# Weapons can be found in resources dot py. The higher
# the index, the better.

enitems = {
  'Goon': weapon[0],
  'Monster': weapon[1],
  'Boss': weapon[2],
  'Overlord': weapon[3]
}

# Character sheets, like characters dot py.

goon = {
  'stamina': enstamina['Goon'],
  'item': enitems['Goon'],
}

monster = {
  'stamina': enstamina['Monster'],
  'item': enitems['Monster'],
}

boss = {
  'stamina': enstamina['Boss'],
  'item': enitems['Boss'],
}

overlord = {
  'stamina': enstamina['Overlord'],
  'item': enitems['Overlord'],
}
