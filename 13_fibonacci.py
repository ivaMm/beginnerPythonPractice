
def generate_fibonacci(n):
    if n <= 0:
        return False
    else:
        f = [1]
        while len(f) < n:
            f.append(sum(f[len(f) - 2:len(f)]))
        return f



def generate_it():
    num = int(input("How many Fibonnaci numbers to generate? "))
    fibonacci = generate_fibonacci(num)
    if fibonacci:
        print(f'Here are your Fibonacci sequence: {fibonacci}')
    else:
        print("You should ask for at least 1 Fibonacci number! Try again:)")
        generate_it()


generate_it()
