import random


def play():
    print('Pick a number between 1 and 100')
    hlc = ''
    guess = 50
    while hlc != 'c':
        if hlc == 'h':
            guess = guess - 1
        elif hlc == 'l':
            guess = guess + 1
        print(f'Program: {guess}')
        hlc = input('Enter "h" for too high, "l" for too low, or "c" for correct! ').lower()
    print(f'Program guessed correct your number {guess}!')


def play2():
    print('Pick a number between 1 and 100')
    hlc = ''
    guess = random.randint(1, 100)
    while hlc != 'c':
        if hlc == 'h':
            guess = random.randint(1, guess - 1)
        elif hlc == 'l':
            guess = random.randint(guess + 1, 100)
        print(f'Program: {guess}')
        hlc = input('Enter "h" for too high, "l" for too low, or "c" for correct! ').lower()
    print(f'Program guessed correct your number {guess}!')


play2()