memory = []
cc = 1
while True:
    a = float(input('Enter the first number:'))
    b = float(input('Enter the second number:'))
    c = input('Enter the type of calculation(Add, Subtract, Multiply, Divide, Modulus, Exponent, Floor division):').capitalize()
    if c == 'Add':
        add = a + b
        memory.append(add)
        print('The sum of',a,'and',b,'is',add)
    if c == 'Subtract':
        sub = a - b
        memory.append(sub)
        print('The difference of',a,'and',b,'is',sub)
    if c == 'Multiply':
        mul = a * b
        memory.append(mul)
        print('The multiplication of',a,'and',b,'is',mul)
    if c == 'Divide':
        div = a / b
        memory.append(div)
        print('The division of',a,'and',b,'is',div)
    if c == 'Modulus':
        mod = a % b
        memory.append(mod)
        print('The modulus of',a,'and',b,'is',mod)
    if c == 'Exponent':
        exp = a ** b
        memory.append(exp)
        print('The exponent of',a,'and',b,'is',exp)
    if c == 'Floor division':
        fdiv = a // b
        memory.append(fdiv)
        print('The floor division of',a,'and',b,'is',fdiv)
    d = input('Do you want to perform another calculation?(Y/N):').capitalize()
    if d == 'Y':
        ac = float(input('How many more calculations do you want to do? Enter it here:'))
    if d == 'Y' and cc <= ac:
        cc += 1

    elif d == 'N' or cc > ac:
        e = input('Do you want to view history of answers of your calculation?(Y/N):').capitalize()
        if e == 'Y':
            ind = int(input('Enter the index of your calculation:'))
            print(memory[ind])
            break
        if e == 'N':
            break




