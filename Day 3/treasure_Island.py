#use 3 single quotes on both side to make a multiblock string
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction = input ("do you want to go left or right ? ").lower()
if direction == "left":
    swim_wait = input ("you have reached a large lake and you see an island with a cabin in the middle. do you swim or wait for a boat ? (swim/boat)").lower()
    if(swim_wait == "wait"):
        door = input("you finally reach the cabin. you have 3 doors to choose from: Red/Yellow Blue ").lower()
        if(door == "red"):
            print("You are burned by fire. Game over. Sad !")
        elif door == "blue":
            print("You are eaten by beasts. Game over. sad !")
        elif door == "yellow":
            print("You Win ! very nice !")
        else:
            print("need to choose a valid door, game over ")
    else:
        print ("you are attacked by a trout. Game Over. sad ! ")
else:
    print("You fall into a hole. Game Over. Sad ! ")