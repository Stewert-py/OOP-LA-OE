class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    
    def introduce(self, func):
        def wrapper():
            print("Introducing...")
            func()
            print("This character is amazing!")
        return wrapper

# Create instance
naruto = AnimeCharacter("Naruto", "Shadow Clone Jutsu")

# Define and decorate the function
@naruto.introduce
def character_intro():
    print(f"I am {naruto.name} and I can use {naruto.ability}")

# Call the decorated function
character_intro()
