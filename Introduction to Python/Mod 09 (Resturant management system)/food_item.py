# -------------------- FoodItem Class --------------------
"""
This module defines the FoodItem class for the restaurant management system.
A FoodItem represents a single dish/item that can be ordered by customers.
"""

class FoodItem:
    """
    # Class: FoodItem
    # Purpose: Represents a food item in the restaurant menu
    #
    # Properties:
    # - name: The name of the food item (str)
    # - price: The price of the food item (float)
    # - quantity: The available quantity in stock (int)
    # - category: The category of the food item (str) - new property
    # - description: Brief description of the food item (str) - new property
    # - ingredients: List of ingredients (list) - new property
    """
    def __init__(self, name, price, quantity, category="Main Course", description="", ingredients=None):
        """
        # Constructor
        # Initializes a new instance of the FoodItem class
        #
        # Parameters:
        # - name: The name of the food item
        # - price: The price of the food item
        # - quantity: The quantity available in stock
        # - category: The category of the food item (default: "Main Course")
        # - description: Brief description of the food item (default: "")
        # - ingredients: List of ingredients (default: empty list)
        """
        # Instance attributes/properties
        self.name = name
        self.price = price
        self.quantity = quantity  # Quantity in stock
        self.category = category
        self.description = description
        self.ingredients = ingredients or []  # Default to empty list if None is provided
        self.discount_percentage = 0  # Default discount percentage is 0%
    
    def __str__(self):
        """
        # Magic/Dunder Method: __str__
        # Returns a string representation of the food item
        # Used when str() is called on an instance
        """
        return f"{self.name} - ${self.price:.2f} ({self.quantity} in stock)"
    
    def update_quantity(self, amount):
        """
        # Method: update_quantity
        # Updates the quantity of the item in stock
        #
        # Parameters:
        # - amount: The amount to add (positive) or subtract (negative)
        #
        # Returns:
        # - bool: True if update was successful, False if it would result in negative stock
        """
        new_quantity = self.quantity + amount
        if new_quantity < 0:
            return False
        self.quantity = new_quantity
        return True
    
    def is_available(self, requested_quantity=1):
        """
        # Method: is_available
        # Checks if the requested quantity is available in stock
        #
        # Parameters:
        # - requested_quantity: The quantity requested (default: 1)
        #
        # Returns:
        # - bool: True if available, False otherwise
        """
        return self.quantity >= requested_quantity
    
    def apply_discount(self, percentage):
        """
        # Method: apply_discount
        # Applies a discount percentage to the food item
        #
        # Parameters:
        # - percentage: Discount percentage (0-100)
        #
        # Returns:
        # - float: The discounted price
        """
        if 0 <= percentage <= 100:
            self.discount_percentage = percentage
            return True
        return False
    
    def get_discounted_price(self):
        """
        # Method: get_discounted_price
        # Calculates and returns the price after applying any discount
        #
        # Returns:
        # - float: The price after discount
        """
        return self.price * (1 - self.discount_percentage / 100)
    
    def add_ingredient(self, ingredient):
        """
        # Method: add_ingredient
        # Adds a new ingredient to the food item
        #
        # Parameters:
        # - ingredient: The ingredient to add
        """
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)
            return True
        return False
    
    def remove_ingredient(self, ingredient):
        """
        # Method: remove_ingredient
        # Removes an ingredient from the food item
        #
        # Parameters:
        # - ingredient: The ingredient to remove
        #
        # Returns:
        # - bool: True if removed, False if not found
        """
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            return True
        return False