import random
guess = ''
choices = ['heads','tails']
while guess not in ('heads', 'tails'):
    print('GUess the coin toss! Enter the heads or tails: ')
    guess = input()
toss = random.choice(choices) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess aguain!')
    guess=input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

