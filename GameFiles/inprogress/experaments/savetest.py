
# code written by kaiiskool


# player
class player():
    def __init__(self, **kwargs):
        ### items ###
        self.money = 100
        self.snack = 0
        self.heathpack = 0
        self.items = []
        ### items ###
        ### stats ###
        self.heath = 100
        self.mana = 100
        ### stats ###
        ### location ###
        self.location = "town"
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
            self.enchantments = 0

# init
player = player()
boss01 = boss01()
item = item()
basic_sword = basic_sword()

