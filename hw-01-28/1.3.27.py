import sys

userNum = int(sys.argv[1])

for i in range(userNum):
    if (i % 2) == 0:
        print("* " * userNum)
    else:
        print(" *" * (userNum - 1))
