# Parent class
class Spiderman:
    def __init__(self, name, age):
        self.name = name.lower()  # Make sure the name is in lowercase
        self.age = age

    def describeSpiderman(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Child classes inheriting from Spiderman
class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

# Creating objects for each Spiderman version
tobey = Tobey("Tobey", 45, "Spider-Man (2002)")
andrew = Andrew("Andrew", 38, "The Amazing Spider-Man (2012)")
tom = Tom("Tom", 27, "Spider-Man: Homecoming (2017)")

# Printing the name in uppercase and movie title
print(f"{tobey.name.upper()} - {tobey.movieTitle}")
print(f"{andrew.name.upper()} - {andrew.movieTitle}")
print(f"{tom.name.upper()} - {tom.movieTitle}")
