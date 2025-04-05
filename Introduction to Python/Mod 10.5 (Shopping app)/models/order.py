"""
Order Model Module

This module defines the Order class which represents a customer's purchase.
"""

import datetime

class Order:
    """
    Order class representing a customer's purchase.
    
    Attributes:
        order_id (str): Unique identifier for the order
        customer_id (str): ID of the customer who placed the order
        items (list): List of products in the order
        total_price (float): Total price of all items in the order
        date (datetime): Date and time when the order was placed
        status (str): Current status of the order
    """
    
    # Class constants for order status
    STATUS_PENDING = "Pending"
    STATUS_PROCESSING = "Processing"
    STATUS_SHIPPED = "Shipped"
    STATUS_DELIVERED = "Delivered"
    STATUS_CANCELED = "Canceled"
    
    def __init__(self, order_id, customer_id, items):
        """
        Initialize a new Order object.
        
        Args:
            order_id (str): Unique identifier for the order
            customer_id (str): ID of the customer who placed the order
            items (list): List of products in the order
        """
        self._order_id = order_id
        self._customer_id = customer_id
        self._items = items
        self._total_price = sum(item.price for item in items)
        self._date = datetime.datetime.now()
        self._status = self.STATUS_PENDING
    
    @property
    def order_id(self):
        """Get the order ID."""
        return self._order_id
    
    @property
    def customer_id(self):
        """Get the customer ID."""
        return self._customer_id
    
    @property
    def items(self):
        """Get the list of items in the order."""
        return self._items
    
    @property
    def total_price(self):
        """Get the total price of the order."""
        return self._total_price
    
    @property
    def date(self):
        """Get the date and time when the order was placed."""
        return self._date
    
    @property
    def status(self):
        """Get the current status of the order."""
        return self._status
    
    def update_status(self, new_status):
        """
        Update the status of the order.
        
        Args:
            new_status (str): New status for the order
            
        Raises:
            ValueError: If the new status is not valid
        """
        valid_statuses = [
            self.STATUS_PENDING,
            self.STATUS_PROCESSING,
            self.STATUS_SHIPPED,
            self.STATUS_DELIVERED,
            self.STATUS_CANCELED
        ]
        
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}")
        
        self._status = new_status
        print(f"Order {self._order_id} status updated to: {new_status}")
    
    def cancel(self):
        """
        Cancel the order.
        
        Returns:
            bool: True if the order was canceled, False otherwise
        """
        if self._status in [self.STATUS_DELIVERED, self.STATUS_CANCELED]:
            print(f"Cannot cancel order with status: {self._status}")
            return False
        
        self._status = self.STATUS_CANCELED
        print(f"Order {self._order_id} has been canceled.")
        return True
    
    def __str__(self):
        """Return a string representation of the order."""
        return (f"Order #{self._order_id} - {self._status}\n"
                f"Date: {self._date}\n"
                f"Items: {len(self._items)}\n"
                f"Total: ${self._total_price:.2f}")
    
    def get_details(self):
        """
        Get detailed information about the order.
        
        Returns:
            str: Detailed string representation of the order
        """
        details = str(self) + "\nItems:\n"
        for i, item in enumerate(self._items, 1):
            details += f"{i}. {item.name} - ${item.price:.2f}\n"
        return details