import json

birthday = {}
with open('birthdays.json', 'rt') as f:
    birthday = json.load(f)
    print(birthday)


def add_birthday():
    name = input('Name? ')
    day = input('Birthday? ')
    birthday[name] = day

    with open('birthdays.json', 'w') as f:
        json.dump(birthday, f, indent=2)

    with open('birthdays.json', 'rt') as f:
        obj = json.load(f)
        print(obj)

    add_more()


def add_more():
    more = input('Add more? [Y/n] ').lower()
    if more == 'y':
        add_birthday()


add_birthday()



