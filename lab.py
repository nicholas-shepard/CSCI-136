import sys

listNums = sys.argv[1:]

def cat():
    print(listNums)

def head(num):
    print(listNums[4:num])

def tail(num):
    print(listNums[-num:])
