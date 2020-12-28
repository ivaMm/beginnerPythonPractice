def is_prime(n):
    divisors = []
    i = 1
    while i <= n:
        if n % i == 0:
            divisors.append(i)
        i += 1
    return len(divisors) == 2


def check():
    num = int(input('Enter number: '))
    prime = is_prime(num)
    print(f'{num} is prime number') if prime else print(f'{num} is not prime number')


check()
