import random
# r > s, s > p, p > r


def play():
    print('Hello there!')
    comp = random.choice(['r', 'p', 's'])
    user = input("Please chose 'r' for rock, 'p' for paper or 's' for scissors! ")
    print(f'Computer: {comp}')
    cond1 = user == 'r' and comp == 's'
    cond2 = user == 's' and comp == 'p'
    cond3 = user == 'p' and comp == 'r'
    if user == comp:
        print('It is a Tie!')
    elif cond1 or cond2 or cond3:
        print('Yay! You won!')
    else:
        print('You lost!')
    again = input('Play again? [Y/n] ').lower()
    if again == 'y':
        play()


play()