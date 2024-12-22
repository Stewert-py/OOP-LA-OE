class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Fish(Animal):
    def __init__(self, name, type, can_swim):
        super().__init__(name, type)
        self.can_swim = can_swim

# Create and test fish object
nemo = Fish("Nemo", "Clownfish", True)
print(f"Name: {nemo.name}")
print(f"Type: {nemo.type}")
print(f"Can swim: {nemo.can_swim}")
