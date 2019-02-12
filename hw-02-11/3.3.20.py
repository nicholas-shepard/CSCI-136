from datetime import datetime

current = datetime.now()
tot_seconds = (current - current.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

class Time:
    def curhour():
        current = datetime.now()
        tot_seconds = (current - current.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        return int(tot_seconds / 3600)

    def curmin():
        current = datetime.now()
        tot_seconds = (current - current.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        return int(tot_seconds / 60)

    def cursec():
        current = datetime.now()
        tot_seconds = (current - current.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        return int(tot_seconds)

    def __str__(self):
        current = datetime.now()
        tot_seconds = (current - current.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        return ("%d:%d:%d" % (self.curhour(), (self.curmin() % 60), (self.cursec() % 3600)))


time1 = Time

#print(time1.cursec())

current = datetime.now()
tot_seconds = (current - current.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

hours = int(tot_seconds/3600)
mins = int((tot_seconds - (hours * 3600)) / 60)


print("%d:%d:%d" % (int(tot_seconds/3600)
