class FavoriteFood:
    
    def __init__(self, name, ingredients):
        self.__name = name  # Private attribute
        self.__ingredients = ingredients  # Private attribute
    
    
    def get_name(self):
        return self.__name

    
    def set_name(self, new_name):
        self.__name = new_name

    
    def get_ingredients(self):
        return self.__ingredients

    
    def set_ingredients(self, new_ingredients):
        self.__ingredients = new_ingredients

    # Public method to return the string representation
    def to_string(self):
        return f"{self.get_name()} contains the following ingredients: {', '.join(self.get_ingredients())}"


food1 = FavoriteFood("Pizza", ["Dough", "Tomato Sauce", "Cheese", "Pepperoni"])
food2 = FavoriteFood("Pasta", ["Noodles", "Tomato Sauce", "Garlic", "Basil"])
food3 = FavoriteFood("Sandwich", ["Bread", "Lettuce", "Tomato", "Ham", "Cheese"])


food1.set_name("Veggie Pizza")
food1.set_ingredients(["Dough", "Tomato Sauce", "Cheese", "Bell Peppers", "Olives"])


print(food1.to_string())
print(food2.to_string())
print(food3.to_string())