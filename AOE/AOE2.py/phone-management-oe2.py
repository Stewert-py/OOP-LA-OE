class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"

class PhoneManager:
    def __init__(self):
        self.phones = []
    
    def add_phone(self):
        brand = input("Enter phone brand: ")
        model = input("Enter phone model: ")
        price = float(input("Enter phone price: "))
        phone = Phone(brand, model, price)
        self.phones.append(phone)
        print("Phone added successfully!")
    
    def modify_phone(self):
        if not self.phones:
            print("No phones in the list!")
            return
        
        self.list_phones()
        index = int(input("Enter phone number to modify: ")) - 1
        if 0 <= index < len(self.phones):
            phone = self.phones[index]
            phone.price = float(input("Enter new price: "))
            print("Phone modified successfully!")
        else:
            print("Invalid phone number!")
    
    def delete_phone(self):
        if not self.phones:
            print("No phones in the list!")
            return
        
        self.list_phones()
        index = int(input("Enter phone number to delete: ")) - 1
        if 0 <= index < len(self.phones):
            del self.phones[index]
            print("Phone deleted successfully!")
        else:
            print("Invalid phone number!")
    
    def list_phones(self):
        if not self.phones:
            print("No phones in the list!")
            return
        
        print("\nList of Phones:")
        for i, phone in enumerate(self.phones, 1):
            print(f"{i}. {phone}")

def main():
    manager = PhoneManager()
    
    while True:
        print("\nPhone Management System")
        print("1. Add Phone")
        print("2. Modify Phone")
        print("3. Delete Phone")
        print("4. List Phones")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            manager.add_phone()
        elif choice == "2":
            manager.modify_phone()
        elif choice == "3":
            manager.delete_phone()
        elif choice == "4":
            manager.list_phones()
        elif choice == "5":
            print("Thank you for using Phone Management System!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
