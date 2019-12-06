#Brandon Kim
#5-2 Vehicle

class Vehicle(object):

    def __init__(self, make, model, fuelCapacity, mpg):
        self.make = make
        self.model = model
        self.fuelCapacity = fuelCapacity
        self.mpg = mpg

        self.totalMiles = 0
        self.fuelLevel = fuelCapacity

    def addGas(self,gallons):
        if gallons+self.fuelLevel > self.fuelCapacity:
            self.fuelLevel = self.fuelCapacity
        else:
            self.fuelLevel += gallons

        return self.fuelLevel

    def getRange(self):
        return self.mpg * self.fuelLevel

    def drive(self,miles):
        if int(miles) > self.getRange():
            self.totalMiles += self.getRange()
            self.fuelLevel = 0
        else:
            self.totalMiles += miles
            gallons = miles/self.mpg
            self.fuelLevel -= gallons


    def __str__(self):
        return ("%s %s (%.1f mpg); %.1f / %.1f gallons in tank; Range = %.1f miles" % (self.make, self.model, self.mpg, self.fuelLevel, self.fuelCapacity, self.mpg*self.fuelLevel ))