word = input('Enter word: ').upper()
if word == word[::-1]:
    print(f'{word} is palindrome!')
else:
    print(f'{word} is not palindrome!')

