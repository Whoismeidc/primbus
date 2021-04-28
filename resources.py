# Items for the RPG game.


class Explosive:
    def __init__(bomb, cost, dammod):
        bomb.dammod = dammod
        bomb.cost = cost


class Flashbang(Explosive):
    def __init__(flash, cost, dammod, accmod):
        super().__init__(cost, dammod)
        flash.accmod = accmod


class Decoy:
    def __init__(rope, escapechance):
        rope.escapechance = escapechance


class Healing:
    def __init__(medkit, healing):
        medkit.healing = healing


class Money:
    def __init__(stock, value):
        stock.value = value


class Armor:
    def __init__(vest, cost, armor):
        vest.cost = cost
        vest.armor = armor


class Weapon:
    def __init__(knife, cost, damage):
        knife.cost = cost
        knife.damage = damage
