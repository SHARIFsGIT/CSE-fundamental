""" 
Class Method:
- Works with the class as a whole.
- Takes cls as the first argument.
- Can modify the class state.
- Can't modify the instance state.
- Can be called using the class name or instance name.
- Decorated with @classmethod.
"""

"""
Static Method:
- Works with the class as a whole.
- Doesn't take any default argument.
- Can't modify the class or instance
- Can be called using the class name or instance name.
- Decorated with @staticmethod.
"""

class Example:
    class_variable = "Class Level"

    @classmethod
    def class_method(cls):
        return f"Accessing: {cls.class_variable}"

    @staticmethod
    def static_method():
        return "Independent Method"

print(Example.class_method())  # Accessing: Class Level
print(Example.static_method())  # Independent Method
