class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __gt__(self, other):
        return self.age > other.age

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)

# Instances
sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)

# Comparison
older = sakib if sakib > musfiq else musfiq
print(f"The older player is {older.name}, age {older.age}.")
