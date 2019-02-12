import math

def isPrime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

def f(num):
    s = set()
    for i in range(2, num + 1):
        if (num % i) == 0:
            if (isPrime(i) == True):
                s.add(i)
    return s

print(f(12))
