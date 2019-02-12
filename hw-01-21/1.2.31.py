import sys

temp = sys.argv[1:]

print(min(temp), end = " ")
print(int(temp[0]) + int(temp[1]) + int(temp[2]) - int(min(temp)) - int(max(temp)), end = " ")
print(max(temp), end = " ")
