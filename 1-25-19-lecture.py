def productArray(myArray):
    total = 1
    for i in myArray:
        total *= i
    return total

print(productArray([2, 2, 3]))
