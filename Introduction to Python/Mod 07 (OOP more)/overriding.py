class Person:
    def __init__(self, name, age, height, weight) -> None:
        # Initializing the attributes for the Person class
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        # Placeholder for a generic eating behavior
        print('Carbohydrate, Protein, Fat')

    def exercise(self):
        # Abstract method to be implemented by child classes
        raise NotImplementedError('Child class must implement this method')


class Crickter(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        # Adding 'team' attribute specific to Cricketer class
        self.team = team
        # Calling the parent class constructor
        super().__init__(name, age, height, weight)
        
    # Overriding the 'eat' method to specify Cricketer's eating habits
    def eat(self):
        print('Protein, Vegetables, Fruits')

    def exercise(self):
        # Implementing the abstract exercise method with activities specific to Cricketers
        print('Running, Lifting, Stretching')

    # Overloading the '+' operator to add the ages of two Cricketer objects
    def __add__(self, other):
        return self.age + other.age
    
    # Overloading the len() function to return the age of the Cricketer
    def __len__(self):
        return self.age


# Creating two Cricketer objects
player1 = Crickter('Virat', 32, 5.9, 70, 'IND')
# player1.eat()  # Uncomment this line to display player1's eating behavior
# player1.exercise()  # Uncomment this line to display player1's exercise routine

player2 = Crickter('Rohit', 34, 5.11, 75, 'IND')

# Demonstrating the overloaded '+' operator to add the ages of two players
print(player1 + player2)  # Output: 66

# Demonstrating the overloaded len() function to get the age of player1
print(len(player1))  # Output: 32
