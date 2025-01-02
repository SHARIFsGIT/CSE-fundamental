""" 
Operator overloading allows custom implementation of operators (like +, -, ==) for user-defined classes. It enables objects of custom classes to behave like built-in types.
"""
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

a = ComplexNumber(1, 2)
b = ComplexNumber(3, 4)
c = a + b  # Operator Overloading
print(c)  # Output: 4 + 6i


""" 
Method overriding allows a subclass to provide a specific implementation of a method already defined in its parent class. 
"""
class Parent:
    def show(self):
        return "Parent Method"

class Child(Parent):
    def show(self):
        return "Child Method"  # Overriding Parent Method

obj = Child()
print(obj.show())  # Output: Child Method


