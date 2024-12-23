from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("Sleeping...")

# Interface (using abstract base class with only abstract methods)
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

# Concrete class implementing both abstract class and interface
class Bird(Animal, Flyable):
    def make_sound(self):
        print("Chirp chirp")

    def fly(self):
        print("Flying...")

# Usage
bird = Bird()
bird.make_sound()  # Output: Chirp chirp
bird.sleep()       # Output: Sleeping...
bird.fly()         # Output: Flying...