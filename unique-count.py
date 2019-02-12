import sys

def unique(input1):
    s = []
    for line in sys.stdin:
        if line in s:
            continue
        else:
            s.append(line)
            print(line)
