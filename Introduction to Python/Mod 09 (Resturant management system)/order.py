# -------------------- Order Class --------------------
from datetime import datetime

class Order:
    """
    Represents a customer's order containing food items and their quantities.
    """
    def __init__(self):
        self.items = {}  # Dictionary with food_item objects as keys and quantities as values
        self.order_time = None
        self.order_id = None
        self.status = "Cart"  # Cart, Placed, Preparing, Ready, Delivered, Cancelled

    def add_item(self, item, quantity):
        """Add a food item to the order with specified quantity."""
        if not item.is_available(quantity):
            print(f"Sorry, only {item.quantity} of {item.name} available.")
            return False
            
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        
        return True

    def remove_item(self, item):
        """Remove a food item from the order."""
        if item in self.items:
            del self.items[item]
            return True
        return False
        
    def update_item_quantity(self, item, new_quantity):
        """Update the quantity of a food item in the order."""
        if item not in self.items:
            return False
            
        if new_quantity <= 0:
            return self.remove_item(item)
            
        self.items[item] = new_quantity
        return True

    def calculate_total_price(self):
        """Calculate the total price of all items in the order."""
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear_cart(self):
        """Clear all items from the order."""
        self.items.clear()
        
    def place_order(self):
        """Mark the order as placed and record the time."""
        if not self.items:
            print("Cannot place an empty order.")
            return False
            
        self.order_time = datetime.now()
        # Generate a simple order ID: timestamp + first 3 letters of each item
        item_codes = ''.join([item.name[:3].upper() for item in self.items.keys()][:3])
        self.order_id = f"{self.order_time.strftime('%Y%m%d%H%M%S')}-{item_codes}"
        self.status = "Placed"
        return True
        
    def is_empty(self):
        """Check if the order is empty."""
        return len(self.items) == 0
        
    def item_count(self):
        """Get the total number of items in the order."""
        return sum(quantity for quantity in self.items.values())