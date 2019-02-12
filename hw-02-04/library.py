def stringxy(aString, x, y):
    if len(aString) == 0:
        return ""
    else:
        if aString[0] == x:
            return (y + (stringxy(aString[1:], x, y)))
        else:
            return (aString[0] + stringxy(aString[1:], x, y))
    #DONE

def evenInts(intArray):
    if len(intArray) == 0:
        return []
    
    if intArray[0] % 2 == 1:
        return evenInts(intArray[1:])
    else:
        return (intArray[0], evenInts(intArray[1:]))

def dupChars(aString):
    pass

def dupChars2(aString):
    pass

print(evenInts([1, 2, 3, 4, 5, 6]))
