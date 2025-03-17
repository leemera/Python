class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"
    def __str__(self):
        return f"f{self.name} is a {self.breed} dog." 