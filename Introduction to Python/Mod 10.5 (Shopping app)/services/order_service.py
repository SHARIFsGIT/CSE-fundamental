"""
Order Service Module

This module provides functionality for managing orders in the e-shopping app.
"""

from models.order import Order
from utils.database import Database

class OrderService:
    """
    Service class for handling order-related operations.
    
    This class demonstrates the separation of concerns principle by
    encapsulating all order-related functionality.
    """
    
    def __init__(self):
        """Initialize the order service."""
        self.db = Database()
    
    def create_order(self, customer_id, cart_items):
        """
        Create a new order for a customer.
        
        Args:
            customer_id (str): ID of the customer placing the order
            cart_items (list): List of Product objects in the customer's cart
            
        Returns:
            tuple: (success (bool), message (str), order_id (str or None))
        """
        # Validate inputs
        if not cart_items:
            return False, "Cart is empty", None
        
        # Check if all items are in stock
        for item in cart_items:
            if not item.is_in_stock():
                return False, f"Product '{item.name}' is out of stock", None
        
        # Decrease stock for each item
        for item in cart_items:
            if not item.decrease_stock(1):
                # This shouldn't happen since we already checked above, but just in case
                return False, f"Not enough stock for product '{item.name}'", None
        
        # Generate a unique order ID
        order_id = self.db.generate_order_id()
        
        # Create the order
        order = Order(order_id, customer_id, cart_items)
        
        # Save the order to the database
        self.db.add_order(order)
        
        return True, "Order created successfully", order_id
    
    def get_order(self, order_id):
        """
        Get an order by its ID.
        
        Args:
            order_id (str): ID of the order to get
            
        Returns:
            Order or None: The order if found, None otherwise
        """
        return self.db.get_order_by_id(order_id)
    
    def get_customer_orders(self, customer_id):
        """
        Get all orders for a specific customer.
        
        Args:
            customer_id (str): ID of the customer
            
        Returns:
            list: List of the customer's orders
        """
        return self.db.get_orders_by_customer(customer_id)
    
    def update_order_status(self, order_id, new_status):
        """
        Update the status of an order.
        
        Args:
            order_id (str): ID of the order to update
            new_status (str): New status for the order
            
        Returns:
            tuple: (success (bool), message (str))
        """
        order = self.db.get_order_by_id(order_id)
        
        if not order:
            return False, "Order not found"
        
        try:
            order.update_status(new_status)
            return True, f"Order status updated to: {new_status}"
        except ValueError as e:
            return False, str(e)
    
    def cancel_order(self, order_id):
        """
        Cancel an order.
        
        Args:
            order_id (str): ID of the order to cancel
            
        Returns:
            tuple: (success (bool), message (str))
        """
        order = self.db.get_order_by_id(order_id)
        
        if not order:
            return False, "Order not found"
        
        # Try to cancel the order
        if not order.cancel():
            return False, f"Cannot cancel order with status: {order.status}"
        
        # Restore stock for each item in the order
        for item in order.items:
            product = self.db.get_product_by_id(item.product_id)
            if product:
                product.stock += 1
        
        return True, "Order canceled successfully"