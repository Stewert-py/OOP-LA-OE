class Character:
    def __init__(self, name, health=100, power=20):
        self.name = name
        self.health = health
        self.power = power
        self.base_power = power
    
    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name} for {self.power} damage!")
        print(f"{target.name}'s remaining health: {target.health}")
    
    def special_move(self):
        pass

class Warrior(Character):
    def special_move(self):
        print(f"{self.name} uses Shield Bash!")
        self.power = self.base_power * 2
        print(f"Attack power doubled to {self.power} for next attack!")

class Mage(Character):
    def special_move(self, target):
        damage = 100
        print(f"{self.name} casts Fireball!")
        target.health -= damage
        print(f"{target.name} takes {damage} magic damage!")
        print(f"{target.name}'s remaining health: {target.health}")

class Archer(Character):
    def special_move(self, target):
        print(f"{self.name} shoots a Piercing Arrow!")
        direct_damage = self.power * 1.5
        target.health -= direct_damage
        print(f"{target.name} takes {direct_damage} piercing damage!")
        print(f"{target.name}'s remaining health: {target.health}")

# Test the battle system
warrior = Warrior("Conan", health=150, power=25)
mage = Mage("Gandalf", health=80, power=15)
archer = Archer("Legolas", health=100, power=20)

# Demonstrate normal attacks
warrior.attack(mage)
mage.attack(archer)
archer.attack(warrior)

# Demonstrate special moves
warrior.special_move()
warrior.attack(mage)  # Attack with doubled power
mage.special_move(warrior)  # Direct magic damage
archer.special_move(mage)  # Piercing damage
