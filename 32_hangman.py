import random
import string


def pick_word(file):
    with open(file) as f:
        words = f.read().splitlines()
    return list((random.choice(words)).upper())


def hangman():
    print('Welcome to Hangman :)')
    alphabet = set(string.ascii_uppercase)
    word = pick_word('sowpods.txt')
    print(word)
    guess = ['_' for ch in word]
    lives = 6
    used_letters = []
    while guess != word and lives > 0:
        print(' '.join(guess))
        print(f'You have {lives} lives')
        if len(used_letters) > 0:
            print(f'Used letters: {used_letters}')    
        letter = input('Guess letter: ').upper()
        if letter in alphabet:
            if letter in used_letters or letter in guess:
                print(f'You already guessed letter {letter}, try another one\n')
            elif letter not in used_letters and letter not in word:
                used_letters.append(letter)
                lives -= 1
                print(f'Sorry, there is no letter {letter}! Try another!\n')
            elif letter in word:
                indices = [index for index, value in enumerate(word) if value == letter]
                for i in indices:
                    guess[i] = letter
                print('')
        else:
            print(f'{letter} is not valid! Try another one!')
    if guess == word and lives > 0:
        print(f'Yay! You guessed correct word {"".join(guess)}')
    else:
        print(f'Oh no! You died! Word was {"".join(word)}')
    play_again()


def play_again():
    again = input("Play again? [Y/N] ").lower()
    if again == 'y':
        print("\n")
        hangman()
        
        
hangman()
