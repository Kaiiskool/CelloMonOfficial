# new game or not
print('''
   ______________________________
 / \                             \.
|   |                            |.
 \_ |   Welcome to Placeholder!  |.
    |                            |.
    |    would you like to start |.
    |     a new game? type "n".  |.
    |                            |.
    |     to continue from your  |.
    |     last save type "c".    |.
    |   _________________________|___
    |  /                            /.
    \_/____________________________/.
''')
answer = input().lower().strip()
if answer == "n":
    f = open("classes.py", "w")
    f.write('''
# code written by kaiiskool 


# player
class player():
    def __init__(self, **kwargs):
        ### items ###
        self.name = "placeholder"
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
    ''')
    f.close()
    from classes import player
    import time
    print('''
       ______________________________
     / \                             \.
    |   |                            |.
     \_ |   Welcome to Placeholder!  |.
        |                            |.
        |    written by kaiiskool    |.
        |     (press any key to      |.
        |      continue)             |.
        |                            |.
        |   _________________________|___  
        |  /                            /.
        \_/____________________________/.
    ''')

    player.name = input().lower().strip()
    print("you will now be sent to town01!")
    time.sleep(1)


elif answer == "c":
    import time
    print("you will now be sent to town01!")
    time.sleep(1)

import time
import random
import sys
# imports classes from file "classes.py"
from classes import player
from classes import boss01
from classes import item
from classes import basic_sword
from classes import god_sword
from classes import epic_dagger
from classes import meh_axe


while 1 == 1:
    # start
    while player.location == "town":
        player.lastlocation = "town"
        print('''
                                                                                           _ _                                  
                                                                                          ( Y )                                 
                                                                                           \ /                                  
                                                                                            \          /^\\                     
                                                                                              )       //^\\\\                   
                                                                                           (         //   \\\\                  
           _______________________________                                                   )      //     \\\\                 
           |  HP: ''',player.heath,'''                  |                                                  __     //       \\\\                
           |  MANA: ''', player.mana ,'''                |                                                 |=^|   //    _    \\\\               
           |-----------------------------|                                               __|= |__//    (+)    \\\\              
           |-----------------------------|                                              /LLLLLLL//      ~      \\\\             
           |_____________________________|                                             /LLLLLLL//               \\\\            
           | Your in town homia!         |                                            /LLLLLLL//                 \\\\           
           | what would you like to do?  |                                           /LLLLLLL//  |~[|]~| |~[|]~|  \\\\          
           |----------------------------------|                                      ^| [|] //   | [|] | | [|] |   \\\\         
           | type "h" to enter your house     |                                       | [|] ^|   |_[|]_| |_[|]_|   |^           
           | type "m" to enter the hospital   |                                    ___|______|                     |            
           | type "s" to enter the shop       |                                   /LLLLLLLLLL|_____________________|            
           | type "c" to travel down the path |                                  /LLLLLLLLLLL/LLLLLLLLLLLLLLLLLLLLLL\           
           | type "i" to check your inventory |                                 /LLLLLLLLLLL/LLLLLLLLLLLLLLLLLLLLLLLL\          
           | type "e" to enter the menu (save)|                                 ^||^^^^^^^^/LLLLLLLLLLLLLLLLLLLLLLLLLL\         
           |----------------------------------|                                  || |~[|]~|^^||^^^^^^^^^^||^|~[|]~|^||^^        
           |----------------------------------|                                  || | [|] |  ||  |~~~~|  || | [|] | ||           
           |----------------------------------|                                  || |_[|]_|  ||  | [] |  || |_[|]_| ||          
                                                                                 ||__________||  |   o|  ||_________||          
                                                                               .'||][][][][][||  | [] |  ||[][][][][||.'.       
                                                                              ."'||[][][][][]||_-`----'-_||][][][][]||"."       
                                                                            .(')^(.)(').( )'^@/-- -- - --\@( )'( ).(( )^(.)^    
                      ____________________________                         '( )^(`)'.(').( )@/-- -- - -- -\@ (.)'(.),( ).(').   
                      |     |       hospital     |                         ".'.'." ." '.". @/- - --- -- - -\@ '.".'.".'.".'."   
                      |   -----        _____     |                         ". '' ".".".'.'@/ - -- -- -- -- -\@".'..'".'."'.'.'  
                      |     |          |_|_|     |                        '.".".''.".''."@/ -- --- --- -- - -\@.".''.".''.".'". 
                      |________|||_______________|                                      _/                    \_                
            ____________      |   |         ____                            ___________/                        \_              
           /____________\\     |   |        /____\\                          |                                      |                
            |  0    0  |      |   |        _|__|_                          |                                      |              
            |____||____|      |   |        |shop|                         /         ______________________________|                                            
                |  | <_>      |   |         \\  /                         |        _|                                                
        ________|  |__|_______|   |_________|  |________________________/       _|                                                     
            *                                                                 _/                                                     
        _____________________________________________________________________/                                                     
        ''')
        answer = input().lower().strip()
        if answer == "h":
            pass

        elif answer == "m":
            pass

        elif answer == "s":
            player.location = "shop"

        elif answer == "c":
            pass

        elif answer == "i":
            pass

        elif answer == "e":
            player.location = "menu"

        else:
            print("thats not a valid option! please try again")
            time.sleep(2)
            pass


    while player.location == "menu":
        print('''
            _____________________________________________________________________________
            |  ______________________                _______________________________    |
            |  | Menu options:      |                |/  __  __                   \|    |
            |  |  to save game type |                |  |  \/  |                   |    |   
            |  |  "s".              |                |  | \  / | ___ _ __  _   _   |    |
            |  |  to exit menu type |                |  | |\/| |/ _ \ '_ \| | | |  |    |
            |  |  "exit"            |                |  | |  | |  __/ | | | |_| |  |    |
            |  ----------------------                |\ |_|  |_|\___|_| |_|\__,_| /|    |
            |                                        |_\_________________________/_|    |
            |                                                                           |
            |                                                                           |
            |___________________________________________________________________________|
        ''')
        answer = input().lower().strip()

        if answer == "s":
            with open("classes.py", "w") as f:
                f.write(f'''
# code written by kaiiskool
# player
class player():
    def __init__(self, **kwargs):
        ### items ###
        self.name = "{player.name}"
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
        self.location = "{player.location}"
        self.lastlocation = "{player.lastlocation}"
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
        self.luck = {basic_sword.luck}
        self.cost = {basic_sword.cost}
        
        
class god_sword():
    def __init__(self, **kwargs):
        self.damage = {god_sword.damage}
        self.durability = {god_sword.durability}
        self.luck = {god_sword.luck}
        self.cost = {god_sword.cost}


class epic_dagger():
    def __init__(self, **kwargs):
        self.damage = {epic_dagger.damage}
        self.durability = {epic_dagger.durability}
        self.luck = {epic_dagger.luck}
        self.cost = {epic_dagger.cost}


class meh_axe():
    def __init__(self, **kwargs):
        self.damage = {meh_axe.damage}
        self.durability = {meh_axe.durability}
        self.luck = {meh_axe.luck}
        self.cost = {meh_axe.cost}

# init
player = player()
boss01 = boss01()
item = item()
basic_sword = basic_sword()
god_sword = god_sword()
epic_dagger = epic_dagger()
meh_axe = meh_axe()

            ''')
            f.close()

        else:
            player.location = player.lastlocation


    while player.location == "shop":
        if player.exp < 25:
            print('''       
                ___________________________________________________________________________
                |  ______________________              _______________________________    |
                |  | items for sale:    |              |/    _____ _                \|    |
                |  |  snack = 25g       |              |   / ____| |                 |    | 
                |  |  heathpack = 50g   |              |  | (___ | |__   ___  _ __   |    |
                |  |  basic sword = 30g |              |   \___ \| '_ \ / _ \| '_ \  |    |
                |  ----------------------              |   ____) | | | | (_) | |_) | |    |
                |  ___________________________         |  |_____/|_| |_|\___/| .__/  |    |
                |  | you have ''', player.money, ''' gold     |          |                    | |     |    |
                |  ---------------------------         |\                    |_|    /|    |
                |  (type "exit" to leave shop)         |_\_________________________/_|    |
                |_________________________________________________________________________|
            ''')
            answer = input("merchant: what do you want to buy?(type what you want):").lower().strip()

            if answer == "snack":
                if player.money < item.snack:
                    print('insufficient funds')
                    time.sleep(2)
                elif player.money >= item.snack:
                    player.snack += 1
                    player.money -= item.snack
                    print("You now have", player.snack, "snack(s)")
                    time.sleep(2)

            elif answer == "heathpack":
                if player.money < item.heathpack:
                    print('insufficient funds')
                    time.sleep(2)
                elif player.money >= item.heathpack:
                    player.heathpack += 1
                    player.money -= item.heathpack
                    print("You now have", player.heathpack, "heathpacks(s)")
                    time.sleep(2)

            elif answer == "basic sword":
                if answer == "basic sword" and ["basic_sword"] not in player.items:
                    if player.money < basic_sword.cost:
                        print('insufficient funds')
                        time.sleep(2)
                    elif player.money >= basic_sword.cost:
                        player.items.append("basic_sword")
                        player.money -= basic_sword.cost
                        print("You now have a basic sword!")
                        time.sleep(2)
                else:
                    print("you already own a basic sword! come back when you need a new one.")
                    time.sleep(2)

            elif answer == "exit":
                print("leaving...")
                time.sleep(1)
                player.location = player.lastlocation

            else:
                print("thats not a valid option! please try again")
                time.sleep(2)
