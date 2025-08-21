# Developed by Tanmay Raj
# Version: V1 | Structure Phase
# Om Ekadantaya Vidmahe, Vakratundaya Dhimahi, Tanno Danti Prachodayat



from combat_PLAY import *
from player import *
from shopmarket import *
from boss import *

import random

print("Rouge Terminal V1")

def DisplayStat():
    print(f"Your health:{player_cha.healthp}\n Boss Health:{player_boss.healthb}")

while True:
    try:
        player_choice_to_play= int(input("1.Play\n2.Shop\n3.Exit(Enter 1,2 or 3)"))
    except Exception as e:
        print(f"Invalid Input, Error: {e}")
        continue
    if player_choice_to_play not in [1,2,3]:
        print(f"Invalid Input")
        continue
    if player_choice_to_play == 1:
        pass
    elif player_choice_to_play == 2:
        shopfunc()
    elif player_choice_to_play == 3:
        exit()
    try:
        player_cha_input= input("Enter the character you want to play with(Mega or Rico M/R)").capitalize()
        if player_cha_input == 'M':
            mega.using = 'Y'


            print("Character: Mega")
            pass
        elif player_cha_input == 'R':
            if rico.unlock == True:
                ricop.using = 'Y'

                print("Character: Rico")
                pass
            elif rico.unlock == False:
                print("You have not unlocked Rico yet, going with Mega")
                mega.using = 'Y'
                pass
        else:
            print("Invalid Input")
            continue
    except Exception as e:
        print(f"Error {e}")
        continue

    try:
        player_choice_boss = int(input("Enter the boss you want to fight (Check the Readme for stats of each boss)"
                                       "\n Note: Enter 1,2 or 3 respective to the levels:"))
        if player_choice_boss not in [1,2,3]:
            print("Invalid Input")
            continue
        elif player_choice_boss == 1:
            Level1.usingb = 'Y'
            pass
        elif player_choice_boss == 2:
            Level2.usingb = 'Y'
            pass
        elif player_choice_boss == 3:
            Level3.usingb = 'Y'
            pass
        check()

        if Level1.usingb == 'Y' or Level2.usingb == 'Y' or Level3.usingb == 'Y':
            print("Successful")
        else:
            print("Failed")

    except Exception as e:
        print(f"Error {e}")
        continue

    break

while True:
    try_use_talisman = input("Do you want to use Talisman? (Y/N)").capitalize()
    try:
        if try_use_talisman not in ['Y', 'N']:
            print("Invalid Input")
            continue
        elif try_use_talisman == 'Y':
            use_talisman()
            pass
        elif try_use_talisman == 'N':
            print("Continuing..")
            pass
        else:
            print("Invalid Input")
            continue
    except Exception as e:
        print(f"Error {e}")
        continue
    print("Starting The Combat")
    break
while True:
    print(f"Your health:{player_cha.healthp}\n Boss Health:{player_boss.healthb}")
    choice_AI_list = [0,1]
    choice_AI = random.choice(choice_AI_list)

    if player_boss.healthb <= 0:
        print("Congratulations, you won, your rewards have been added!")
        user.coins += player_boss.rewardb
        break
    if player_cha.healthp <= 0:
        print("Aww, you lost, try again next time!")
        break
    player_choice = int(input("Enter the number of the move you want to play as provided in the readme):"))
    if player_choice not in [1,2]:
        print("Invalid Input")
        continue
    elif player_choice == 1:
        attack_player()
        pass
    elif player_choice == 2:
        heal_player()
        pass
    else:
        print("Invalid Input")
        continue
    if choice_AI == 1:
        attack_boss()
        continue
    elif choice_AI == 2:
        heal_boss()
        continue




