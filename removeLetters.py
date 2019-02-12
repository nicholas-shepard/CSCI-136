def removeLetters(aString):
    if len(aString) <= 1:
        return ""
    if len(aString) == 2:
        if aString[1] == aString[0]:
            return aString[0]
        else:
            return aString
    if aString[1] == aString[0]:
        return (aString[0] + removeLetters(aString[2:]))
    else:
        return removeLetters(aString[1:])

print(removeLetters("aaaabbbbcccc"))
