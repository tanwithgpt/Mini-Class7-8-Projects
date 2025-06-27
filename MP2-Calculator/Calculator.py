
a = float(input('Enter 1st no. you want to perform the calculation: '))
b = float(input('Enter 2nd no. you want to perform the calculation: '))

c = input('Enter the type of calculation(Add,Subtract,Divide,Multiply,Exponent,Modulus: ').capitalize()
if c == 'Add':
   add = a + b
   print('The sum of',a,'and',b,'is',add)
elif c == 'Subtract':
    sub = a - b
    print('The difference of',a,'and',b,'is',sub)
elif c == 'Divide':
    div = a / b
    print('The quotient of',a,'and',b,'is',div)
elif c == 'Multiply':
    mult = a * b
    print('The multiplication of',a,'and',b,'is',mult)
elif c == 'Exponent':
    exp = a ** b
    print('The exponent of',a,'and',b,'is',exp)
elif c == 'Modulus':
    mod = a % b
    print('The modulus of',a,'and',b,'is',mod)
else:
    print('Enter a valid option')