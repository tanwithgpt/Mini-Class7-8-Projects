import random
print('Message for the host: Enter the range of numbers you want the player to guess')
c = 1
#This is the number of guesses player gets
g = float(input('Enter the amount of guesses the player will get:'))
#This is the number player has to guess:
try:
    diff = int(input('Enter the difficulty:'
        '\nInteger(1)'
        '\nReal Number/Float/ Decimal (2)'))

    if diff == 1:
            ran = int(input('Enter the range of numbers you want the player to guess'))
            num_to_guess = random.randint(0, ran)
            while True:
                ng = float(input('Enter the number you guessed:'))
                if ng == num_to_guess:
                    print('You have guessed the number!')
                    break
                if c == g:
                    print('You ran out of tries decided by the host, try again!')
                    break
                if ng < num_to_guess:
                    c = c + 1
                    print('Your guess is too low, try again!')
                    continue
                if ng > num_to_guess:
                    c = c + 1
                    print('Your guess is too high, try again!')
                    continue
    elif diff == 2:
            ran = int(input('Enter the range of numbers you want the player to guess'))
            num_to_guess = random.uniform(0, ran)
            while True:
                ng = float(input('Enter the number you guessed:'))
                if ng == num_to_guess:
                    print('You have guessed the number!')
                    break
                if c == g:
                    print('You ran out of tries decided by the host, try again!')
                    break
                if ng < num_to_guess:
                    c = c + 1
                    print('Your guess is too low, try again!')
                    continue
                if ng > num_to_guess:
                    c = c + 1
                    print('Your guess is too high, try again!')
                    continue

        # This is where the user tries to guess the number


except ValueError:
        print('Invalid Input')
        exit()








