def arraySum(thisArray):
    if len(thisArray) == 0:
        return 0
    else:
        return thisArray[0] + arraySum(thisArray[1:])

myArray = [1, 2, 3, 4, 5]

print(arraySum(myArray))
