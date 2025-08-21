

from boss import *
from player import *
from shopmarket import *
player_boss = Level1


def check():
    global player_boss
    try:
        if Level1.usingb == 'Y':

            player_boss = Level1
            print("f")
        elif Level2.usingb == 'Y':
            player_boss = Level2
            print("f")
        elif Level3.usingb == 'Y':
            player_boss = Level3
            print("f")
        else:
            print("None Found")
    except:
        print("Something went wrong")
        exit()
try:
    if mega.using == 'Y':
        player_cha = mega

    elif ricop.using == 'Y':
        player_cha = ricop
    else:
        player_cha = mega
except:
    print("Something went wrong")
    exit()
try:
    if Level1.usingb == 'Y':
        player_boss = Level1
    elif Level2.usingb == 'Y':
        player_boss = Level2
    elif Level3.usingb == 'Y':
        player_boss = Level3
    else:
        print("None Found")
except:
    print("Something went wrong")
    exit()
def attack_player():
    player_boss.healthb -= player_cha.attackp
    print("Boss: HOW DARE YOU!")
def attack_boss():
    player_cha.healthp -= player_boss.attackb
    print("Boss: Take THIS!")
def heal_player():
    if player_cha.healthp >= 100:
        print(f"You cant heal, your current health is {player_cha.healthp}!")
    else:
        player_cha.healthp += player_cha.healpp
        print(f"You have healed, current health: {player_cha.healthp}!")
def heal_boss():
    if player_boss.healthb >= 100:
        print(f"Boss tried to heal, but could not as his current HP is {player_boss.healthb}!")
    else:
        player_boss.healthb += player_boss.healb
        print(f"Boss has healed, current boss health: {player_boss.healthb}!")
        print("Boss: Try and Defeat me now!")
def use_talisman():
    tal_input = int(input("Which Talisman do you want to use?(Enter the name given in readme): "))
    while True:
        if tal_input not in [1,2,3,4]:
            print("Invalid input. Try again.")
            continue
        else:
            break
    while True:
        if tal_input == 1:
            tal = health
            pass
        elif tal_input == 2:
            tal = attack
            pass
        elif tal_input == 3:
            tal = heal
            pass
        elif tal_input == 4:
            tal = shadow_of_the_realm
            pass
        if tal.unlock == False:

            print("Either not owned, or not using RICO!")
            break
        #For Mega
        if player_cha == mega:
            mega.healthp = tal.healthup + mega.healthp
            mega.attackp = tal.attackup + mega.attackp
            mega.healpp = tal.healup + mega.healpp
            print(f"Using Talisman: {tal.name}")
            pass
        #For Rico
        elif player_cha == ricop:

            ricop.healthp += tal.healthup
            ricop.attackp += tal.attackup
            ricop.healpp += tal.healup
            print(f"Using Talisman: {tal.name}")
            pass
        else:
            print("Either not owned, or not using RICO!")
            pass