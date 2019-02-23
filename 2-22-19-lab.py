import sys

#def func(a):
#    d = {}
#    for x in a:
#        if x in d:
#            d[x] += 1
#        else:
#            d[x] = 1
#    return(max(d, key=d.get))

#print(func([1, 2, 1, 7, 2, 1]))

#def func(a):
#    if a == []:
#        return None
#    b = []
#    return funcHelper(a, b)

#def funcHelper(a, b):
#    if a == []:
#        return b
#    if a[0] % 2 == 0:
#        b.append(a[0])
#    return funcHelper(a[1:], b)

#print(func([1,2,2,3,4,5,5,5,6,8,8,9,10]))

#class Circuit:
#    def __init__(self, connected):
#        self.connected = connected

#    def reset(self):
#        self.connected = True
#        return ("Circuit reset.")

#    def is_connected(self):
#        if self.connected == True:
#            return "Connected."
#        return "Not connected."

#circuit1 = Circuit(False)

#print(circuit1.is_connected())
#print(circuit1.reset())
#print(circuit1.is_connected())

a = []

for line in sys.stdin:
    a.append(line)

maxnum = max(a)

for i in range(maxnum, 0, -1):
    for j in range(0, len(a)):
        
