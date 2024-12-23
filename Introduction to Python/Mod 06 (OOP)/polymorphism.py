# Poly --> Many
# Morphism --> Forms

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print('Animal sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Bark')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Meh')

user1 = Cat('Tom')
# user1.make_sound()

user2 = Dog('Rex')
# user2.make_sound()

user3 = Goat('Billy')
# user3.make_sound()

user4 = Goat('Nanny')
# user4.make_sound()

animals = [user1, user2, user3, user4]
for animal in animals:
    animal.make_sound()