class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"

# Polymorphic behavior
vehicles = [Car(), Plane(), Bicycle()]

for vehicle in vehicles:
    print(vehicle.move())
