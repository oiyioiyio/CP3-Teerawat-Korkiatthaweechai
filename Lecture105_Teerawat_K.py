class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    pass

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

car = Car()
pickup = PickUp()
van = Van()
estatecar = Estatecar()

car.turnOnAirConditioner()
pickup.turnOnAirConditioner()
van.turnOnAirConditioner()
estatecar.turnOnAirConditioner()


