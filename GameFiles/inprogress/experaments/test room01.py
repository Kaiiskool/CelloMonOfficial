from classes import player
from classes import item
import time


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


if answer == "god_sword" and ["god_sword"] not in player.items:
    if player.money < god_sword.cost:
        print('insufficient funds')
        time.sleep(2)
    elif player.money >= god_sword.cost:
        player.items.append("god_sword")
        player.money -= god_sword.cost
        print("You now have a god sword!")
        time.sleep(2)