from abc import ABC, abstractmethod

class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass

class Warrior(GameCharacter):
    def attack(self):
        print("Swings sword!")

class Mage(GameCharacter):
    def attack(self):
        print("Casts a fireball!")

class Archer(GameCharacter):
    def attack(self):
        print("Shoots an arrow!")

class Healer(GameCharacter):  # Bonus class
    def attack(self):
        print("Casts healing spell on ally!")

# Create instances of each character type
warrior = Warrior()
mage = Mage()
archer = Archer()
healer = Healer()

# Test attacks
print("Warrior:", end=" ")
warrior.attack()

print("Mage:", end=" ")
mage.attack()

print("Archer:", end=" ")
archer.attack()

print("Healer:", end=" ")
healer.attack()
