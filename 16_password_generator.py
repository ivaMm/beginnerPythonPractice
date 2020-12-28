import random
import string


def generate_password(size):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.sample(chars, size))


def generate_it():
    size = int(input('Enter size of your password: '))
    psw = generate_password(size)
    print(f'Here is your password: {psw}')
    new_psw = input('New one? [Y/n] ').lower()
    if new_psw == 'y':
        generate_it()


generate_it()
