#CA 3 Programming for Big data. B8IT105 (B8IT105_1617_TMD3)
#Stuart O'Rourke
#Student Number: 10334192
#DBS Car Rental.

#Object is blue print, methods pass arguement to Class object. 

#Determination of the objects that make up the system. 

class Car(object):#Class definitions for car objects Petrol, Electric, Diesel, Hybrid.
# initiate the objects as above, associate attributes.
#Private instance variables of a class begin with two underscore characters (e.g., __colour) and cannot be directly accessed
    
    def __init__(self):#Things an object knows about itself are called instance variables. An object will present an interface to other objects to allow interaction.


        self.__colour = ''#class variable atrributes colour, hidden/private, self by convention.
        self.__make = ''# class variable make hidden/private
        self.__mileage = 0 # class variable mileage/private
        self.engineSize = ''# classs variable engine size/not hidden

    def getColour(self):#The things an object can do are called methods. Set and get are ways of accessing Private instance variables.
        return self.__colour # get methods colour, make, milage. A method is a function that belongs to an object and passes arguements to the object

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage

    def setColour(self, colour):#set method, colour, make, milage.
        self.__colour = colour 

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage


class ElectricCar(Car):#sub class of object, inherits from Class Object blueprint.
    
    def __init__(self):
        Car.__init__(self)
        self.__numberOfFuelCells = 4

    def getNumberOfFuelCells(self): #set number of fuel cells
        return self.__numberOfFuelCells

    def setNumberOfFuelCells(self, value): # set number of fuel cells
        self.__numberOfFuelCells = value

class PetrolCar(Car):#sub class of object, inherits from Class Object blueprint.

    def __init__(self):
        Car.__init__(self)
        self.__cubic_capacity = 1 # number of litres or cubic capacity in Cubic centimetres CC

    def getCubicCapacity(self):
        return self.__cubic_capacity 

    def setCubicCapacity(self, value):
        self.__CubicCapacity = value #Set cubic capacity of engine

class DieselCar(Car):#sub class of object, inherits from Class Object blueprint.

    def __init__(self):# Define cubic capacity Diesel
        Car.__init__(self)
        self.__cubicCapacityD = 2.6 

    def getCubicCapacityD(self):
        return self.__CubicCapacityD # Return value of Cubic capacity

    def setCubicCapacityD(self, value):
        self.__CubicCapacityD = value
		
class HybridCar(Car):##sub class of object, inherits from Class Object blueprint.  

    def __init__(self):
        Car.__init__(self)
        self.__CubicCapacityH = 2.2 #Normal petrol engine in Hybrid, coupled with fuel cells,

    def getCubicCapacityH(self):
        return self.__CubicCapacityH

    def setCubicCapacityH(self, value):
        self.__CubicCapacityH = value

