
# code written by kaiiskool
# player
class player():
    def __init__(self, **kwargs):
        ### items ###
        self.name = "kai"
        self.money = 25
        self.snack = 1
        self.healthpack = 1
        self.items = []
        ### items ###
        ### stats ###
        self.heath = 100
        self.mana = 100
        ### stats ###
        ### location ###
        self.location = "menu"
        self.lastlocation = "town"
        self.phase = 1
        ### location ###
        self.exp = 0


# boss 01
class boss01():
    def __init__(self, **kwargs):
        self.heath = 100
        self.attack = 25


# shop
class item():
    def __init__(self, **kwargs):
        self.snack = 25
        self.heathpack = 50


# swords
class basic_sword():
    def __init__(self, **kwargs):
        self.damage = 15
        self.durability = 750
        self.luck = 85
        self.cost = 35


class god_sword():
    def __init__(self, **kwargs):
        self.damage = 1000
        self.durability = 1500000
        self.luck = 90
        self.cost = 100000


class epic_dagger():
    def __init__(self, **kwargs):
        self.damage = 75
        self.durability = 750
        self.luck = 15
        self.cost = 175


class meh_axe():
    def __init__(self, **kwargs):
        self.damage = 10
        self.durability = 300
        self.luck = 75
        self.cost = 30


# init
player = player()
boss01 = boss01()
item = item()
basic_sword = basic_sword()
god_sword = god_sword()
epic_dagger = epic_dagger()
meh_axe = meh_axe()
            