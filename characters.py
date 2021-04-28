# Defense is the chance to cause a miss, from 0 to 100.
# This is for flashbangs.
# Armor decides how much less damage someone takes from
# an attack, addition wise.


class Character:
    def __init__(char, stamina, defense):
        char.health = 5 + stamina
        char.armor = 0
        char.inventory = []
        char.defense = 0

# The charm is the player's special ability.


class Player(Character):
    def __init__(player, stamina, defense, charm):
        super().__init__(stamina, defense)
        player.charm = charm
