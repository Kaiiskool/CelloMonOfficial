### this code is was writen by morgan lessard ###

### IMPORT'S ###
import time
import random
import sys
### IMPORT'S ###

### CLASSES ####

### PLAYER ###
class Player():
    def __init__(self, **kwargs):
        self.money = 100
        self.snack = 0
        self.in_shop = False  # or 0
        self.at_hotel = False
        self.Location = 0
        self.phase = 1  # to schedule phases of the game and use to see if the player did a quest or has progressed
        self.items = []
        self.Town_1 = 0
        self.Town_2 = 0
        self.Town_3 = 0
        self.Town_4 = 0
        self.Heath = 100
        self.Heathpack = 0
        ### .LOCATION LEGEND ###
            ### 0 = town 1 pre battle ###
            ### 1 = town 1 after battle ###
            ### 2 = route 1 ###
            ### 3 = town 2 pre battle ###
            ### 4 = town 2 after battle ###
            ### 5 = route 2 ###
            ### 6 = town 3 pre battle ###
            ### 7 = town 3 after battle ###
            ### 8 = route 3 ###
            ### 9 = town 4 pre battle ###
            ### 10 = town 4 after battle ###
            ### 11 = ending ###
        ### .LOCATION LEGEND ###
### PLAYER ###
### MAYOR 01 ###
class Mayor01():
    def __init__(self, **kwargs):
        self.Heath = 100
### MAYOR 01 ###

### SHOP ###
class item():
    def __init__(self):
        self.cost = 25
        self.cost2 = 50
### SHOP ###

### CLASSES ###
