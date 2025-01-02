""" 
Getter: Method to retrieve the value of a private attribute.
Setter: Method to modify the value of a private attribute. 
"""
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self.__age = value

p = Person("John", 25)
print(p.name)  # John
p.name = "Doe"
print(p.name)  # Doe