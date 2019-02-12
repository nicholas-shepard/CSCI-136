import math

n = 2

while n <= 2048:
    print(int(math.log(n)), end = "")
    print("\t", end = "")
    print(n, end = "")
    print("\t", end = "")
    print(int(n * math.log(n)), end = "")
    print("\t", end = "")
    print(n ** 2, end = "")
    print("\t", end = "")
    print(n ** 3, end = "")
    print("\t", end = "")
    print(2 ** n, end = "")
    print("\t\n\n")
    n *= 2
