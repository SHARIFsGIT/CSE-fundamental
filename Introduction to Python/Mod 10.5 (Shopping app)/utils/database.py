"""
Database Utility Module

This module simulates a simple in-memory database for storing application data.
In a real application, this would be replaced with a proper database system.
"""

class Database:
    """
    Simple in-memory database to store application data.
    
    This class demonstrates the Singleton pattern to ensure only one
    database instance exists throughout the application.
    """
    
    _instance = None
    
    def __new__(cls):
        """
        Create a new Database instance if one doesn't exist already.
        This implements the Singleton pattern.
        
        Returns:
            Database: The singleton Database instance
        """
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            # Initialize data stores dictionaries
            cls._instance._users = {}
            cls._instance._products = {}
            cls._instance._orders = {}
            # Initialize ID counters
            cls._instance._user_id_counter = 1
            cls._instance._product_id_counter = 1
            cls._instance._order_id_counter = 1
        return cls._instance
    
    def add_user(self, user):
        """
        Add a user to the database.
        
        Args:
            user: User object to add
            
        Returns:
            str: The user ID
        """
        # Store the user in a dictionary using user_id as the key
        self._users[user.user_id] = user
        return user.user_id
    
    def get_user_by_id(self, user_id):
        """
        Get a user by their ID.
        
        Args:
            user_id (str): ID of the user to get
            
        Returns:
            User or None: The user if found, None otherwise
        """
        return self._users.get(user_id)
    
    def get_user_by_email(self, email):
        """
        Get a user by their email.
        
        Args:
            email (str): Email of the user to get
            
        Returns:
            User or None: The user if found, None otherwise
        """
        for user in self._users.values():
            if user.email == email:
                return user
        return None
    
    def generate_user_id(self):
        """
        Generate a unique user ID.
        
        Returns:
            str: A new unique user ID
        """
        user_id = f"USER_{self._user_id_counter:04d}"
        self._user_id_counter += 1
        return user_id
    
    def add_product(self, product):
        """
        Add a product to the database.
        
        Args:
            product: Product object to add
            
        Returns:
            str: The product ID
        """
        self._products[product.product_id] = product
        return product.product_id
    
    def get_product_by_id(self, product_id):
        """
        Get a product by its ID.
        
        Args:
            product_id (str): ID of the product to get
            
        Returns:
            Product or None: The product if found, None otherwise
        """
        return self._products.get(product_id)
    
    def get_all_products(self):
        """
        Get all products in the database.
        
        Returns:
            list: List of all products
        """
        return list(self._products.values())
    
    def get_products_by_seller(self, seller_id):
        """
        Get all products by a specific seller.
        
        Args:
            seller_id (str): ID of the seller
            
        Returns:
            list: List of the seller's products
        """
        return [p for p in self._products.values() if p.seller_id == seller_id]
    
    def remove_product(self, product_id):
        """
        Remove a product from the database.
        
        Args:
            product_id (str): ID of the product to remove
            
        Returns:
            bool: True if the product was removed, False otherwise
        """
        if product_id in self._products:
            del self._products[product_id]
            return True
        return False
    
    def generate_product_id(self):
        """
        Generate a unique product ID.
        
        Returns:
            str: A new unique product ID
        """
        product_id = f"PROD_{self._product_id_counter:04d}"
        self._product_id_counter += 1
        return product_id
    
    def add_order(self, order):
        """
        Add an order to the database.
        
        Args:
            order: Order object to add
            
        Returns:
            str: The order ID
        """
        self._orders[order.order_id] = order
        return order.order_id
    
    def get_order_by_id(self, order_id):
        """
        Get an order by its ID.
        
        Args:
            order_id (str): ID of the order to get
            
        Returns:
            Order or None: The order if found, None otherwise
        """
        return self._orders.get(order_id)
    
    def get_orders_by_customer(self, customer_id):
        """
        Get all orders by a specific customer.
        
        Args:
            customer_id (str): ID of the customer
            
        Returns:
            list: List of the customer's orders
        """
        return [o for o in self._orders.values() if o.customer_id == customer_id]
    
    def generate_order_id(self):
        """
        Generate a unique order ID.
        
        Returns:
            str: A new unique order ID
        """
        order_id = f"ORD_{self._order_id_counter:04d}"
        self._order_id_counter += 1
        return order_id