import sys

def f(d):
    if (d*2) > 9:
        dd1 = (d * 2) % 10
        dd2 = ((d * 2) - dd1) / 10
        return (int(dd1 + dd2))
    else:
        return d

tenDigits = int(sys.argv[1])
temp = tenDigits

digitsList = []

for i in range(10):
    di = tenDigits % 10
    tenDigits /= 10
    digitsList.append(int(di))

digitsList.reverse()

for j in range(1, 10, 2):
    digitsList[j] = f(digitsList[j])

sumNums = sum(digitsList)
remainder = sumNums % 10
elevenDigits = temp * 10 + remainder

print(elevenDigits)
