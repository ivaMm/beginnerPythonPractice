import json
from collections import Counter

MONTHS = {'01': 'January',
          '02': 'February',
          '03': 'March',
          '04': 'April',
          '05': 'May',
          '06': 'June',
          '07': 'July',
          '08': 'August',
          '09': 'September',
          '10': 'October',
          '11': 'November',
          '12': 'December'
          }

with open('birthdays.json', 'rt') as f:
    birthday = json.load(f)
    months = [MONTHS[date.split('/')[0]] for date in birthday.values()]
    print(Counter(months))
