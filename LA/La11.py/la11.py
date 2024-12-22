class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def describePhone(self):
        print(f"This is a {self.brand} {self.model}")

class Android(Phone):
    def __init__(self, brand, model):
        super().__init__(brand, model)

# Create instance
android_phone = Android("Samsung", "Galaxy S21")

# Test description
android_phone.describePhone()
