"""
User Model Module

This module defines the User base class and its subclasses (Customer and Seller).
It demonstrates inheritance and encapsulation principles in OOP.
"""

class User:
    """
    Base User class that contains common attributes and methods for all users.
    
    Attributes:
        user_id (str): Unique identifier for the user
        email (str): User's email address
        password (str): User's password (in a real app, this would be hashed)
        name (str): User's full name
    """
    
    def __init__(self, user_id, email, password, name):
        """
        Initialize a new User object.
        
        Args:
            user_id (str): Unique identifier for the user
            email (str): User's email address
            password (str): User's password
            name (str): User's full name
        """
        self._user_id = user_id  # Protected attribute (indicated by _)
        self._email = email
        self._password = password
        self._name = name
    
    @property
    def user_id(self):
        """Get the user's ID."""
        return self._user_id
    
    @property
    def email(self):
        """Get the user's email."""
        return self._email
    
    @property
    def name(self):
        """Get the user's name."""
        return self._name
    
    def authenticate(self, password):
        """
        Authenticate a user by checking their password.
        
        Args:
            password (str): Password to check
            
        Returns:
            bool: True if password matches, False otherwise
        """
        return self._password == password
    
    def __str__(self):
        """Return a string representation of the user."""
        return f"User: {self._name} ({self._email})"


class Customer(User):
    """
    Customer class that inherits from User.
    Represents a customer who can browse products and place orders.
    
    Attributes:
        cart (list): List of products in the customer's shopping cart
        order_history (list): List of the customer's past orders
    """
    
    def __init__(self, user_id, email, password, name):
        """
        Initialize a new Customer object.
        
        Args:
            user_id (str): Unique identifier for the customer
            email (str): Customer's email address
            password (str): Customer's password
            name (str): Customer's full name
        """
        # Call parent class constructor
        super().__init__(user_id, email, password, name)
        self._cart = []
        self._order_history = []
    
    @property
    def cart(self):
        """Get the customer's shopping cart."""
        return self._cart
    
    @property
    def order_history(self):
        """Get the customer's order history."""
        return self._order_history
    
    def add_to_cart(self, product):
        """
        Add a product to the customer's cart.
        
        Args:
            product: Product object to add to cart
        """
        self._cart.append(product)
        print(f"Added {product.name} to cart.")
    
    def remove_from_cart(self, product_id):
        """
        Remove a product from the customer's cart.
        
        Args:
            product_id (str): ID of the product to remove
            
        Returns:
            bool: True if product was removed, False if not found
        """
        for i, product in enumerate(self._cart):
            if product.product_id == product_id:
                del self._cart[i]
                print(f"Removed {product.name} from cart.")
                return True
        print("Product not found in cart.")
        return False
    
    def clear_cart(self):
        """Clear all items from the cart."""
        self._cart = []
        print("Cart cleared.")
    
    def add_order_to_history(self, order):
        """
        Add an order to the customer's order history.
        
        Args:
            order: Order object to add to history
        """
        self._order_history.append(order)
    
    def __str__(self):
        """Return a string representation of the customer."""
        return f"Customer: {self._name} ({self._email})"


class Seller(User):
    """
    Seller class that inherits from User.
    Represents a seller who can publish and manage products.
    
    Attributes:
        products (list): List of products that the seller has published
    """
    
    def __init__(self, user_id, email, password, name):
        """
        Initialize a new Seller object.
        
        Args:
            user_id (str): Unique identifier for the seller
            email (str): Seller's email address
            password (str): Seller's password
            name (str): Seller's full name
        """
        # Call parent class constructor
        super().__init__(user_id, email, password, name)
        self._products = []
    
    @property
    def products(self):
        """Get the seller's published products."""
        return self._products
    
    def add_product(self, product):
        """
        Add a product to the seller's inventory.
        
        Args:
            product: Product object to add
        """
        self._products.append(product)
        print(f"Added product: {product.name}")
    
    def remove_product(self, product_id):
        """
        Remove a product from the seller's inventory.
        
        Args:
            product_id (str): ID of the product to remove
            
        Returns:
            bool: True if product was removed, False if not found
        """
        for i, product in enumerate(self._products):
            if product.product_id == product_id:
                del self._products[i]
                print(f"Removed product: {product.name}")
                return True
        print("Product not found in inventory.")
        return False
    
    def update_product_stock(self, product_id, quantity):
        """
        Update the stock quantity of a product.
        
        Args:
            product_id (str): ID of the product to update
            quantity (int): New quantity
            
        Returns:
            bool: True if product was updated, False if not found
        """
        for product in self._products:
            if product.product_id == product_id:
                product.stock = quantity
                print(f"Updated stock for {product.name} to {quantity}.")
                return True
        print("Product not found in inventory.")
        return False
    
    def __str__(self):
        """Return a string representation of the seller."""
        return f"Seller: {self._name} ({self._email})"