class Sphere:
    def __init__(self):
        self.radius = 0
        self.Pi = 3.1415
    def __init__(self,r):
        self.Pi = 3.1415
        if r > 0:
            self.radius = r
        else :
            self.radius = 0
    def Area(self):
        area = 4 * self.Pi * self.radius**2
        return area
    def Volume(self):
        volume = (4*self.Pi*self.radius**3)/3
        return volume
    def __str__(self):
        s = 'Sphere chars:\n\tradius: {}\n\tArea: {}\n\tVolume: {}'.format(self.radius,self.Area(),self.Volume())
        return s   
    
r = int(input("ENTER THE SPHERE RADIUS:"))        
sphere = Sphere(r)
print(sphere)
