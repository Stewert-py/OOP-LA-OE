
class FavoriteFood:

    def __init__(self, name, ingredients):
        self.name = name  # Private attribute
        self.ingredients = ingredients  # Private attribute
    
    
    def to_string(self):
        return f"{self.name} contains the following ingredients: {', '.join(self.__ingredients)}"


food1 = FavoriteFood("Pizza", ["Dough", "Tomato Sauce", "Cheese", "Pepperoni"])
food2 = FavoriteFood("Pasta", ["Noodles", "Tomato Sauce", "Garlic", "Basil"])
food3 = FavoriteFood("Sandwich", ["Bread", "Lettuce", "Tomato", "Ham", "Cheese"])


print(food1.to_string())
print(food2.to_string())
print(food3.to_string())