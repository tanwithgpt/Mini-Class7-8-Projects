import random
import time


class player_bowler:
    def __init__(self,name,skill,overs_b,overs_p):
        self.vskill =  skill
        self.oversb = overs_b
        self.oversp = overs_p
        self.name = name
oc = 0
bc = 0
ovp = 0
wp = 0
wai = 0
runs_player = 0
runs_AI = 0

def hit_ai(b):
    global bc
    global wai
    global runs_AI
    global runs_player
    global wp
    if b <= 5:
        chance = ['F','P','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F','F','F']
            out_chance = random.choice(chance_out)
            if out_chance == 'F':
                

                bc += 1
            if out_chance == 'P':
                bc = bc + 1

                wp+= 1
        elif ot == 'P':
            bc = bc + 1

            runs_player += 4
    elif b > 5 and b < 9:
        chance = ['F','P','F','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F',]
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':

                bc = bc + 1
            if chance_out_chance == 'P':
                bc = bc + 1
                
                wai += 1
        if ot == 'P':
            bc = bc + 1

            runs_AI += 4
    elif b >= 9 or b == 10:
        chance = ['F','P','F','F','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F',]
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':

                bc = bc + 1
            if chance_out_chance == 'P':
                bc = bc + 1

                wai = wai + 1
        elif ot == 'P':
            bc = bc + 1
            
            runs_AI += 4

def hit_p(b):
    global bc
    global wai
    global runs_AI
    global runs_player
    global wp
    if b <= 5:
        chance = ['F','P','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F','F','F']
            out_chance = random.choice(chance_out)
            if out_chance == 'F':

                bc += 1
            if out_chance == 'P':
                bc = bc + 1

                wp+= 1
        elif ot == 'P':
            bc = bc + 1

            runs_player += 4
    elif b > 5 and b < 9:
        chance = ['F','P','F','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F',]
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':

                bc = bc + 1
            if chance_out_chance == 'P':
                bc = bc + 1

                wp = wp + 1
        if ot == 'P':
            bc = bc + 1

            runs_player += 4
    elif b >= 9 or b == 10:
        chance = ['F','P','F','F','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F',]
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':


                bc = bc + 1
            if chance_out_chance == 'P':

                bc = bc + 1
                wp = wp + 1
        elif ot == 'P':
            bc = bc + 1

            runs_player += 4
def slog_p(b):
    global bc
    global wai
    global runs_AI
    global runs_player
    global wp
    if b <= 5:
        chance = ['F','P','F','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F','F']
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':

                bc = bc + 1
            elif chance_out_chance == 'P':

                bc = bc + 1
                wp = wp + 1
        elif ot == 'P':
            bc = bc + 1

            runs_player += 6
    elif b > 5 and b < 9:
        chance = ['F','P','F','F','F','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F','F',]
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':
                
                bc = bc + 1
            elif chance_out_chance == 'P':

                bc = bc + 1
                wp = wp + 1
        if ot == 'P':
            bc = bc + 1

            runs_player += 6
    elif b >= 9 or b == 10:
        chance = ['F','P','F','F','F','F','F','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F']
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':
                
                bc = bc + 1
            elif chance_out_chance == 'P':

                bc = bc + 1
                wp = wp + 1
        elif ot == 'P':

            bc = bc + 1
            runs_player += 6
def slog_c(b):
    global bc
    global wai
    global runs_AI
    global runs_player
    global wp
    if b <= 5:
        chance = ['F','P','F','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F','F']
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':
                
                bc = bc + 1
            elif chance_out_chance == 'P':
                
                bc = bc + 1
                wai = wai + 1
        elif ot == 'P':
            bc = bc + 1

            runs_AI += 6
    elif b > 5 and b < 9:
        chance = ['F','P','F','F','F','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F','F',]
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':
                
                bc = bc + 1
            elif chance_out_chance == 'P':
                
                bc = bc + 1
                wai = wai + 1
        if ot == 'P':
            bc = bc + 1

            runs_AI += 6
    elif b >= 9 or b == 10:
        chance = ['F','P','F','F','F','F','F','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F']
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':
                
                bc = bc + 1
            elif chance_out_chance == 'P':
                
                wai = wai + 1
                bc = bc + 1
        elif ot == 'P':

            bc = bc + 1
            runs_AI += 6
def defend_p(b):
    global bc
    global wai
    global runs_AI
    global runs_player
    global wp
    if b <= 5:
        chance = ['F','P','P','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F','F','F','F']
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':
                
                bc = bc + 1
            elif chance_out_chance == 'P':

                wp = wp + 1
                bc = bc + 1
        if ot == 'P':
            bc = bc + 1

            runs_c = [1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3]
            runs_sc = random.choice(runs_c)
            runs_player += runs_sc
    if b > 5 and b < 9:
        chance = ['F','P','F','P','P','P','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F','F','F','F']
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':
                
                bc = bc + 1
            elif chance_out_chance == 'P':

                wp = wp + 1
                bc = bc + 1
        elif ot == 'P':

            runs_c = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
            runs_sc = random.choice(runs_c)
            runs_player += runs_sc
    if b >= 9 or b == 10:
        chance = ['F','P','F','F','P','P','P',]
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F','F','F','F','F']
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':
                
                bc = bc + 1
            elif chance_out_chance == 'P':

                wp = wp + 1
                bc = bc + 1
        elif ot == 'P':

            runs_c = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
            runs_sc = random.choice(runs_c)
            runs_player += runs_sc
            bc = bc + 1





def defend_ai(b):
    global bc
    global wai
    global runs_AI
    global runs_player
    global wp
    if b <= 5:
        chance = ['F','P','P','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F','F','F','F']
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':
                
                bc = bc + 1
            elif chance_out_chance == 'P':
                
                wai = wai + 1
                bc = bc + 1
        if ot == 'P':
            bc = bc + 1

            runs_c = [1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3]
            runs_sc = random.choice(runs_c)
            runs_AI += runs_sc
    if b > 5 and b < 9:
        chance = ['F','P','F','P','P','P','F']
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F','F','F','F']
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':
                
                bc = bc + 1
            elif chance_out_chance == 'P':
                
                wai = wai + 1
                bc = bc + 1
        elif ot == 'P':

            runs_c = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
            runs_sc = random.choice(runs_c)
            runs_AI += runs_sc
    if b >= 9 or b == 10:
        chance = ['F','P','F','F','P','P','P',]
        ot = random.choice(chance)
        if ot == 'F':
            chance_out = ['F','P','F','F','F','F','F','F']
            chance_out_chance = random.choice(chance_out)
            if chance_out_chance == 'F':
                
                bc = bc + 1
            elif chance_out_chance == 'P':
                
                wai = wai + 1
                bc = bc + 1
        elif ot == 'P':

            runs_c = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
            runs_sc = random.choice(runs_c)
            runs_AI += runs_sc
            bc = bc + 1



Hardik = player_bowler("Hardik",7,0,1)
Axar = player_bowler("Axar",8,0,1)
Jadeja = player_bowler("Jadeja",8,0,1)
Arshdeep = player_bowler("Arshdeep",8,0,1)
Bumrah = player_bowler("Bumrah",9,0,1)
Kuldeep = player_bowler("Kuldeep",8,0,1)
Maxwell = player_bowler("Maxwell",6,0,1)
Green = player_bowler("Green",6,0,1)
Ben = player_bowler("Ben",8,0,1)
Ellis = player_bowler("Ellis",9,0,1)
Kunheman = player_bowler("Kunheman",8,0,1)
Zampa = player_bowler("Zampa ",9,0,1)
au_bowler = [Maxwell,Green,Ben,Ellis,Kunheman,Zampa]

ind_bowler = [Hardik,Axar,Jadeja,Arshdeep,Bumrah,Kuldeep]
while True:
    try:
        overs = int(input("Enter the number of overs(5 or 10)"))
        if overs == 5 or overs == 10:
            break
        else:
            print("Invalid input")
            continue
    except ValueError:
        print("Please enter a valid input.")
        continue
while True:
    try:
        print("Team India:\n"
              "Rohit Sharma\n"
                "Virat Kohli\n" 
                "Rishab Pant\n"	
                "Surya Kumar Yadav\n"
                "Rinku Singh\n"
                "Hardik Pandya\n"
                "Axar Patel\n"
                "Ravindra Jadeja\n"
                "Arshdeep Singh\n"
                "Jasprit Bumrah\n"
                "Kuldeep Yadav\n")
        print("Australlia:\n"
              "Glenn Maxwell\n"   
                "Mitchell Marsh\n"
                "Josh Inglis\n"
                "Cameron Green\n"  
                "Tim David\n"
                "Mitchell Owen\n" 
                "Cooper Connolly\n" 
                "Ben Dwarshuis\n"
                "Nathan Ellis\n"
                "Matthew Kuhnemann\n"
                "Adam Zampa\n")
        team = input("Enter the team name(A or I(Australia or India))").capitalize()
        if team == "A" or team == "I":
            break
        else:
            print("Invalid input")
    except:
        print("Please enter a valid input.")
        continue
user_first = 'B'
while True:
    try:
        toss = ['H','T']
        toss_value = input("Enter the toss(H or T)").capitalize()
        if toss_value == "H" or toss_value == "T":
            toss_r = random.choice(toss)
            if toss_value == toss_r:
               choice = input("Enter Batting or Bowling(B or BO)").upper()
               if choice == 'B' or choice == 'BO':
                   pass
               else:
                   print("Invalid input, you'll have to do toss again.")
                   continue
               if choice == 'B':
                    print("You are batting first")
                    break
               elif choice == 'BO':
                   print("You are bowling first")
                   user_first = 'BO'
                   break
            if toss_value != toss_r:
                ai_choice_list = ['B', 'BO']
                ai_choice = random.choice(ai_choice_list)
                if ai_choice == 'B':
                    user_first = 'BO'
                    print("You are bowling first, AI won the toss")
                elif ai_choice == 'BO':
                    user_first = 'B'
                    print("You are batting first, AI won the toss")
                break
        else:
            print("Invalid input, you'll have to do toss again.")
            continue
    except:
        print("Please enter a valid input.")
        continue
if overs == 10:
    player_bowler.oversp = 2
while True:
    if runs_AI > 0 and runs_player == runs_AI + 1:
        print("You won!, closing in 5 seconds")
        time.sleep(5)
        exit()
    if runs_player > 0 and runs_AI == runs_player + 1:
        print("You lost, try again by restarting the program, closing in 5 seconds")
        time.sleep(5)
        exit()
    if user_first == 'B' and oc >= overs or wp == 10:
        user_first = 'BO'
        oc = 0
        bc = 0
    if user_first == 'BO' and oc >= overs or wai == 10:
        user_first  = 'B'
        oc = 0
        bc = 0
    if user_first == 'B' and oc < overs:
        ai_bowler_choice = random.choice(au_bowler)
        if bc == 6:
            oc = oc + 1
            bc = 0
            ai_bowler_choice = random.choice(au_bowler)
            try:
                ai_bowler_choice.oversb += 1
            except:
                pass
        try:
            shot_type = input("Enter shot type(Hit,Slog or Defense by H,S or D)")
            if shot_type == 'H' or 'S'or 'D':
                pass
            else:
                print("Enter H S OR D for shot selection only.")
                continue
        except ValueError:
            print("Please enter a valid shot type.")
            continue

        if shot_type == 'H':
            hit_p(ai_bowler_choice.vskill)
            print(f"Your Score:{runs_player}"
                  f"Wicket: {wp}")
        if shot_type == 'S':
            slog_p(ai_bowler_choice.vskill)
            print(f"Your Score:{runs_player}"
                  f"Wicket: {wp}")
        if shot_type == 'D':
            defend_p(ai_bowler_choice.vskill)
            print(f"Your Score:{runs_player}"
                  f"Wicket: {wp}")
    if user_first == 'BO' and oc < overs and team == 'I':
        if bc == 0:
            try:
                p_bowler_choice_i = int(input(f"Enter the index of a player name from '['{Hardik.name,Axar.name,Jadeja.name,Arshdeep.name,Bumrah.name,Kuldeep.name}']'"))
                if type(p_bowler_choice_i) == int:
                    pass
                else:
                    print("Invalid input")
                    continue
                p_bowler_choice = ind_bowler[p_bowler_choice_i]

            except:
                print("Please enter a valid player index.")
                continue

        if bc == 6:
            oc = oc + 1
            bc = 0
            try:
                p_bowler_choice.oversb += 1
            except:
                pass
        ai_bat_list = ['S','H','D']
        ai_bat_choice = random.choice(ai_bat_list)
        if ai_bat_choice == 'S':
            slog_p(p_bowler_choice.vskill)
            print(f"AI Score:{runs_AI}"
                  f"Wicket: {wai}")
        if  ai_bat_choice == 'H':
            hit_ai(p_bowler_choice.vskill)
            print(f"AI Score:{runs_AI}"
                  f"Wicket: {wai}")
        if ai_bat_choice == 'D':
            defend_ai(p_bowler_choice.vskill)
            print(f"AI Score:{runs_AI}"
                  f"Wicket: {wai}")
    if user_first == 'BO' and oc < overs and team == 'A':
        if bc == 0:
            try:
                p_bowler_choice_i = int(input(
                    f"Enter the index of a player name from '['{Maxwell.name,Green.name,Ben.name,Ellis.name,Kunheman.name,Zampa.name}']'"))
                if type(p_bowler_choice_i) == int:
                    pass
                else:
                    print("Invalid input")
                    continue
                p_bowler_choice = au_bowler[p_bowler_choice_i]

            except:
                print("Please enter a valid player index.")
                continue

        if bc == 6:
            oc = oc + 1
            bc = 0
            try:
                p_bowler_choice.oversb += 1
            except:
                pass
                p_bowler_choice = au_bowler[p_bowler_choice_i]


            try:
                p_bowler_choice.oversb += 1
            except:
                pass
        ai_bat_list = ['S', 'H', 'D']
        ai_bat_choice = random.choice(ai_bat_list)
        if ai_bat_choice == 'S':
            slog_p(p_bowler_choice.vskill)
            print(f"AI Score:{runs_AI}"
                  f"Wicket: {wai}")
        if ai_bat_choice == 'H':
            hit_ai(p_bowler_choice.vskill)
            print(f"AI Score:{runs_AI}"
                  f"Wicket: {wai}")
        if ai_bat_choice == 'D':
            defend_ai(p_bowler_choice.vskill)
            print(f"AI Score:{runs_AI}"
                  f"Wicket: {wai}")









