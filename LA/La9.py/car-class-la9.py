class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def __str__(self):
        return f"This is a {self.brand} car"

# Create car object
my_car = Car("Toyota")

# Print the object using str representation
print("Before deletion:", my_car)

# Delete the object
del my_car

# Try to print after deletion (this will raise an error)
try:
    print("After deletion:", my_car)
except NameError as e:
    print("Error:", e)
