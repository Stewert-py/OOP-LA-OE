class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display_details(self):
        print(f"Toy: {self.name}")
        print(f"Price: ${self.price}")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

# Create and test car object
toy_car = Car("Hot Wheels Racer", 9.99)
toy_car.display_details()
