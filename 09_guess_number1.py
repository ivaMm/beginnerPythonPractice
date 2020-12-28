import random


def play():
    num = random.randint(1, 9)
    guess = 0
    counter = 0
    while num != int(guess) and guess != "exit":
        guess = input('Guess a number between 1 to 9: ')
        if guess == "exit":
            break
        guess = int(guess)
        counter += 1
        if int(guess) < num:
            print('Too low')
        elif int(guess) > num:
            print('Too high')
        else:
            print(f'Yay! Your guess {guess} is correct! You needed {counter} {pluralize("guess")}!')
            again = input('Play again? [Y/n] ').lower()
            if again == 'y':
                play()


def pluralize(my_string):  # ternary operator syntax: [on_true] if [expression] else [on_false]
    return my_string + 'es' if my_string.endswith('s') else my_string + 's'


play()
