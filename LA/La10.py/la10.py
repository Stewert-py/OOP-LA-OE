class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    
    def describeVehicle(self):
        print(f"This is a {self.brand} {self.model} that runs on {self.fuel_type}")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

# Create instances
car = Car("Toyota", "Camry", "gasoline")
motorcycle = Motorcycle("Honda", "CBR", "gasoline")

# Test descriptions
print("Car description:")
car.describeVehicle()

print("\nMotorcycle description:")
motorcycle.describeVehicle()
