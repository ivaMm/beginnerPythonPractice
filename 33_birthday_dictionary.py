birthdays = {
            'Albert Einstein': '03/14/1879',
            'Benjamin Franklin': '01/17/1706',
            'Ada Lovelace': '12/10/1815',
            'Amelia Earhart': '07/24/1897'
            }


def interface():
    print('>>> Welcome to the birthday dictionary. We know the birthdays of:')
    for key in birthdays.keys():
        print(key)
    user_key = input('>>> Who\'s birthday do you want to look up? ').strip()
    print(f'{user_key}\'s birthday is {birthdays[user_key]}.')


interface()
