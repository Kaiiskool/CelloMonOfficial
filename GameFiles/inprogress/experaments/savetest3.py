from classes import player
from classes import boss01
from classes import item
from classes import basic_sword

with open("classes01.py", "w") as f:
    f.write(f'''
# code written by kaiiskool
# player
class player():
    def __init__(self, **kwargs):
        ### items ###
        self.money = {player.money}
        self.snack = {player.snack}
        self.healthpack = {player.heathpack}
        self.items = {player.items}
        ### items ###
        ### stats ###
        self.heath = {player.heath}
        self.mana = {player.mana}
        ### stats ###
        ### location ###
        self.location = {player.location}
        self.phase = {player.phase}
        ### location ###
        self.exp = {player.exp}
# boss 01
class boss01():
    def __init__(self, **kwargs):
        self.heath = {boss01.heath}
        self.attack = {boss01.attack}

# shop
class item():
    def __init__(self, **kwargs):
        self.snack = {item.snack}
        self.heathpack = {item.heathpack}

# swords
class basic_sword():
        def __init__(self, **kwargs):
            self.damage = {basic_sword.damage}
            self.durability = {basic_sword.durability}
            self.enchantments = {basic_sword.enchantments}

# init
player = player()
boss01 = boss01()
item = item()
basic_sword = basic_sword()

''')
f.close()
