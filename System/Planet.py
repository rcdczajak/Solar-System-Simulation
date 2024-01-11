import math

class Planet:

    def __init__ (self, iname, irad, im, idist, imoons):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.distance = idist
        self.numMoons = imoons
        self.moonList = [ ]

    def __string__ (self):
        return self.name

    def getName (self):
        return self.name
    
    def getRadius (self):
        return self.radius
    
    def getMass (self):
        return self.mass
    
    def getDistance (self):
        return self.distance
    
    def getMoons (self):
        return self.numMoons
    
    def getMoonList (self):
        return self.moonList
    
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
        return c

    #mutator Methods

    def setName (self, newName):
        self.name = newName

    def setMoons (self, newMoons):
        self.numMoons += newMoons

    def addMoon (self, newMoonName):
        self.moonList += newMoonName