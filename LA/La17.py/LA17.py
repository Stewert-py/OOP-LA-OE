import random

class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        target.health -= damage
        target.health = max(0, target.health)  # Prevent health from going below zero
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        print(f"{target.name} now has {target.health} health remaining.\n")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount} points.")
        print(f"{self.name} now has {self.health} health remaining.\n")

def main():
    # Create two Player objects
    player1 = Player("Player1", 100, 20)
    player2 = Player("Player2", 120, 15)

    # Battle loop
    while player1.health > 0 and player2.health > 0:
        # Player1 attacks Player2
        player1.attack(player2)
        if player2.health <= 0:
            print(f"{player1.name} wins!")
            break

        # Player2 attacks Player1
        player2.attack(player1)
        if player1.health <= 0:
            print(f"{player2.name} wins!")
            break

        # Optional: players can randomly heal during battle
        if random.choice([True, False]):
            player1.heal(random.randint(5, 10))
        if random.choice([True, False]):
            player2.heal(random.randint(5, 10))

if __name__ == "__main__":
    main()