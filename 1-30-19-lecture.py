#################BOARD WORK ##########################

#def thisFunction(anArray, anInt):
#    returnArray = []
#    for i in range(0, len(anArray), anInt):
#        returnArray.append(anArray[i])
#    return returnArray

#print(thisFunction([1,2,3,4,5,6,7,8,9,10], 2))

#def negativeNums(anArray):
#    negatives = []
#    for i in anArray:
#        if abs(i) != i:
#            negatives.append(i)
#        else:
#            continue
#    return negatives

#myArray = [-1, 2, 3, -4, -6, 7, 8, 9]

#print(negativeNums(myArray))

#def zip(anArray1, anArray2):
#    returnArray = []
#    for i in range(len(anArray1)):
#        returnArray.append(anArray1[i] * anArray2[i])
#    return returnArray

#array1 = [1, 2, 3]
#array2 = [100, 1000, 10000]

#print(zip(array1, array2))

#######################LECTURE#########################

#def factorial_rec(n):
#    if n == 1:
#        return 1

#    print(n)
#    return n * factorial_rec(n - 1)

#print(factorial_rec(6))

def palindrome_rec(s):
    if len(s) == 1:
        return True
    if len(s) == 2:
        return s[0] == s[1]

    return s[0] == s[-1] and palindrome_rec(s[1:-1])

print(palindrome_rec("abbbbbbbba"))
