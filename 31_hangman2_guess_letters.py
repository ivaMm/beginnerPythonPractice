def guess_letters(word):
    print('Welcome to Hangman :)')
    word = list(word.upper())
    guess = ['_' for ch in word]
    while guess != word:
        print(' '.join(guess))
        letter = input('Guess letter: ').upper()
        if letter in word:
            indices = [index for index, value in enumerate(word) if value == letter]
            for i in indices:
                guess[i] = letter
        else:
            print(f'Sorry, there is no letter {letter}! Try another!')
    print(f'Yay! You guessed correct word {"".join(guess)}')


guess_letters('hello')
