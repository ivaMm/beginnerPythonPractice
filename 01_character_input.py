import datetime
name = input("What's your name? ").capitalize()
age = int(input("How old are you? "))
now = datetime.datetime.now()
year = now.year + (100 - age)
print(f"Hello {name}, you will be 100 years old in the year {year}!")