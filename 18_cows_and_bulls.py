import random
import string


def generate_number_list(size=4):
    return random.sample(string.digits, size) #''.join(


def play():
    num = generate_number_list()
    # print(num)
    guess = []
    while guess != num:
        guess = list(input('Guess a 4 digit number: '))
        c = 0
        b = 0
        for n1 in guess:
            for n2 in num:
                if n1 == n2 and guess.index(n1) == num.index(n2):
                    c += 1
                elif n1 == n2 and guess.index(n1) != num.index(n2):
                    b += 1
        print(f'{c} cows, {b} bulls')
    print(f'Yay! You guessed correct the number {"".join(guess)}')


play()