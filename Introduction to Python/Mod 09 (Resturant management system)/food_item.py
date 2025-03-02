# -------------------- FoodItem Class --------------------

class FoodItem:
    """
    Represents a food item in the restaurant with name, price, and quantity.
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity  # Quantity in stock
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.quantity} in stock)"
    
    def update_quantity(self, amount):
        """Update the quantity of the item in stock."""
        new_quantity = self.quantity + amount
        if new_quantity < 0:
            return False
        self.quantity = new_quantity
        return True
    
    def is_available(self, requested_quantity=1):
        """Check if the requested quantity is available in stock."""
        return self.quantity >= requested_quantity