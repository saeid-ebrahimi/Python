class Time:
    def __init__(self, h = 0, m = 0, s = 0):
        if 0 < h <= 24:
            self.hour = h
        else:
            self.hour = 0
        if 0 < m <= 59:
            self.minute = m
        else:
            self.minute = 0
        if 0 < s <= 59:
            self.second = s
        else:
            self.second = 0
            
    def isEqual(self, time):
        e1 = (self.second == time.second)
        e2 = (self.minute == time.minute)
        e3 = (self.hour == time.hour)
        return (e1 and e2 and e3 )
    def __str__(self):
        return f'Time: {self.hour}:{self.minute}:{self.second}'

time1 = Time(s=9,m=10)
print(time1)
time2 = Time(0,10,9)
print(time2)
print(time2.isEqual(time1))
