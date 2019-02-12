import math

class Stats:
    def __init__(self, s):
        self.s = s
        
    def setadd(self, num):
        self.s.add(num)

    def setlen(self):
        return len(self.s)

    def setmean(self):
        return (sum(self.s)/len(self.s))

    def setsd(self):
        capsig = 0
        for i in self.s:
            capsig += ((i - self.setmean()) ** 2)
        return math.sqrt(capsig / self.setlen())

    def setvar(self):
        return (self.setsd() ** 2)

class Stats2:
    def __init__(self, setl, sets, setssquares):
        self.setl = setl
        self.sets = sets
        self.setssquares = setssquares

    def setadd(self, num):
        self.setl += 1
        self.sets += num
        self.setssquares += (num ** 2)

    def setlen(self):
        return self.setl

    def setmean(self):
        return (self.sets / self.setl)

    def setsd(self):
        capsig = self.setssquares + self.setl * (self.setmean()) - (2 * self.setmean() * self.sets)
        return math.sqrt(capsig / self.setl)

    def setvar(self):
        return (self.setsd() ** 2)
    

mystats = Stats({-1.0, 1.0, 0.0})
mystats2 = Stats2(3, 0, 2)

print(mystats.setsd())
print(mystats2.setsd())

