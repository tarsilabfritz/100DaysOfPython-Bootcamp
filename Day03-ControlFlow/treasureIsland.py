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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

# Introduction
print("Welcome to the Treasure Island!\nYour mission is to find the treasure.\n")

# 1st step = Direction
direction = input("Do you want to go left or right? ").lower()  # The .lower() ensures the input is note case-sensitive

if direction == "left":
    # 2nd step = Swim or Wait
    want_to_swim = input("Now, do you want to swim or wait? ").lower()
    if want_to_swim == "wait":
        # 3rd step = Door Choice
        chosen_door = input("We are almost there! Now you just need to choose a door: Red, Blue or Yellow. ").lower()
        if chosen_door == "yellow":
            print("Congratulations! You found the treasure! You win!")
        elif chosen_door == "red":
            print("You opened the red door and were burned by fire! Game Over.")
        elif chosen_door == "blue":
            print("You opened the blue door and were eaten by beasts! Game Over.")
        else:
            print("That door doesn't exist! Game Over.")
    else:
        print("You were attacked by trout while swimming! Game Over.")
else:
    print("You fell into a hole! Game Over.")