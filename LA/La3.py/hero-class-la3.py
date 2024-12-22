# LA#3: Utilizing method
class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def describe_hero(self):
        print(f"{self.name} is a {self.role} hero")

# Example usage
hero = Hero("Layla", "marksman")
hero.describe_hero()  # Output: Layla is a marksman hero
