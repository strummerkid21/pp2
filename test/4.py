def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def filter_prime():
    numbers = input().split()
    primes = []
    for num in numbers:
        num = int(num)
        if is_prime(num):
            primes.append(num)
    print(primes)

filter_prime()
