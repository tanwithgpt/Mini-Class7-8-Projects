def add_log():
    """Adds the logs to Logs.txt"""
    f = open("Logs.txt","a")
    ed = input('Enter the date in DD/MM/YYYY format:')
    em = input('Enter the state of mood:')
    et = input('Enter the task:')
    ed1 = 'Date :' + ed
    em1 = '\nState :' + em
    et1 = '\nTask :' + et + '\n'*2
    f.write(ed1)
    f.write(em1)
    f.write(et1)
    f.close()
def check_log():
    f = open("Logs.txt","r")
    print(f.read())
    f.close()


while True:
    a = int(input('What do you want to do?:'
              '\n1.Add Log'
              '\n2.Check All the Logs'
              '\n3.Exit'
              '\n(Write only the option):'))
    if a == 1:
        add_log()
        print('Your log has been added')
        dyal = input('Do you want to add another log?(y/n):').lower()
        if dyal == 'y':
            add_log()
            print('Your log has been added')
            continue
        if dyal == 'n':
            pass
        dyc = input('Do you want to continue the program?(y/n)').lower()
        if dyc == 'y':
            continue
        if dyc == 'n':
            break
    if a == 2:
        check_log()
        dyc = input('Do you want to add another log?(y/n)').lower()
        if dyc == 'y':
            add_log()
        if dyc == 'n':
            break
    if a == 3:
        break
