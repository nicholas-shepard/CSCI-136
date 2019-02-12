def dupString(aString):
    if len(aString) <= 1:
        return aString
    return dupStringHelper(aString[1:], aString[0])

def dupStringHelper(aString, prevChar):
    if len(aString) == 1:
        if aString == prevChar:
            return ""
    if aString[0] == prevChar:
        return (aString[0] + dupStringHelper(aString[1:], prevChar))
    return (prevChar + aString[0] + dupStringHelper(aString[1:], aString[0]))

print(dupString("aaabbccc"))
