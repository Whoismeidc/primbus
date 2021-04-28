# Items for the RPG game.


class Explosive:
    def __init__(bomb, cost, dammod):
        '''Attributes for bombs.'''
        bomb.dammod = dammod
        bomb.cost = cost


class Flashbang(Explosive):
    def __init__(flash, cost, dammod, accmod):
        '''Attributes for flashbangs.'''
        super().__init__(cost, dammod)
        flash.accmod = accmod


class Decoy:
    def __init__(rope, escapechance):
        '''Attributes for decoys.'''
        rope.escapechance = escapechance


class Healing:
    def __init__(medkit, healing):
        '''Attributes for healing items.'''
        medkit.healing = healing


class Money:
    def __init__(stock, value):
        '''Attributes for money items.'''
        stock.value = value


class Armor:
    def __init__(vest, cost, armor):
        '''Attributes for armor items.'''
        vest.cost = cost
        vest.armor = armor


class Weapon:
    def __init__(knife, cost, damage):
        '''Attributes for weapons.'''
        knife.cost = cost
        knife.damage = damage
