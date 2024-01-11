import Sun as s
import Planet as p

class SolarSystem:

    def __init__ (self, width, height):
        self.thesun = None
        self.planets = [ ]

    def addSun (self, asun):
        self.thesun = asun

    def addPlanet (self, aplanet):
        self.planets.append (aplanet)

    def removwPlanet (self):
        r = input ("Which planet would you like to remove?")
        for i in self.planets:
            if r == i:
                self.planets -= i

    def showPlanets (self):
        for aplanet in self.planets:
            print (aplanet.getName ())

    def numPlanets (self):
        p = 0
        for i in self.planets:
            p += 1
        print (p)

    def totalMass (self):
        m = 0.0
        for i in self.planets:
            m += i.getMass ( )
        print (m)

    def getNearest (self):
        d = self.planets [0].getDistance ( )
        for i in self.planets:

            if i.getDistance ( ) < d:
                d = i.getDistance ( )

        for j in self.planets:
            if d == j.getDistance ( ):
                print (j.getName ())

    def getFarthest (self):
        d = 0
        for i in self.planets:
            if i.getDistance ( ) > d:
                d = i.getDistance ( )

        for j in self.planets:
            if d == j.getDistance ( ):
                print (j.getName ())