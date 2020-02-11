from random import randint

print('Hi Bool, ready to play rock-paper-scissors?')

# assign a random number to the computer
random_number = randint(0, 2)

# assign a random play to the computer
cool = ''
if random_number == 0:
    cool = 'Rock'
elif random_number == 1:
    cool = 'Paper'
else:
    cool = 'Scissors'

# the boolean to hold player's winning stats
win = False
tie = False

player = input('Rock, Paper, Scissors?')

# TODO: implement the rock-paper-scissors game here

# TODO: now make this game repeat itself until player enters "Exit"
# Your program should store a count of how many terms both Bool and Cool won
# And print this at the end of programs
