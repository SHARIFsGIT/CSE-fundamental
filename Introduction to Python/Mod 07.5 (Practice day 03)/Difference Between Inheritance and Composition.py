""" 
Inheritance:
- "Is-A" relationship between classes.
- Subclass inherits the properties and behavior of the superclass.
"""

""" 
Composition:
- "Has-A" relationship between classes.
- Class contains an instance of another class. 
"""

# Inheritance Example
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Bark"

dog = Dog()
print(dog.speak())  # Bark



# Composition Example
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

engine = Engine()
car = Car(engine)
print(car.start())  # Engine started
