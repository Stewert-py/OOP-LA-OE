class BirthdayParty:
    def __init__(self, theme, foods):
        self.theme = theme
        self.foods = foods
    
    def __secret_dish(self):
        return "Special Birthday Cake with Sparklers"
    
    def display_menu(self):
        print(f"\n{self.theme} Party Menu:")
        for food in self.foods:
            print(f"- {food}")
        print(f"Special Surprise: {self.__secret_dish()}")

# Create three different party objects
superhero_party = BirthdayParty("Superhero", 
    ["Pizza", "Hero Sandwiches", "Power Punch", "Cookie Heroes"])

princess_party = BirthdayParty("Princess", 
    ["Cupcakes", "Tea Sandwiches", "Royal Punch", "Magic Wands"])

space_party = BirthdayParty("Space", 
    ["Star Cookies", "Moon Pies", "Asteroid Punch", "Galaxy Brownies"])

# Display menus
superhero_party.display_menu()
princess_party.display_menu()
space_party.display_menu()
