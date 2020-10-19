### this code is was writen by morgan lessard ###
### it also had help from members of the tech with tim discord server ###

### IMPORT'S ###
import time
import random
import sys
### IMPORT'S ###

### CLASSES ####

### PLAYER ###
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

### PLAYER ###
### boss 01 ###
class boss01():
    def __init__(self, **kwargs):
        self.heath = 100
        self.attack = 25
### boss 01 ###

### SHOP ###
class item():
    def __init__(self, **kwargs):
        self.snack = 25
        self.heathpack = 50
### SHOP ###

### CLASSES ###

### INIT ###

player = player()
boss01 = boss01()
item = item()
### INIT ###

########################################################################################################################
########################################################################################################################
########################################################################################################################
