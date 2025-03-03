# -------------------- Order Class --------------------
"""
This module defines the Order class for the restaurant management system.
The Order class manages a customer's order, including items, quantities, and status.
"""
from datetime import datetime
import uuid

class Order:
    """
    # Class: Order
    # Purpose: Represents a customer's order containing food items and their quantities
    #
    # Properties:
    # - items: Dictionary with food_item objects as keys and quantities as values
    # - order_time: The time when the order was placed
    # - order_id: Unique identifier for the order
    # - status: Current status of the order
    # - customer_id: ID of the customer who placed the order (new)
    # - table_number: Restaurant table number (for dine-in orders) (new)
    # - delivery_address: Address for delivery (for delivery orders) (new)
    # - special_instructions: Any special instructions for the order (new)
    # - payment_method: Method of payment (new)
    """
    
    # Class attribute - used to track all possible order statuses
    ORDER_STATUSES = [
        "Cart",       # Initial status (items in cart, not placed)
        "Placed",     # Order has been placed but not yet processed
        "Preparing",  # Kitchen is preparing the order
        "Ready",      # Order is ready for pickup/delivery
        "Delivered",  # Order has been delivered to the customer
        "Cancelled"   # Order has been cancelled
    ]
    
    def __init__(self):
        """
        # Constructor
        # Initializes a new instance of the Order class
        """
        # Instance attributes/properties
        self.items = {}  # Dictionary with food_item objects as keys and quantities as values
        self.order_time = None
        self.order_id = None
        self.status = "Cart"  # Initial status
        
        # Additional attributes for enhanced functionality
        self.customer_id = None
        self.table_number = None
        self.delivery_address = None
        self.special_instructions = ""
        self.payment_method = None
        self.payment_status = "Pending"  # Can be "Pending", "Paid", or "Refunded"
        self.last_updated = datetime.now()
        self.notes = []  # List to track order history/notes

    def add_item(self, item, quantity):
        """
        # Method: add_item
        # Adds a food item to the order with specified quantity
        #
        # Parameters:
        # - item: The FoodItem object to add
        # - quantity: The quantity to add
        #
        # Returns:
        # - bool: True if added successfully, False if not enough in stock
        """
        # Check if the requested quantity is available
        if not item.is_available(quantity):
            print(f"Sorry, only {item.quantity} of {item.name} available.")
            return False
        
        # Add to existing quantity if the item is already in the order
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        
        # Add note about the addition
        self._add_note(f"Added {quantity} x {item.name} to order")
        return True

    def remove_item(self, item):
        """
        # Method: remove_item
        # Removes a food item from the order
        #
        # Parameters:
        # - item: The FoodItem object to remove
        #
        # Returns:
        # - bool: True if removed successfully, False if not in order
        """
        if item in self.items:
            quantity = self.items[item]
            del self.items[item]
            
            # Add note about the removal
            self._add_note(f"Removed {quantity} x {item.name} from order")
            return True
        return False
        
    def update_item_quantity(self, item, new_quantity):
        """
        # Method: update_item_quantity
        # Updates the quantity of a food item in the order
        #
        # Parameters:
        # - item: The FoodItem object to update
        # - new_quantity: The new quantity
        #
        # Returns:
        # - bool: True if updated successfully, False if not in order or invalid quantity
        """
        if item not in self.items:
            return False
            
        if new_quantity <= 0:
            return self.remove_item(item)
        
        old_quantity = self.items[item]
        self.items[item] = new_quantity
        
        # Add note about the quantity update
        self._add_note(f"Updated {item.name} quantity from {old_quantity} to {new_quantity}")
        return True

    def calculate_total_price(self):
        """
        # Method: calculate_total_price
        # Calculates the total price of all items in the order
        #
        # Returns:
        # - float: The total price
        """
        return sum(item.get_discounted_price() * quantity for item, quantity in self.items.items())

    def calculate_subtotal(self):
        """
        # Method: calculate_subtotal
        # Calculates the subtotal before taxes and fees
        #
        # Returns:
        # - float: The subtotal
        """
        return self.calculate_total_price()
    
    def calculate_tax(self, tax_rate=0.05):
        """
        # Method: calculate_tax
        # Calculates the tax amount based on the subtotal
        #
        # Parameters:
        # - tax_rate: The tax rate (default: 5%)
        #
        # Returns:
        # - float: The tax amount
        """
        return self.calculate_subtotal() * tax_rate
    
    def calculate_grand_total(self, tax_rate=0.05, delivery_fee=0):
        """
        # Method: calculate_grand_total
        # Calculates the grand total including tax and delivery fee
        #
        # Parameters:
        # - tax_rate: The tax rate (default: 5%)
        # - delivery_fee: The delivery fee (default: 0)
        #
        # Returns:
        # - float: The grand total
        """
        return self.calculate_subtotal() + self.calculate_tax(tax_rate) + delivery_fee

    def clear_cart(self):
        """
        # Method: clear_cart
        # Clears all items from the order
        """
        self.items.clear()
        self._add_note("Cart cleared")
        
    def place_order(self, customer_id=None, table_number=None, delivery_address=None):
        """
        # Method: place_order
        # Marks the order as placed and records the time
        #
        # Parameters:
        # - customer_id: ID of the customer placing the order (optional)
        # - table_number: Table number for dine-in orders (optional)
        # - delivery_address: Address for delivery orders (optional)
        #
        # Returns:
        # - bool: True if the order was placed successfully, False otherwise
        """
        if not self.items:
            print("Cannot place an empty order.")
            return False
        
        # Set order details
        self.order_time = datetime.now()
        self.customer_id = customer_id
        self.table_number = table_number
        self.delivery_address = delivery_address
        
        # Generate a unique order ID
        # Format: YYYYMMDD-HHMMSS-XXXX (where XXXX is a short UUID)
        timestamp = self.order_time.strftime('%Y%m%d-%H%M%S')
        short_uuid = str(uuid.uuid4())[:8]  # First 8 characters of a UUID
        self.order_id = f"{timestamp}-{short_uuid}"
        
        # Update status
        self.status = "Placed"
        
        # Add note about placing the order
        self._add_note(f"Order placed by customer {customer_id or 'Anonymous'}")
        
        return True
        
    def update_status(self, new_status):
        """
        # Method: update_status
        # Updates the status of the order
        #
        # Parameters:
        # - new_status: The new status
        #
        # Returns:
        # - bool: True if updated successfully, False if invalid status
        """
        if new_status not in self.ORDER_STATUSES:
            print(f"Invalid status: {new_status}")
            return False
            
        old_status = self.status
        self.status = new_status
        self.last_updated = datetime.now()
        
        # Add note about the status change
        self._add_note(f"Status changed from {old_status} to {new_status}")
        
        return True
    
    def _add_note(self, note):
        """
        # Private Method: _add_note
        # Adds a note to the order's history with timestamp
        #
        # Parameters:
        # - note: The note to add
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.notes.append(f"{timestamp}: {note}")
        self.last_updated = datetime.now()
        
    def add_special_instructions(self, instructions):
        """
        # Method: add_special_instructions
        # Adds special instructions to the order
        #
        # Parameters:
        # - instructions: The special instructions
        """
        self.special_instructions = instructions
        self._add_note(f"Special instructions added: {instructions}")
        
    def set_payment_method(self, method):
        """
        # Method: set_payment_method
        # Sets the payment method for the order
        #
        # Parameters:
        # - method: The payment method
        """
        self.payment_method = method
        self._add_note(f"Payment method set to: {method}")
        
    def mark_as_paid(self):
        """
        # Method: mark_as_paid
        # Marks the order as paid
        """
        self.payment_status = "Paid"
        self._add_note(f"Payment received via {self.payment_method}")
        
    def is_empty(self):
        """
        # Method: is_empty
        # Checks if the order is empty
        #
        # Returns:
        # - bool: True if empty, False otherwise
        """
        return len(self.items) == 0
        
    def item_count(self):
        """
        # Method: item_count
        # Gets the total number of items in the order
        #
        # Returns:
        # - int: Total number of items
        """
        return sum(quantity for quantity in self.items.values())
    
    def get_order_summary(self):
        """
        # Method: get_order_summary
        # Returns a formatted summary of the order
        #
        # Returns:
        # - str: Formatted order summary
        """
        summary = []
        summary.append(f"Order ID: {self.order_id}")
        summary.append(f"Status: {self.status}")
        summary.append(f"Time: {self.order_time}")
        summary.append(f"Items: {self.item_count()}")
        
        if self.customer_id:
            summary.append(f"Customer: {self.customer_id}")
        
        if self.table_number:
            summary.append(f"Table: {self.table_number}")
        
        if self.delivery_address:
            summary.append(f"Delivery: {self.delivery_address}")
        
        summary.append(f"Total: ${self.calculate_total_price():.2f}")
        
        return "\n".join(summary)
    
    def __str__(self):
        """
        # Magic/Dunder Method: __str__
        # Returns a string representation of the order
        # Used when str() is called on an instance
        """
        if not self.order_id:
            return f"Shopping Cart with {self.item_count()} items"
        return f"Order {self.order_id} ({self.status}): {self.item_count()} items, ${self.calculate_total_price():.2f}"