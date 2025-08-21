

from player import *

class items:
    def __init__(self, name, price, unlock,healthup,attackup,healup):
        self.name = name
        self.price = price
        self.unlock = unlock
        self.healthup = healthup
        self.attackup = attackup
        self.healup = healup
rico = items("Rico", 200, False,0,0,0)
health = items("Health Talisman",20, False,10,0,0)
attack = items("Attack Talisman",20, False,0,10,0)
heal = items("Heal Talisman",20, False,0,0,10)
shadow_of_the_realm = items("Shadow Of The Realm Talisman",100, False,20,20,20)

def shopfunc():

    while True:
        try:
            player_choice_item = int(input("What item do you want to buy?:\n1. Rico: 200 coins\n2. Health Talisman: 20 coins\n3. Attack Talisman: 20 coins\n4. Heal Talisman: 20 coins\n5. Shadow of the Realm Talisman: 100 coins"))
            if player_choice_item not in [1,2,3,4,5]:
                print("Invalid Input")
                continue
            if player_choice_item == 1:
                player_choice_item = rico
            elif player_choice_item == 2:
                player_choice_item = health
            elif player_choice_item == 3:
                player_choice_item = attack
            elif player_choice_item == 4:
                player_choice_item = heal
            elif player_choice_item == 5:
                player_choice_item = shadow_of_the_realm
            if player_choice_item.unlock == True:
                print("You have already unlocked this shop item")
                continue
            if player_choice_item.price > user.coins:
                print(f"You cant afford {player_choice_item.name}")
            elif player_choice_item.price <= user.coins:
                user.coins -= player_choice_item.price
                player_choice_item.unlock = True
        except Exception as e:
            print(f"Error occurred, error:{e}")
            continue


