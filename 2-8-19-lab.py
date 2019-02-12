############### BOARD WORK ##################

#class parentClass:
#    def printString(aString):
#        print(aString)

#class childClass(parentClass):
#    def printString(aString):
#        super().printString(aString)

#a = childClass

#a.printString("A")

#def lastOddRec(anArray):
#    if anArray[0] % 2 == 1:
#        return lastOddRecHelp(anArray[1:], anArray[0])
#    if anArray[0] % 2 == 0:
#        return lastOddRec(anArray[1:])

#def lastOddRecHelp(anArray, a):
#    if anArray == []:
#        return a
#    if anArray[0] % 2 == 1:
#        return lastOddRecHelp(anArray[1:], anArray[0])
#    if anArray[0] % 2 == 0:
#        return a

#print(lastOddRec([1,2,3,3,3,4,5,6]))

#def setFromArray(anArray):
#    s = set()
#    for i in anArray:
#        s.add(i)
#    return s

def setFromArrayRec(anArray):
    s = set()
    return setFromArrayRecHelp(anArray, s)

def setFromArrayRecHelp(anArray, s):
    if anArray == []:
        return s
    s.add(anArray[0])
    return setFromArrayRecHelp(anArray[1:], s)

print(setFromArrayRec([1,1,1,2,3,3,4,5,6,6,6,7]))

############### LECTURE ###################
