
import time
import random
import sys
# imports classes from file "classes.py"
from classes import player
from classes import boss01
from classes import item
from classes import basic_sword

# intro
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
answer = input().lower().strip()
print("You will now be sent to town 1!")
time.sleep(2)

# start
while player.location == "town":
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
       |----------------------------------|                                 /LLLLLLLLLLL/LLLLLLLLLLLLLLLLLLLLLLLL\          
                                                                            ^||^^^^^^^^/LLLLLLLLLLLLLLLLLLLLLLLLLL\         
                                                                             || |~[|]~|^^||^^^^^^^^^^||^|~[|]~|^||^^        
                                                                             || | [|] |  ||  |~~~~|  || | [|] | ||           
                                                                             || |_[|]_|  ||  | [] |  || |_[|]_| ||          
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

    else:
        print("thats not a valid option! please try again")
        time.sleep(1)
        pass

while player.location == "shop":
    if player.exp < 25:
        print(
            '''
    
    
            ___________________________________________________________________________
            |  ______________________              _______________________________    |
            |  | items for sale:    |              |/    _____ _                \|    |
            |  |  snack = 25g       |              |   / ____| |                 |    | 
            |  |  heathpack = 50g   |              |  | (___ | |__   ___  _ __   |    |
            |  |  basic sword = 30g |              |   \___ \| '_ \ / _ \| '_ \  |    |
            |  ----------------------              |   ____) | | | | (_) | |_) | |    |
            |  ___________________________         |  |_____/|_| |_|\___/| .__/  |    |
            |  | you have ''', player.money, ''' gold     |         |                    | |      |    |
            |  ---------------------------         |\                   |_|     /|    |
            |  (type "exit" to leave shop)         |_\_________________________/_|    |
            |_________________________________________________________________________|


        ''')
        answer = input().lower().strip()

        if answer == "snack":
            pass

        elif answer == "heathpack":
            pass

        elif answer == "basic sword":
            pass