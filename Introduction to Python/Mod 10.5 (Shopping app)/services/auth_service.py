"""
Authentication Service Module

This module provides authentication functionality for users,
including registration and login.
"""

from models.user import Customer, Seller
from utils.database import Database

class AuthService:
    """
    Service class for handling user authentication.
    
    This class demonstrates the separation of concerns principle by
    encapsulating all authentication-related functionality.
    """
    
    def __init__(self):
        """Initialize the authentication service."""
        self.db = Database()
    
    def register_customer(self, email, password, name):
        """
        Register a new customer.
        
        Args:
            email (str): Customer's email address
            password (str): Customer's password
            name (str): Customer's name
            
        Returns:
            tuple: (success (bool), message (str), user_id (str or None))
        """
        # Check if email is already in use
        existing_user = self.db.get_user_by_email(email)
        if existing_user:
            return False, "Email already registered", None
        
        # Create new customer
        user_id = self.db.generate_user_id()
        customer = Customer(user_id, email, password, name)
        self.db.add_user(customer)
        
        return True, "Customer registered successfully", user_id
    
    def register_seller(self, email, password, name):
        """
        Register a new seller.
        
        Args:
            email (str): Seller's email address
            password (str): Seller's password
            name (str): Seller's name
            
        Returns:
            tuple: (success (bool), message (str), user_id (str or None))
        """
        # Check if email is already in use
        existing_user = self.db.get_user_by_email(email)
        if existing_user:
            return False, "Email already registered", None
        
        # Create new seller
        user_id = self.db.generate_user_id()
        seller = Seller(user_id, email, password, name)
        self.db.add_user(seller)
        
        return True, "Seller registered successfully", user_id
    
    def login(self, email, password):
        """
        Authenticate a user with email and password.
        
        Args:
            email (str): User's email address
            password (str): User's password
            
        Returns:
            tuple: (success (bool), message (str), user_id (str or None))
        """
        user = self.db.get_user_by_email(email)
        
        if not user:
            return False, "Email not found", None
        
        if not user.authenticate(password):
            return False, "Incorrect password", None
        
        return True, "Login successful", user.user_id
    
    def get_user(self, user_id):
        """
        Get a user by their ID.
        
        Args:
            user_id (str): ID of the user to get
            
        Returns:
            User or None: The user if found, None otherwise
        """
        return self.db.get_user_by_id(user_id)
    
    def is_customer(self, user_id):
        """
        Check if a user is a customer.
        
        Args:
            user_id (str): ID of the user to check
            
        Returns:
            bool: True if the user is a customer, False otherwise
        """
        user = self.db.get_user_by_id(user_id)
        return user is not None and isinstance(user, Customer)
    
    def is_seller(self, user_id):
        """
        Check if a user is a seller.
        
        Args:
            user_id (str): ID of the user to check
            
        Returns:
            bool: True if the user is a seller, False otherwise
        """
        user = self.db.get_user_by_id(user_id)
        return user is not None and isinstance(user, Seller)