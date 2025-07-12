def display_hp():
    print("Your current HP:", hpp)
    print("AI current HP:", hpc)
import random
a = input("Enter Difficulty(E/H where E = Easy and H = Hard: ").upper()
opt = ['A','D']
opt_h = ['H','A','D']
if a == "E":
    hpp = 100
    hpc = 100
    dp = 5
    dc = 5
    ap = 10
    ac = 10
    phc = 2
    atc = 0
    while True:
        pi = input("Enter the option(A,D or H where A = Attack, D = Defense and H = Heal: ").upper()
        ci = random.choice(opt)
        if hpc <= 0:
            print("Congratulations, you win!")
            break
        if hpp <= 0:
            print("Sorry, you lose, please try again.")
            break
        if atc == 3:
            print("Please chose any other option other than ATTACK, it is only permitted to use attack 3 times in a row")
            display_hp()
            continue
        if pi == 'H' and hpp <= 90:
            print("You have healed!")
            phc = phc - 1
            hpp = hpp + 10
            display_hp()
            continue
        if pi == 'H' and hpc >= 90:
            print("You cannot heal!(HP is already at 90)")
            display_hp()
            continue
        if ci == "A" and pi == "D":
            hpp = hpp - (ac - dp)
            print("You received damage of:", ac-dp)
            atc = 0
            display_hp()
            continue
        if ci == "D" and pi == "A":
            hpc = hpc - (ap - dc)
            print("AI received damage of ", ap-dc)
            atc += 1
            display_hp()
            continue
        if ci == "A" and pi == "A":
            print("This turn tied")
            display_hp()
            continue
        if ci == "D" and pi == "D":
            print("This turn tied")
            display_hp()
            continue

if a == "H":
    hpp = 100
    hpc = 100
    dp = 5
    dc = 5
    ap = 10
    ac = 15
    phc = 2
    chc = 3
    atc = 0
    while True:
        pin = input("Enter the option(A,D or H where A = Attack, D = Defense and H = Heal: ").upper()
        cin = random.choice(opt)
        if hpc <= 0:
            print("Congratulations, you win!")
            break
        if hpp <= 0:
            print("Sorry, you lose, please try again.")
            break
        if atc == 3:
            print("Please chose any other option other than ATTACK, it is only permitted to use attack 3 times in a row")
            display_hp()
            continue
        if pin == 'H' and hpp <= 90:
            print("You have healed!")
            phc = phc - 1
            hpp = hpp + 10
            display_hp()
            continue
        if pin == 'H' and hpp >= 90:
            print("You cannot heal!(HP is already at 90)")
            display_hp()
            continue
        if cin == 'H' and hpc >= 100:
            print("AI tried to heal, but it couldn't")
            display_hp()
            continue
        elif cin == 'H' and hpc < 100:
            print("AI healed!")
            chc = chc - 1
            hpc = hpc + 10
            display_hp()
            continue
        if cin == "A" and pin == "D":
            hpp = hpp - (ac - dp)
            print("You received damage of:",ac - dp)
            display_hp()
            continue
        if cin == "D" and pin == "A":
            hpc = hpc - (ap - dc)
            print("AI received damage of ", ap-dc)
            display_hp()
            continue
        if cin == "A" and pin == "A":
            print("This turn tied")
            display_hp()
            continue
        if cin == "D" and pin == "D":
            print("This turn tied")
            display_hp()
            continue


