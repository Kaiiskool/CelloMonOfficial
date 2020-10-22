from classes import player
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
''')