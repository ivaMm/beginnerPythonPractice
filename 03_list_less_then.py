a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Enter a number: "))
result = [str(n) for n in a if n < num]

if len(result) > 0:
    print(f"Numbers less then {num} from list {a} are: {','.join(result)}")
else:
    print(f"There's no numbers less then {num} in list {a}.")