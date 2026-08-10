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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
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
print("Welcome to Treasure Island\n")
print("Your mission is to find the treasure.\n")
choice1 = input('You\'re at a crossroad, where do you wanto to go? Type "Left" or "Right\n"')

if choice1 == "Left":
    choice2 = input('You\'ve come to a lake\n. '
                    'There is an island in the middlle of lake. '
                    'Type "wait" to wait for a boat.'
                    'Type "swin" to swin across\n').lower() #Continue in game
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharemd."
                        "There is house with 3 doors. Onde red, "
                        "one yellow and one blue "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It`s a room full of fire. Game over")
        elif choice3 == "yellow":
            print("You found the treasure. You win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. You lose!")
        else:
            print("You choose a door that doesn't exist. Game over")

    else:
        print("You got attacked by an a angry trout. Game over!")

else:
    print("You fall in to a hole. Game over")