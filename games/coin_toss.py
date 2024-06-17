import random
data = ('heads', 'tails')
guess = ''
while guess not in data:
    user = int(input('Enter a number between 0 and 1: '))
    number = random.randint(0, 1)
    if user == number:
        if number == 0:
            guess = 'tails'
        else:
            guess = 'heads'
        print('You have won the game and it will now exit')
        break
    else:
        print('Missed it.')
