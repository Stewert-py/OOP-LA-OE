class Hero:
    def __init__(self, name, role, damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type
    
    def __str__(self):
        return f"{self.name} is a {self.damage_type} damage {self.role}"
    
    @classmethod
    def describe_team(cls, team):
        print("\nMobile Legends Dream Team:")
        for i, hero in enumerate(team, 1):
            print(f"{i}. {hero}")
        print("\nTeam Composition:")
        print("This team has a perfect balance of physical and magical damage")
        print("with strong initiation and good sustain capabilities!")

# Create dream team
dream_team = [
    Hero("Gusion", "Assassin", "Magical"),
    Hero("Beatrix", "Marksman", "Physical"),
    Hero("Esmeralda", "Tank/Mage", "Magical"),
    Hero("Mathilda", "Support", "Magical"),
    Hero("Paquito", "Fighter", "Physical")
]

# Display team
Hero.describe_team(dream_team)
