class FavoriteFood:
    # Step 2: Add private attributes to represent the ingredients
    def __init__(self, name, ingredients):
        self.__name = name  # Private attribute
        self.__ingredients = ingredients  # Private attribute
    
    # Getter method for name
    def get_name(self):
        return self.__name

    # Getter method for ingredients
    def get_ingredients(self):
        return self.__ingredients

    # Public method to return the string representation
    def to_string(self):
        return f"{self.get_name()} contains the following ingredients: {', '.join(self.get_ingredients())}"

# Step 4: Create three objects based on the class
food1 = FavoriteFood("Pizza", ["Dough", "Tomato Sauce", "Cheese", "Pepperoni"])
food2 = FavoriteFood("Pasta", ["Noodles", "Tomato Sauce", "Garlic", "Basil"])
food3 = FavoriteFood("Sandwich", ["Bread", "Lettuce", "Tomato", "Ham", "Cheese"])

# Step 5: Print the objects using the string representation
print(food1.to_string())
print(food2.to_string())
print(food3.to_string())