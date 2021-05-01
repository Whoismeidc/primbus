from tabulate import tabulate
from random import *

# Python didn't play nice with importing,
# so the main data is all compiled here,
# separated between characters, combat, and environments.

damage = 0
armor = 0
health = 0
activeenemy = 0
charm = 0
cash = 0
dammod = 1
defense = 0
fighton = 0
activeplayer = 0
shop_on = 0

# Characters

# Defense is the chance to cause a miss, from 0 to 100.
# This is for flashbangs.
# Armor decides how much less damage someone takes from
# an attack, addition wise.


class Character:
    '''Attributes for characters.'''
    def __init__(char, name, stamina, attack):
        char.health = 5 + stamina
        char.name = name
        char.armor = 0
        char.inventory = []
        char.attack = attack
        char.currhealth = 5 + stamina

    def check_inventory(char):
        '''Prints out inventory.'''
        print("This is what you have in your inventory:")
        print(char.inventory)

    def change_health(char, change):
        '''For use when healed or attacked.'''
        if char.currhealth + change >= char.health:
            char.currhealth = char.health
        else:
            char.currhealth = char.currhealth + change

    def apply_armor(char, change):
        '''Sets armor to character.'''
        char.armor = change

    def apply_weapon(char, change):
        '''Sets damage to character.'''
        char.attack = change

    def set_damage(char):
        '''Sets global damage for attacking with.'''
        damage = char.attack
        return damage

    def set_armor(char):
        '''Sets global armor for defending with.'''
        armor = char.armor
        return armor

    def set_defense(char, *addition):
        '''Sets global evasion for dodging with.'''
        defense = char.defense + addition
        return defense

    def show_health(char):
        '''Checks health in a fight to see if it needs
        to end'''
        health = char.currhealth
        print(f"The defender has {health} health.")
        return health

    def show_stats(char):
        '''Prints player stats'''
        print("These are your stats:")
        print(f"Health: {str(char.health)}")
        print(f"Armor: {str(char.armor)}")
        print(f"Current Health: {str(char.currhealth)}")
        print(f"Charm: {str(char.charm)}")

    def set_charm(char):
        '''Sets player charm for use in overworld'''
        charm = char.charm
        return charm

    def remove_item(char, item):
        char.inventory.remove(str(item))

    def check_health(char):
        health = char.health
        return health


class Player(Character):
    '''Attributes for player character. Charms are special abilities.'''
    def __init__(player, name, stamina, attack, defense, charm):
        super().__init__(name, stamina, attack)
        player.charm = charm
        player.defense = defense

    def wear_weapon(player, attack):
        '''Changes player weapon to attack value.
            Derived from shop.'''
        global cash
        global shop_on
        if cash >= attack:
            player.attack = attack
            cash = cash - attack
            print("Okay, your damage is set.")
            shop_on = 0
            return shop_on
        else:
            print("Oops, you can't afford that.")

    def wear_armor(player, armor):
        '''Changes player armor to armor value.
            Derived from shop.'''
        global cash
        global shop_on
        if cash >= armor:
            player.armor = armor
            cash = cash - armor
            print("Okay, your armor is set.")
            shop_on = 0
        else:
            print("Oops, you can't afford that.")

    def add_inv(player, inventory, *quality):
        '''Adds item to inventory. Derived from shop.'''
        global cash
        global shop_on
        global charm
        # I've created three levels of medkit.
        if inventory == 'medkit':
            if quality == 1:
                if 'Medkit' not in player.inventory:
                    cash = cash - quality
                    player.inventory.append('Medkit')
                    print("Okay, it's in your inventory.")
                    shop_on = 0
                    # If you're Kali, you get a refund.
                    if charm == 'Data Wizard':
                        cash = cash + 1
                else:
                    print("Oops! You already have that!")
            elif quality == 2:
                if 'potion' not in player.inventory:
                    cash = cash - quality
                    player.inventory.append('{p}otion')
                    print("Okay, it's in your inventory.")
                    shop_on = 0
                    # If you're Kali, you get a refund.
                    if charm == 'Data Wizard':
                        cash = cash + 1
                else:
                    print("Oops! You already have that!")
            elif quality == 3:
                if 'ambrosia' not in player.inventory:
                    cash = cash - quality
                    player.inventory.append('ambrosia')
                    print("Okay, it's in your inventory.")
                    shop_on = 0
                    # If you're Kali, you get a refund.
                    if charm == 'Data Wizard':
                        cash = cash + 1
                else:
                    print("Oops! You already have that!")
        else:
            if inventory not in player.inventory:
                player.inventory.append(str(inventory))
                shop_on = 0
                print("Okay, it's in your inventory.")
                # If you're Kali, you pay nothing.
                if charm != 'Data Wizard':
                    cash = cash - 1

            else:
                print("Oops! You already have that!")

    def medkit_use(player, item):
        '''Expends medkit to give player health.'''
        if item == 'Medkit':
            player.healing = player.currhealth // 3
            player.change_health(player.healing)
            print(f"You healed {player.healing} health.")
            player.remove_item('medkit')
        elif item == 'potion':
            player.healing = player.health // 1.5
            player.change_health(player.healing)
            print(f"You healed {player.healing} health.")
            player.remove_item('potion')
        elif item == 'ambrosia':
            player.healing = player.health
            player.change_health(player.healing)
            print(f"You healed {player.healing} health.")
            player.remove_item('ambrosia')

    def set_charm(player):
        '''Sets player charm to global value for use.'''
        global charm
        charm = player.charm

# Created various monster types.
goon = Character('goon', 2, 2)
monster = Character('monster', 6, 3)
boss = Character('boss', 10, 4)
overlord = Character('overlord', 14, 5)

# Created various player types.
shul = Player('Shul', 4, 1, 0, 'Kensei')
kali = Player('Kali', 2, 1, 1, 'Data Wizard')
rey = Player('Rey', 4, 1, 0, 'Barrier Jacket')


def startplayer():
    # Decides which character the player uses.
    global shul
    global kali
    global rey
    global activeplayer
    global charm
    while charm == 0:
        # Player becomes Shul, Kali, or Rey.
        candidates = ['Shul', 'Kali', 'Rey']
        print("Who are you playing?")
        choice = input("Shul, Kali, or Rey?")
        if choice.title() == 'Shul':
            activeplayer = shul
            shul.set_charm()
        elif choice.title() == 'Kali':
            activeplayer = kali
            kali.set_charm()
        elif choice.title() == 'Rey':
            activeplayer = rey
            rey.set_charm()
        else:
            print("I don't understand.")

startplayer()

# Combat
# Similar code can be found in oldcombat, but classes
# don't mesh well with other classes.


def start_fight(combat2):
    '''Transitions to fight phase.'''
    global defense
    global activeplayer
    global dammod
    global fighton
    fighton = 1
    print(str(activeplayer))
    while fighton == 1:
        print("What would you like to do?")
        possibleitems = [
                'Medkit',
                'Potion',
                'Ambrosia',
                'Flashbang',
                'Bomb',
                'Rope',
            ]
        choice = input("Fight, or inventory?")
        if choice.title() == 'Fight':
            # Active player fights the goon in combat2.
            attack(combat2)
        elif choice.title() == 'Inventory':
            # Checks inventory.
            activeplayer.check_inventory()
        elif choice.title() in possibleitems:
            # Uses item in inventory.
            item_use(str(choice.title()))
        elif choice.title() == 'Cheat':
            # Ends the fight immediately.
            end_fight(combat2)
        else:
            print("I don't understand.")


def attack(combat2):
    global charm
    global defense
    global dammod
    global activeplayer
    # The player attacks.
    print(f"You attack!")
    activeplayer.set_damage()
    # If you're Shul, you do one extra base damage.
    if charm == 'Kensei':
        combat2.change_health(-(damage + 1) * dammod)
    else:
        combat2.change_health(-(damage) * dammod)
    check_health(combat2)
    print("The " + str(combat2) + " strikes!")
    activeplayer.set_armor()
    combat2.set_damage()
    if damage - armor >= 0:
        # Enemy has a 1 in defense minus 2 chance of missing.
        roll = randint(-1, defense)
        # If you're Rey, you take one less damage.
        if roll <= 1:
            if charm == 'Barrier Jacket':
                activeplayer.change_health(-(damage - 1))
                check_health(activeplayer, combat2)
            else:
                activeplayer.change_health(-(damage))
                check_health(activeplayer, combat2)

        else:
            print("They missed!")
    else:
        print("They did no damage.")


def item_use(item):
    global activeplayer
    if item == 'Medkit':
        activeplayer.check_health()
        activeplayer.change_health(health // 3)
        print(f"You healed {health // 3} health.")
        activeplayer.remove_item('Medkit')

    elif item == 'Potion':
        activeplayer.check_health()
        activeplayer.change_health(health // 1.5)
        print(f"You healed {health // 1.5} health.")
    elif item == 'Ambrosia':
        activeplayer.check_health()
        activeplayer.change_health(health)
        print(f"You healed {health} health.")

    elif item == 'Flashbang':
        activeplayer.set_defense(2)
        print("You threw a flashbang.")
        print("They're more likely to miss!")

    elif item == 'Bomb':
        global dammod
        dammod = 2
        print("You threw a bomb.")
        print("You've opened them up to damage!")
        activeplayer.remove_item()
        return dammod
    elif item == 'Rope':
        print("You're out of there.")
        end_fight(1)


def check_health(combat2):
    '''Checks if someone should be dead.'''
    global activeplayer
    activeplayer.show_health()
    if health > 0:
        combat2.show_health()
        if health <= 0:
            end_fight(combat2)
    else:
        loss()


def end_fight(combat2, *escape):
    '''If the enemy is dead, transition back to
        map mode.'''
    global fighton
    global dammod
    global damage
    global defense
    global activeplayer
    global cash
    fighton = 0
    dammod = 1
    activeplayer.set_defense()
    combat2.set_damage()

    # Player is rewarded based on the damage the enemy
    # does. If the enemy does five damage, they're the
    # boss and the player should win.
    if escape == 1:
        cash = cash
    elif damage == 2:
        cash = cash + 3
        print("You win! You get 2 cash.")
    elif damage == 3:
        cash = cash + 5
    elif damage == 4:
        cash = cash + 10
    elif damage == 5:
        victory()


def victory():
    # Victory text.
    nice = True
    while nice is True:
        print("You win!")
        break


def loss():
    # Loss text.
    nice = True
    while nice is True:
        print("Game over.")
        break

# Environments


class FriendlyBusiness:
    '''Attributes for businesses.'''
    def __init__(store, name):
        store.items = []
        store.name = name

    def give_items(store, *items):
        # Activates store mode.
        # Once something is bought, player is kicked out.
        shop_on = 1
        print(f"Welcome to {store.name}!")
        print("Is there anything you'd like to buy?")
        print("A weapon, armor, medkit, or item?")
        print("By items, we mean a flashbang, bomb,")
        print("and rope.")
        store.items = ['Bomb', 'Flashbang', 'Rope']
        while shop.on == 1:
            shopchoice = input("Or quit?")
            if shopchoice.title() == 'Weapon':
                store.give_weapon()
            elif shopchoice.title() == 'Armor':
                store.give_armor()
            elif shopchoice.title() == 'Medkit':
                store.addinv()
            elif shopchoice.title() in store.items:
                store.addinv()
            elif shopchoice.title() == 'Quit':
                print("Okay, then.")
            else:
                print("I don't understand.")

    def give_weapon(store):
        # Decides quality of weapon.
        # Make a typo to return to the front page.
        print("What level? 1, 2, or 3?")
        goodnums = [1, 2, 3]
        weapchoice = input()
        if weapchoice in str(goodnums):
            activeplayer.wear_weapon(int(weapchoice))
        else:
            print("I don't understand.")

    def give_armor(store):
        # Decides quality of armor.
        # Make a typo to return to the front page.
        print("What level? 1, 2, or 3?")
        goodnums = [1, 2, 3]
        armchoice = input()
        if armchoice in str(goodnums):
            activeplayer.wear_armor(int(armchoice))
        else:
            print("I don't understand.")

    def give_medkit(store):
        # Decides quality of medkit.
        # Make a typo to return to the front page.
        global cash
        print("What level? 1, 2, or 3?")
        goodnums = [1, 2, 3]
        medchoice = input()
        if medchoice in str(goodnums):
            if medchoice >= cash:
                print("Oops! You can't afford that.")
            else:
                activecharacter.add_inv(int(medchoice))
        else:
            print("I don't understand.")

shop = FriendlyBusiness('Walmart')


class FriendlyNeighborhood:
    '''Attributes for money tiles.'''
    def __init__(home):
        home.money = []

    def add_money(home, money):
        global cash
        cash = cash + money
        print("Welcome to the neighbourhood!")
        print("You got 1 cash.")
        print(f"You have {cash} cash.")
        return cash

# Create a money tile
base = FriendlyNeighborhood()


class Tile:
    def __init__(tile, name):
        '''Blank tiles that waste the player's time.'''
        tile.name = name


class HostileTile(Tile):
    def __init__(tile, name, enemy):
        '''Tile that spawns enemies.'''
        super().__init__(name)
        tile.enemy = enemy


class Map:
    # Row is how wide the map is. Column is how tall the
    # map is. The coordinate starts at the last tile.
    def __init__(scroll, row, column):
        '''Attributes for maps.'''
        scroll.row = row
        scroll.column = column
        scroll.tiles = []
        scroll.coord = scroll.row * scroll.column - 1
        scroll.playertile = 0
        scroll.max = scroll.row * scroll.column

    def make_map(scroll, tile):
        '''Adds tiles named after the tile name.'''
        for i in range(scroll.row):
            for i in range(scroll.column):
                scroll.tiles.append(tile.name)

    def replace_tile(scroll, tile, beats, lastindex):
        '''Replaces tiles with meaningful ones.'''
        for spot in range(0, int(lastindex), beats):
            del scroll.tiles[spot]
            scroll.tiles.insert(spot, tile.name)

    def move_map(scroll, submap, firstindex, lastindex):
        '''Places sections of map in a list for use in an
        array.'''
        for spot in range(firstindex, lastindex):
            submap.insert(spot, scroll.tiles[spot])

    def basic_print_map(scroll):
        print(scroll.tiles)

    def check_tile(scroll):
        '''Check the name of the tile the player is on.'''
        print(scroll.tiles[scroll.coord])

    def adjust_place(scroll, direction):
        '''Removes the tile player was on, replaces it
        with a tile the player was not on, and indicates
        their next position.'''
        del scroll.tiles[scroll.coord]
        scroll.tiles.insert(scroll.coord,
                            scroll.playertile)
        if direction.title() == 'Up':
            if scroll.coord - 3 <= 0:
                print("You waste time going nowhere.")
            else:
                scroll.coord = scroll.coord - 3
        elif direction.title() == 'Down':
            if scroll.coord + 3 >= scroll.max:
                print("You waste time going nowhere.")
            else:
                scroll.coord = scroll.coord + 3
        elif direction.title() == 'Left':
            if scroll.coord - 1 <= 0:
                print("You waste time going nowhere.")
            else:
                scroll.coord = scroll.coord - 1
        elif direction.title() == 'Right':
            if scroll.coord + 1 >= scroll.max:
                print("You waste time going nowhere.")
            else:
                scroll.coord = scroll.coord + 1

    def move_place(scroll):
        '''Puts the player on the next position.'''
        scroll.playertile = scroll.tiles.pop(scroll.coord)
        scroll.tiles.insert(scroll.coord,
                            f"{scroll.playertile}*")
        return goodmap

    def establish_tile(scroll):
        '''Creates the player tile.'''
        scroll.playertile = scroll.tiles[scroll.coord]

# Creates a 3 by 8 map of open field.

bigmap = Map(3, 8)

field = Tile('Open Field')

bigmap.make_map(field)

# Replaces every five tiles with bad neighbourhoods.
slum = HostileTile('Bad Neighbourhood', 'goon')
shoptile = Tile('Good Business')
hood = Tile('Good Hood')
bigmap.replace_tile(slum, 5, 24)
bigmap.replace_tile(shoptile, 9, 24)
bigmap.replace_tile(hood, 13, 24)

# Replaces start and end of map with Start and End tiles.
start = Tile('Start')

end = HostileTile('End', 'Boss')

bigmap.replace_tile(start, 23, 24)
bigmap.replace_tile(end, 24, 24)


def print_map(scroll):
    '''Prints the map neatly, according to the list array.
    Because there are eight maps, each of which has 3
    tiles, it prints a 3 by 8.'''
    print(tabulate(scroll, tablefmt="plain"))
    print("\n")

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


def update_map():
    '''Copies the above process.'''
    global base
    global shop
    global activeplayer
    global goon
    global boss

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
    # If player is standing on end tile, they fight
    # the boss.
    if 'End*' in map1:
        print("It's the boss.")
        start_fight(boss)
    # If player stands on a Good Hood, they get a dollar.
    elif 'Good Hood*' in map5:
        base.add_money(1)
    elif 'Bad Neighbourhood*' in map2:
        # I wanted to refer to goodmap instead of each
        # individual map, but Python is lazy.
        print("You've been attacked by a goon!")
        start_fight(goon)
    elif 'Bad Neighbourhood*' in map4:
        print("You've been attacked by a goon!")
        start_fight(goon)
    elif 'Bad Neighbourhood*' in map6:
        print("You've been attacked by a goon!")
        start_fight(goon)
    elif 'Bad Neighbourhood*' in map7:
        print("You've been attacked by a goon!")
        start_fight(goon)
    elif 'Friendly Business*' in map4:
        shop.give_items()
    elif 'Friendly Business*' in map7:
        shop.give_items()
