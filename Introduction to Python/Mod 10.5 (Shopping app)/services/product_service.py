"""
Product Service Module

This module provides functionality for managing products in the e-shopping app.
"""

from models.product import Product
from utils.database import Database

class ProductService:
    """
    Service class for handling product-related operations.
    
    This class demonstrates the separation of concerns principle by
    encapsulating all product-related functionality.
    """
    
    def __init__(self):
        """Initialize the product service."""
        self.db = Database()
    
    def add_product(self, name, description, price, stock, seller_id, category="Uncategorized"):
        """
        Add a new product.
        
        Args:
            name (str): Product name
            description (str): Product description
            price (float): Product price
            stock (int): Initial stock quantity
            seller_id (str): ID of the seller
            category (str, optional): Product category. Defaults to "Uncategorized".
            
        Returns:
            tuple: (success (bool), message (str), product_id (str or None))
        """
        try:
            # Input validation
            if not name or not description:
                return False, "Name and description cannot be empty", None
            
            # Generate a unique product ID
            product_id = self.db.generate_product_id()
            
            # Create the product
            product = Product(product_id, name, description, price, stock, seller_id, category)
            
            # Add the product to the database
            self.db.add_product(product)
            
            return True, "Product added successfully", product_id
        
        except ValueError as e:
            return False, str(e), None
    
    def update_product(self, product_id, **kwargs):
        """
        Update an existing product.
        
        Args:
            product_id (str): ID of the product to update
            **kwargs: Product attributes to update (name, description, price, stock, category)
            
        Returns:
            tuple: (success (bool), message (str))
        """
        product = self.db.get_product_by_id(product_id)
        
        if not product:
            return False, "Product not found"
        
        try:
            # Update product attributes based on provided kwargs
            if 'price' in kwargs:
                product.price = kwargs['price']
            
            if 'stock' in kwargs:
                product.stock = kwargs['stock']
            
            if 'category' in kwargs:
                product.category = kwargs['category']
            
            # Note: name, description, and seller_id are not mutable
            
            return True, "Product updated successfully"
        
        except ValueError as e:
            return False, str(e)
    
    def delete_product(self, product_id):
        """
        Delete a product.
        
        Args:
            product_id (str): ID of the product to delete
            
        Returns:
            tuple: (success (bool), message (str))
        """
        if not self.db.get_product_by_id(product_id):
            return False, "Product not found"
        
        if self.db.remove_product(product_id):
            return True, "Product deleted successfully"
        return False, "Failed to delete product"
    
    def get_product(self, product_id):
        """
        Get a product by its ID.
        
        Args:
            product_id (str): ID of the product to get
            
        Returns:
            Product or None: The product if found, None otherwise
        """
        return self.db.get_product_by_id(product_id)
    
    def get_all_products(self):
        """
        Get all products.
        
        Returns:
            list: List of all products
        """
        return self.db.get_all_products()
    
    def get_products_by_seller(self, seller_id):
        """
        Get all products by a specific seller.
        
        Args:
            seller_id (str): ID of the seller
            
        Returns:
            list: List of the seller's products
        """
        return self.db.get_products_by_seller(seller_id)
    
    def get_available_products(self):
        """
        Get all products that are in stock.
        
        Returns:
            list: List of products that are in stock
        """
        all_products = self.db.get_all_products()
        return [p for p in all_products if p.is_in_stock()]
    
    def search_products(self, keyword):
        """
        Search for products by keyword in name or description.
        
        Args:
            keyword (str): Search keyword
            
        Returns:
            list: List of products matching the search keyword
        """
        all_products = self.db.get_all_products()
        keyword = keyword.lower()
        
        return [p for p in all_products if keyword in p.name.lower() or keyword in p.description.lower()]
    
    def filter_products_by_category(self, category):
        """
        Filter products by category.
        
        Args:
            category (str): Category to filter by
            
        Returns:
            list: List of products in the specified category
        """
        all_products = self.db.get_all_products()
        return [p for p in all_products if p.category.lower() == category.lower()]
    
    def update_stock(self, product_id, quantity):
        """
        Update the stock of a product.
        
        Args:
            product_id (str): ID of the product
            quantity (int): New stock quantity
            
        Returns:
            tuple: (success (bool), message (str))
        """
        product = self.db.get_product_by_id(product_id)
        
        if not product:
            return False, "Product not found"
        
        try:
            product.stock = quantity
            return True, f"Stock updated successfully: {quantity} items"
        except ValueError as e:
            return False, str(e)