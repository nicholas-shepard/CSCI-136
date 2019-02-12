import sys
################# BOARD WORK ############################

#1. Printing first 10 items from stdin

#count = 0


#    for i in sys.stdin:
#        if i < 10:
#            print(i)
#        count += 1

#2. Unique elements in an array as a set

#def func(anArray):
#    s = set()
#    for i in anArray:
#        s.add(i)
#    return s

#print(func([1,2,2,2,3,4,4,5,6,6,6,7,8,8,9]))

#3. Recursive version of #2

#def funcRecHelper(anArray, s):
#    if len(anArray) == 0:
#        continue
#    s.add(anArray[0])
#    return funcRec

#def funcRec(anArray):
#    s = set()
#    if len(anArray) == 1:
#        return {anArray[0]}
#    return funcRecHelper(anArray[1:],

#print(funcRec([1,1,1,2,2,3,4,5,5,6]))

#4.Class that represents an interval

#class Interval:
#    def __init__(self, a, b):
#        self.a = a
#        self.b = b

#    def contains(self, n):
#        if (self.a < n) and (self.b > n):
#            return True
#        else:
#            return False

#interval1 = Interval(1, 5)

#print(interval1.contains(5.001))

#################   LECTURE  ############################

class MyClass:

    def f(self):
        print("Hello")

class NewClass(MyClass):

    def t(self):
        print("Hi")

thisClass = NewClass()

thisClass.f()
