# LA#5: Utilizing self parameter
class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def get_hero_info(self):
        return f"{self.name} is a {self.role} hero"

# Example usage
hero = Hero("Layla", "marksman")
print(hero.get_hero_info())  # Output: Layla is a marksman hero
