num1 = int(input())
num2 = int(input())
num3 = int(input())

temp = [num1, num2, num3]

print(min(temp), end = " ")
print(temp[0] + temp[1] + temp[2] - min(temp) - max(temp), end = " ")
print(max(temp), end = " ")
