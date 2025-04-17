"""
Banking Management System - Bank Module
This module defines the Bank class which manages users and administrators.

For beginners:
- This file contains the Bank class that serves as the central database
- It manages all users and admins in the system
- It provides methods to calculate total balance, track loans, etc.
- The Bank class connects the User and Admin classes together
"""

import datetime
import json

class Bank:
    """
    Represents the bank which manages all users and financial operations.
    
    Attributes:
        _users (list): List of all User objects (private)
        _admins (list): List of all Admin objects (private)
        _total_loan (float): Total outstanding loan amount (private)
        _loan_enabled (bool): Whether the loan feature is enabled (private)
        _interest_rate (float): Current loan interest rate (private)
        _transaction_log (list): Log of all bank-wide transactions (private)
    """
    
    def __init__(self):
        """Initialize a new bank with default settings."""
        # Private attributes (indicated by underscore prefix)
        self._users = []
        self._admins = []
        self._total_loan = 0.0
        self._loan_enabled = True
        self._interest_rate = 8.5  # Default interest rate (8.5%)
        self._transaction_log = []
        self._last_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Log bank creation
        self._log_transaction("Bank system initialized")
    
    def add_user(self, user):
        """
        Add a user to the bank.
        
        Args:
            user (User): The user object to add
        """
        self._users.append(user)
        self._log_transaction(f"New user added: {user.username}")
    
    def add_admin(self, admin):
        """
        Add an admin to the bank.
        
        Args:
            admin (Admin): The admin object to add
        """
        self._admins.append(admin)
        self._log_transaction(f"New admin added: {admin.username}")
    
    def user_exists(self, username):
        """
        Check if a user with the given username exists.
        
        Args:
            username (str): The username to check
            
        Returns:
            bool: True if user exists, False otherwise
        """
        return any(user.username == username for user in self._users)
    
    def get_user(self, identifier):
        """
        Get a user by username or account number.
        
        Args:
            identifier (str): The username or account number to look for
            
        Returns:
            User or None: The user object if found, None otherwise
        """
        # Check if user exists by username
        for user in self._users:
            if user.username == identifier or user.account_number == identifier:
                return user
        return None
    
    def authenticate_user(self, username, password):
        """
        Authenticate a user with the given credentials.
        
        Args:
            username (str): The username to authenticate
            password (str): The password to verify
            
        Returns:
            User or None: The authenticated user object if successful, None otherwise
        """
        user = self.get_user(username)
        if user and user.authenticate(password):
            self._log_transaction(f"User login: {username}")
            return user
        return None
    
    def authenticate_admin(self, username, password):
        """
        Authenticate an admin with the given credentials.
        
        Args:
            username (str): The admin username to authenticate
            password (str): The password to verify
            
        Returns:
            Admin or None: The authenticated admin object if successful, None otherwise
        """
        for admin in self._admins:
            if admin.username == username and admin.authenticate(password):
                self._log_transaction(f"Admin login: {username}")
                return admin
        return None
    
    def get_total_balance(self):
        """
        Get the total balance of all users in the bank.
        
        Returns:
            float: The sum of all user balances
        """
        return sum(user.get_balance() for user in self._users)
    
    def get_total_loan(self):
        """
        Get the total loan amount of the bank.
        
        Returns:
            float: The total loan amount
        """
        # Double-check by calculating from user loans (for data integrity)
        calculated_total = sum(user.get_loan_amount() for user in self._users)
        
        # If there's a discrepancy, update the stored value
        if calculated_total != self._total_loan:
            self._log_transaction(f"Loan amount discrepancy detected and corrected: {self._total_loan} -> {calculated_total}")
            self._total_loan = calculated_total
            
        return self._total_loan
    
    def add_to_total_loan(self, amount):
        """
        Add to the total loan amount when a new loan is issued.
        
        Args:
            amount (float): The loan amount to add
            
        Returns:
            bool: True if successful, False otherwise
        """
        if amount > 0:
            self._total_loan += amount
            self._log_transaction(f"Loan issued: ${amount:.2f}")
            return True
        return False
    
    def is_loan_enabled(self):
        """
        Check if the loan feature is enabled.
        
        Returns:
            bool: True if loans are enabled, False otherwise
        """
        return self._loan_enabled
    
    def toggle_loan_feature(self):
        """
        Toggle the loan feature on or off.
        
        Returns:
            bool: The new state of the loan feature
        """
        self._loan_enabled = not self._loan_enabled
        status = "enabled" if self._loan_enabled else "disabled"
        self._log_transaction(f"Loan feature {status}")
        return self._loan_enabled
    
    def get_interest_rate(self):
        """
        Get the current loan interest rate.
        
        Returns:
            float: The interest rate percentage
        """
        return self._interest_rate
    
    def set_interest_rate(self, rate):
        """
        Set a new loan interest rate.
        
        Args:
            rate (float): The new interest rate percentage
            
        Returns:
            bool: True if successful, False if invalid rate
        """
        # Validate interest rate (must be positive and reasonable)
        if 0 < rate < 30:  # Arbitrary reasonable range
            old_rate = self._interest_rate
            self._interest_rate = rate
            self._log_transaction(f"Interest rate changed: {old_rate}% -> {rate}%")
            return True
        return False
    
    def get_all_users(self):
        """
        Get all users in the bank.
        
        Returns:
            list: List of all user objects
        """
        return self._users
    
    def get_transaction_log(self, limit=None):
        """
        Get the bank-wide transaction log.
        
        Args:
            limit (int, optional): Maximum number of transactions to return
            
        Returns:
            list: List of transaction log entries
        """
        if limit is None:
            return self._transaction_log
        return self._transaction_log[-limit:]
    
    def get_bank_statistics(self):
        """
        Get various statistics about the bank.
        
        Returns:
            dict: Dictionary containing various bank statistics
        """
        # Calculate various statistics
        total_users = len(self._users)
        total_balance = self.get_total_balance()
        total_loan = self.get_total_loan()
        
        # Create statistics dictionary
        stats = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_users": total_users,
            "total_balance": total_balance,
            "total_loan": total_loan,
            "loan_enabled": self._loan_enabled,
            "interest_rate": self._interest_rate,
            "average_balance": total_balance / total_users if total_users > 0 else 0,
            "loan_to_deposit_ratio": (total_loan / total_balance * 100) if total_balance > 0 else 0
        }
        
        return stats
    
    def _log_transaction(self, description):
        """
        Add an entry to the bank's transaction log.
        
        Args:
            description (str): Description of the transaction or event
            
        Note:
            This is a private method (indicated by underscore prefix)
        """
        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create log entry
        log_entry = f"[{timestamp}] {description}"
        
        # Add to transaction log
        self._transaction_log.append(log_entry)
        
        # Update last updated timestamp
        self._last_updated = timestamp
    
    def export_data(self, filename=None):
        """
        Export bank data to a JSON file.
        
        Args:
            filename (str, optional): The name of the file to export to
            
        Returns:
            bool: True if export was successful, False otherwise
        """
        if filename is None:
            filename = f"bank_export_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
        try:
            # Create data structure for export
            export_data = {
                "metadata": {
                    "export_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "total_users": len(self._users),
                    "total_admins": len(self._admins)
                },
                "statistics": self.get_bank_statistics(),
                "users": [],
                "transaction_log": self._transaction_log
            }
            
            # Add user data (excluding private details like passwords)
            for user in self._users:
                user_data = {
                    "username": user.username,
                    "account_number": user.account_number,
                    "balance": user.get_balance(),
                    "loan_amount": user.get_loan_amount(),
                    "creation_date": user.creation_date,
                    "last_login": user.last_login,
                    "transaction_count": len(user.get_transaction_history())
                }
                export_data["users"].append(user_data)
                
            # Write to file
            with open(filename, "w") as file:
                json.dump(export_data, file, indent=4)
                
            self._log_transaction(f"Data exported to {filename}")
            return True
            
        except Exception as e:
            print(f"Export error: {e}")
            return False


# Example usage (for testing)
if __name__ == "__main__":
    # This code only runs when you execute this file directly
    # It doesn't run when you import this file into another file
    
    print("Testing Bank class...")
    
    # Create a test bank
    test_bank = Bank()
    
    # Create a test user and admin
    from user import User
    from admin import Admin
    
    test_user = User("testuser", "password123")
    test_admin = Admin("admin", "admin123")
    
    # Add to bank
    test_bank.add_user(test_user)
    test_bank.add_admin(test_admin)
    
    # Test a few methods
    print(f"User exists: {test_bank.user_exists('testuser')}")
    print(f"Total balance: ${test_bank.get_total_balance()}")
    print(f"Loan feature enabled: {test_bank.is_loan_enabled()}")
    
    print("\nBank testing completed.")