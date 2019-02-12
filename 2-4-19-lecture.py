######## BOARD WORK ##############

import math

class Triangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def hyp(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

myTriangle = Triangle(4, 3)

#print(myTriangle.hyp())


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def isIn(self):
        if (math.sqrt(self.x ** 2 + self.y ** 2) > self.r):
            return False
        else:
            return True

myCircle = Circle((1 / math.sqrt(2)), (1.1 / math.sqrt(2)), 1)

#print(myCircle.isIn())

def sumRec(anArray):
    if len(anArray) == 1:
        return anArray[0]
    return (anArray[0] + sumRec(anArray[1:]))

#print(sumRec([1,2,3,4,5]))

def sumEvenRec(anArray):
    if anArray == []:
        return 0
    if anArray[0] % 2 == 0:
        return (anArray[0] + sumEvenRec(anArray[1:]))
    return sumEvenRec(anArray[1:])

#print(sumEvenRec(['a', 'b', 'cc']))

def sumEveryOther(anArray):
    if anArray == []:
        return 0
    if len(anArray) <= 2:
        return anArray[0]
    if len(anArray) % 2 == 0:
        return (anArray[0] + sumEveryOther(anArray[2:]))
    return (anArray[0] + sumEveryOther(anArray[2:]))


#print(sumEveryOther([1,1,0,2,0,3,0,4,0,5,0]))

######### LECTURE #########

#Sets
s = {100, 2, 3, 4}

s.add(4)
s.add(4)
s.add(4)

#print(s)

for element in s:
    #print(element)

#print(({1,2,3} == {2,1,3}))

#frozensets are IMMUTABLE

#Maps

#dict literal
#key : value
#d = {
#    "foo" : 1,
#    "bar" : 2,
#    "baz" : 3
#    }

#print("foo" in d)

#Tuples
#t = (1, 2, 24)

#print(t)
