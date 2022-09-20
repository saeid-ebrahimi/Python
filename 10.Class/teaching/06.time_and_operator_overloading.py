class Time:
    def __init__(self, h = 0, m = 0, s = 0):
        if 0 < h <= 24:
            self.__hour = h
        else:
            self.__hour = 0
        if 0 < m <= 59:
            self.__minute = m
        else:
            self.__minute = 0
        if 0 < s <= 59:
            self.__second = s
        else:
            self.__second = 0
    
    def copy(self):
        return Time(self.__hour, self.__minute, self.__second)
    def __copy__(self):
        return Time(self.__hour,self.__minute,self.__second)
    def get_hour(self): return self.__hour
    def get_minute(self): return self.__minute
    def get_second(self): return self.__second

    def __add__(self,time):
        sec = self.__second + time.get_second()
        mini = self.__minute + time.get_minute()
        hour = self.__hour + time.get_hour()
        if sec >= 60:
            sec -= 60
            mini +=1
        if mini >= 60:
            mini -= 60
            hour += 1
        if hour >= 24:
            hour -= 24
        return Time(hour,mini,sec)
    def __iadd__(self, time):
        self.__second += time.get_second()
        self.__minute += time.get_minute()
        self.__hour += time.get_hour()
        if self.__second >= 60:
            self.__second -= 60
            self.__minute += 1
        if self.__minute >= 60:
            self.__minute -= 60
            self.__hour += 1
        if self.__hour >= 24:
            self.__hour -= 24
        return self
    
    def __sub__(self, time):
        sec = self.__second - time.get_second()
        mini = self.__minute - time.get_minute()
        hour = self.__hour - time.get_hour()
        if sec < 0:
            sec += 60
            mini -= 1
        if mini < 0:
            mini += 60
            hour -= 1
        if hour < 0:
            hour += 24
        return Time(hour,mini,sec)
    
    def __isub__(self,time):
        self.__second -= time.get_second()
        self.__minute -= time.get_minute()
        self.__hour -= time.get_hour()
        if self.__second < 0:
            self.__second += 60
            self.__minute -= 1
        if self.__minute < 0:
            self.__minute += 60
            self.__hour -= 1
        if self.__hour < 0:
            self.__hour += 24
        return self
    
    def __eq__(self, time):
        e1 = (self.second == time.get_second())
        e2 = (self.minute == time.get_minute())
        e3 = (self.hour == time.get_hour())
        return (e1 and e2 and e3 )

    def __ne__(self,time):
        return not self.__eq__(time)
    
    def __lt__(self, time):
        if self.__hour < time.get_hour():
            return True
        elif self.__hour == time.get_hour():
            if self.__minute < time.get_minute():
                return True
            elif self.__minute == time.get_minute():
                if self.__second < time.get_second():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __le__(self, time):
        if self.__hour < time.get_hour():
            return True
        elif self.__hour == time.get_hour():
            if self.__minute < time.get_minute():
                return True
            elif self.__minute == time.get_minute():
                if self.__second <= time.get_second():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, time):
        if self.__hour > time.get_hour():
            return True
        elif self.__hour == time.get_hour():
            if self.__minute > time.get_minute():
                return True
            elif self.__minute == time.get_minute():
                if self.__second > time.get_second():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __ge__(self, time):
        if self.__hour > time.get_hour():
            return True
        elif self.__hour == time.get_hour():
            if self.__minute > time.get_minute():
                return True
            elif self.__minute == time.get_minute():
                if self.__second >= time.get_second():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __str__(self):
        return f'Time: {self.__hour}:{self.__minute}:{self.__second}'


time1 = Time(s=20,m=10)
print(time1)
time2 = Time(1,10,9)
print(time2)
print(time2 < time1)
print(time2 >= time1)
print(time1 + time2)
print(time1 - time2)
print(time2 - time1)
