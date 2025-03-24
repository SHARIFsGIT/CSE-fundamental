class Person:
    """
    Base class representing a person in the school management system.
    
    Attributes:
        name (str): Name of the person
    """
    
    def __init__(self, name):
        """
        Initialize a Person object.
        
        Args:
            name (str): Name of the person
        """
        self.name = name
    
    def __str__(self):
        """String representation of the Person."""
        return f"Name: {self.name}"