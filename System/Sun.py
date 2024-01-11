import math

class Sun:

    def __init__ (self, iname, irad, im, itemp):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.temp = itemp

    def __str__ (self):
        return self.name
    
    def getName (self):
        return self.name
    
    def getRadius (self):
        return self.radius
    
    def getMass (self):
        return self.mass
    
    def getDistance (self):
        return self.distance
    
    def getTemp (self):
        return self.temp
    
    def getVolume (self):
        v = 4.0/3 * math.pi * self.radius**3
        return v
    
    def getSurfaceArea (self):
        sa = 4.0 * math.pi * self.radius**2
        return sa
    
    def getDensity (self):
        d = self.mass / self.getVolume ( )
        return d
    
    def getCircumference (self):
        c = 2 * (math.pi * self.radius)

    #mutator Methods

    def setName (self, newName):
        self.name = newName

    def setRadius (self, newRad):
        self.radius = newRad