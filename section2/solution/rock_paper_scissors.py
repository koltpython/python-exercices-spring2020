from random import randint

print('Hi Bool, ready to play rock-paper-scissors?')


bool_win_count = 0
cool_win_count = 0
tie_count = 0

player = input('Rock, Paper, Scissors?')

while player != 'Exit':
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

    tie = cool == player

    if (cool == 'Rock'):
        win = (player == 'Paper')
    elif (cool == 'Paper'):
        win = (player == 'Scissors')
    else:
        win = (player == 'Rock')

    if (tie):
        print('Tie!')
        tie_count += 1
    elif (win):
        print(f'Bool wins, Cool said {cool}')
        bool_win_count += 1
    else:
        print(f'Bool loses, Cool said {cool}')
        cool_win_count += 1

    player = input('Rock, Paper, Scissors?')


# TODO: now make this game repeat itself until player enters "Exit"
# Your program should store a count of how many terms both Bool and Cool won
# And print this at the end of programs
print(f'Bool won {bool_win_count} times, Cool won {cool_win_count} times and {tie_count} rounds ended with a draw.')
