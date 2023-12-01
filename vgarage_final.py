class Vehicle:
    """Vehicle parent class"""
# Define initial function
    def __init__ (self, make, model):
        self.make = make
        self.model = model

# Method to set the vehicle make, inherited        
    def setmake(self, make):
        self.make = make
# Method to set vehicle model        
    def setVehiclemodel(self, model):
        self.model = model

# Method to display vehicle model
    def getVehiclemodel(self):
        vmodel = f"{self.model}"
        print(f"Model: {vmodel.title()}")

# Method to display vehicle make
    def getVehiclemake(self):
        vmake = f"{self.make}"
        print(f"Make: {vmake.title()}")
        
# inheret objects from Vehicle class into Car class
class Car(Vehicle):
    """Car child class"""
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def setDoors(self, doors):
        self.doors = doors

    def getDoors(self):
        cdoors = f"{self.doors}"
        print(f"Doors: {cdoors}")
    
class Truck(Vehicle):
    """Truck child class"""
    def __init__(self, make, model, bedlength):
        super().__init__(make, model)
        self.bedlength = bedlength

    def setBedlength(self, bedlength):
        self.bedlength = bedlength

    def getBedlength(self):
        blength = f"{self.bedlength}"
        print(f"Bed length: {blength}ft")
    
print("Welcome to Jackie's Garage!")

# Find better loops
z = True
while z == True:
    
    x = input("Please enter 1 for a car, 2 for a truck, or 3 to exit: ")
    
    if x == '1':
        carmake = input("Enter the car's make: ")
        carmodel = input("Enter the car's model: ")
        cardoors = input("Enter the number of doors on the car: ")

# New instance of Car class, called methods  
        newcar = Car(carmake, carmodel, cardoors)
        newcar.getVehiclemake()
        newcar.getVehiclemodel()
        newcar.getDoors()

    if x == '2':
        truckmake = input("Please enter the truck's make: " )
        truckmodel = input("Pleae enter the truck's model: ")
        trucklength = input("Please enter the truck's bedlength in feet: ")

# New instance of Truck class, called methods       
        newtruck = Truck(truckmake, truckmodel, trucklength)
        newtruck.getVehiclemake()
        newtruck.getVehiclemodel()
        newtruck.getBedlength()

    if x == '3':
        print("Thanks for coming!")
        print("Have a good one!")
        print("Bye!")
        quit()



