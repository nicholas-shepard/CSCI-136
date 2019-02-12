import sys


userInt = int(sys.argv[1])

for i in range(userInt + 1):
    for n in range(i):
        print(i, end="")
    print("\n")
