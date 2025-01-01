# Define the User class
class User:
    # Constructor method to initialize a User object with name, age, and money attributes
    def __init__(self, name, age, money) -> None:
        self._name = name        # Protected attribute (convention: single underscore means it's for internal use)
        self._age = age          # Protected attribute
        self.__money = money     # Private attribute (double underscore makes it inaccessible directly outside the class)

    # Method to access the user's name (returns the protected _name attribute)
    def name(self):
        return self._name

    # Getter method to access the user's age using the @property decorator
    @property
    def age(self):
        return self._age

    # Getter method to access the private attribute __money, renamed as salary
    @property
    def salary(self):
        return self.__money

    # Setter method to update the salary, while validating the input
    @salary.setter
    def salary(self, value):
        if value < 0:  # Check if the provided value is negative
            return 'Salary cannot be negative'  # Return a message if the input is invalid
        else:
            self.__money += value  # Update the private attribute __money if the value is valid

# Create an instance of the User class
user1 = User('John', 30, 1000)

# Access the user's name using the name() method
print(user1.name())  # Output: John

# Access the user's age using the property method
print(user1.age)  # Output: 30

# Access the user's salary using the property method
print(user1.salary)  # Output: 1000

# Update the user's salary using the setter method
user1.salary = 2000  # Adds 2000 to the current salary
print(user1.salary)  # Output: 3000

# Note:
# - Trying to access the private attribute directly (e.g., user1.__money) will result in an AttributeError.
# - The age and salary attributes are accessed like normal variables due to the @property decorator.