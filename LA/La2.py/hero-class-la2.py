# LA#2: Utilizing __init__
class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def print_hero(self):
        print(self.name, self.role)

# Example usage
hero = Hero("Layla", "marksman")
hero.print_hero()  # Output: Layla marksman
