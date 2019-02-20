class StringBuilder:

    def __init__(self):
        self.a = []

    def add(self, s):
        self.a.append(s)

    def __str__(self):
        print(sum(self.a))

myString = StringBuilder

myString.add("Hello! ")
myString.add("Why is this class so shitty? ")
myString.add("I wish I knew.")
