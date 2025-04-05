"""
Product Model Module

This module defines the Product class which represents items that can be sold in the e-shopping app.
"""

class Product:
    """
    Product class representing items that can be bought and sold.
    
    Attributes:
        product_id (str): Unique identifier for the product
        name (str): Product name
        description (str): Product description
        price (float): Product price
        stock (int): Available quantity
        seller_id (str): ID of the seller who published this product
        category (str): Product category
    """
    
    def __init__(self, product_id, name, description, price, stock, seller_id, category="Uncategorized"):
        """
        Initialize a new Product object.
        
        Args:
            product_id (str): Unique identifier for the product
            name (str): Product name
            description (str): Product description
            price (float): Product price
            stock (int): Available quantity
            seller_id (str): ID of the seller who published this product
            category (str, optional): Product category. Defaults to "Uncategorized".
        
        Raises:
            ValueError: If price is negative or stock is negative
        """
        self._product_id = product_id
        self._name = name
        self._description = description
        
        # Input validation for price and stock
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        self._price = price
        
        if stock < 0:
            raise ValueError("Stock cannot be negative")
        
        self._stock = stock
        
        self._seller_id = seller_id
        self._category = category
    
    @property
    def product_id(self):
        """Get the product ID."""
        return self._product_id
    
    @property
    def name(self):
        """Get the product name."""
        return self._name
    
    @property
    def description(self):
        """Get the product description."""
        return self._description
    
    @property
    def price(self):
        """Get the product price."""
        return self._price
    
    @price.setter
    def price(self, value):
        """
        Set the product price.
        
        Args:
            value (float): New price value
            
        Raises:
            ValueError: If price is negative
        """
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @property
    def stock(self):
        """Get the product stock level."""
        return self._stock
    
    @stock.setter
    def stock(self, value):
        """
        Set the product stock level.
        
        Args:
            value (int): New stock value
            
        Raises:
            ValueError: If stock is negative
        """
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value
    
    @property
    def seller_id(self):
        """Get the seller ID."""
        return self._seller_id
    
    @property
    def category(self):
        """Get the product category."""
        return self._category
    
    @category.setter
    def category(self, value):  # key | value
        """Set the product category."""
        self._category = value
    
    def is_in_stock(self):
        """
        Check if the product is in stock.
        
        Returns:
            bool: True if stock > 0, False otherwise
        """
        return self._stock > 0
    
    def decrease_stock(self, quantity=1):
        """
        Decrease the stock by the given quantity.
        
        Args:
            quantity (int, optional): Quantity to decrease by. Defaults to 1.
            
        Returns:
            bool: True if stock was decreased, False if not enough stock
            
        Raises:
            ValueError: If quantity is negative
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        if self._stock >= quantity:
            self._stock -= quantity
            return True
        return False
    
    def __str__(self):
        """Return a string representation of the product."""
        stock_status = "In Stock" if self.is_in_stock() else "Out of Stock"
        return f"{self._name} - ${self._price:.2f} ({stock_status}, {self._stock} remaining)"