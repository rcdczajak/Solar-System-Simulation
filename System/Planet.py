import math

class Planet:

    def __init__ (self, iname, irad, im, idist):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.distance = idist

    def getName (self):
        return self.name
    
    def getRadius (self):
        return self.radius
    
    def getMass (self):
        return self.mass
    
    def getDistance (self):
        return self.distance
    
    def getVolume (self):
        v = 4.0/3 * math.pi * self.radius**3
        return v
    
    def getSurfaceArea (self):
        sa = 4.0 * math.pi * self.radius**2
        return sa
    
    def getDensity (self):
        d = self.mass / self.getVolume ( )
        return d