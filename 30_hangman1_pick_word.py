import random

def pick_word(file):
    with open(file) as f:
        words = f.read().splitlines()
    return random.choice(words)


print(pick_word('sowpods.txt'))

