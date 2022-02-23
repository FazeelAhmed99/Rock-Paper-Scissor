#rock paper sicssor game with computer

import random
from traceback import print_tb

def game(you, bot_choice):
    if you == bot_choice:
        return None
    elif you == "r":
        if bot_choice == "s":
            return True
        elif bot_choice == "p":
            return False
    elif you == "p":
        if bot_choice == "s":
            return True
        elif bot_choice == "r":
            return False
    elif you == "s":
        if bot_choice == "p":
            return True
        elif bot_choice == "r":
            return False
    else:
        return "Error" 


bot_random = random.randint(1,3)

if bot_random == 1:
    bot_choice = "r"
elif bot_random == 2:
    bot_choice = "p"
else:
    bot_choice = "s"



you = input("Select either Rock(r), Paper(p) or Scissor(s): ")

ans = game(you, bot_choice)


if ans == None:
    print("The bot chooses " + bot_choice)
    print("It's a tie")
elif ans == True:
    print("The bot chooses " + bot_choice)
    print("You Win")
elif ans == False:
    print("The bot chooses " + bot_choice)
    print("You Lose")
elif ans == "Error":
    print("Invalid Selection")