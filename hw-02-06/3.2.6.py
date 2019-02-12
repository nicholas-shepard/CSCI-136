from math import sin
from math import cos
from math import acos
from math import degrees

class Location:

    def __init__(self, lat1, long1):
        self.lat1 = lat1
        self.long1 = long1

    def distanceTo(self, lat2, long2):
        d = 60 * degrees(acos(degrees(sin(self.lat1)) * degrees(sin(lat2)) + degrees(cos(self.lat1)) * degrees(cos(lat2)) * degrees(cos(self.long1 - long2))))
        #d = 60 * acos(degrees(sin(degrees(self.lat1)) * sin(degrees(lat2)) + cos(degrees(self.lat1)) * cos(degrees(lat2)) * cos(degrees(self.long1) - degrees(long2))))
        return d

myLoc = Location(48.87, -2.33)

print(myLoc.distanceTo(37.8, 122.4))
