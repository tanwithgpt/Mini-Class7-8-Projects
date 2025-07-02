scorec= 0
scorep = 0
c = 0.0
def compw():
    print('Computer won this game round, they chose:', op)
    global c
    global scorec
    c = c + 1
    scorec += 1
    f = open('history.txt', 'a+')
    f.write('Game round: ' + str(c) + '\n'
            'Computer won this game round: ' + str(c) + '\n')
def playerw():
    print('Player won this game round')
    print('Computer chose:',op)
    global c
    global scorep
    c = c + 1
    scorep += 1
    f = open('history.txt', 'a+')
    f.write('Game round: ' + str(c) + '\n'
            'Player won this game round: ' + str(c) + '\n')
def tie():
    print('Tie, repeat this game round')



import random

ci = float(input('Enter the number of rounds'))

'''Snake / Water
Water / Gun
Gun / Snake'''
while True:
    lst = ['Snake', 'Water', 'Gun']
    op = random.choice(lst)

    a = input('Choose your option: (Snake(s)/Water(w)/Gun(g)')
    if a == 's' or a == 'w' or a == 'g':
        pass
    else:
        print('Wrong input')
        continue

    if a == 's' and op == 'Water':
        playerw()


    elif a == 'g' and op == 'Snake':
        playerw()
    elif a == 'w' and op == 'Gun':
        playerw()
    if op == 'Snake' and a == 'w':
        compw()


    elif op == 'Snake' and a == 'g':
        compw()
    elif op == 'Water' and a == 's':
        compw()
    elif op == 'Water' and a == 'w':
        tie()
    elif op == 'Snake' and a == 's':
        tie()
    elif op == 'Gun' and a == 'g':
        tie()
    if c == ci:

        dyc = input('Do you want to play again?(y/n)').lower()
        if dyc == 'y':
            ci = float(input('Enter the number of rounds'))
            continue
        if dyc == 'n':
            dywr = input('Do you want to know the result?(y/n)').lower()
            if dywr == 'y':
                g = open('history.txt', 'r')
                print(g.read())
                g.close()
                print('Thank you for playing')
                break
            if dywr == 'n':
                print('Thanks for playing')
                break
        break