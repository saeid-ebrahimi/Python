from math import *

class Circle:
    PI = pi
    radius = 0
    def __init__(self):
        self.r = 0
    def __init__(self,init_r):
        self.r = init_r
    def __del__(self):
        print("DELETING OBJECT...")
    def Area(self):
        area = self.PI * self.r**2
        return area
    def Perimeter(self):
        per = 2*self.PI*self.r
        return per
    def __str__(self):
        s = f"Radius: {self.r}\nArea: {self.Area()}\nPerimeter: {self.Perimeter()}"
        return s
print(Circle.PI)
print(Circle.radius)
print("*********************************")
rad = int(input("enter circle radius: "))
cir = Circle(rad)
print(cir)
print("*********************************")
print(str(cir))
    
