class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Create first car object
car1 = Car("Toyota", "Red")
print(f"Car 1: {car1.brand} - {car1.color}")

# Update color of first car
car1.color = "Blue"
print(f"Car 1 after color update: {car1.brand} - {car1.color}")

# Create second car object
car2 = Car("Honda", "White")
print(f"Car 2: {car2.brand} - {car2.color}")

# Show that car2 is not affected by car1's changes
print(f"Car 1 is still: {car1.brand} - {car1.color}")
print(f"Car 2 is still: {car2.brand} - {car2.color}")
