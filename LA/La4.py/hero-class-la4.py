# LA#4: Utilizing __str__
class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def __str__(self):
        return f"{self.name} is a {self.role} hero"
    
    def print_hero(self):
        print(str(self))

# Example usage
hero = Hero("Layla", "marksman")
hero.print_hero()  # Output: Layla is a marksman hero
print(hero)        # Output: Layla is a marksman hero
