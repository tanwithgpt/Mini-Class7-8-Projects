print('Message for the host: Enter the number you want the player to guess')
print('Message for the host: Enter the amount of guesses as well ')
c = 1
#This is the number of guesses player gets
g = float(input('Enter the amount of guesses the player will get:'))
#This is the number player has to guess
n = float(input('Enter it here and hide the number you entered in the output screen:'))
while True:
#This is where the user tries to guess the number
    ng = float(input('Enter the number you guessed:'))
    if ng == n:
       print('You have guessed the number!')
       break
    if c == g:
        print('You ran out of tries decided by the host, try again!')
        break
    if ng < n:
        c = c + 1
        print('Your guess is too low, try again!')
        continue
    if ng > n:
        c = c + 1
        print('Your guess is too high, try again!')
        continue


