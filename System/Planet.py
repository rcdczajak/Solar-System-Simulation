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
    
    