"""
Banking Management System - Admin Module
This module defines the Admin class and its functionality.

For beginners:
- This file contains all the operations a bank administrator can perform
- Admin users have special permissions to manage the bank system
- The Admin class includes methods for account creation and system settings
"""

from datetime import datetime

class Admin:
    """
    Represents a bank administrator with management capabilities.
    
    Attributes:
        username (str): The admin's username for login
        password (str): The admin's password for authentication
        last_login (str): When the admin last logged in
    """
    
    def __init__(self, username, password):
        """
        Initialize a new admin.
        
        Args:
            username (str): The admin's username
            password (str): The admin's password
        """
        self.username = username
        self.password = password
        self.last_login = None
    
    def authenticate(self, password):
        """
        Authenticate the admin with the given password.
        
        Args:
            password (str): The password to verify
            
        Returns:
            bool: True if authentication is successful, False otherwise
        """
        return self.password == password
    
    def create_user_account(self, username, password, bank):
        """
        Create a new user account in the bank.
        
        Args:
            username (str): Username for the new account
            password (str): Password for the new account
            bank (Bank): The bank instance to add the user to
            
        Returns:
            bool: True if account creation is successful, False if username already exists
        """
        # Check if username already exists
        if bank.user_exists(username):
            return False
        
        # Create new user
        from user import User
        user = User(username, password)
        
        # Add user to bank
        bank.add_user(user)
        
        # Log the action
        self._log_action(f"Created new user account: {username}")
        
        return True
    
    def search_user(self, search_term, bank):
        """
        Search for users by username or account number.
        
        Args:
            search_term (str): The search term to look for
            bank (Bank): The bank instance containing users
            
        Returns:
            list: List of matching User objects
        """
        results = []
        
        # Search for matching users
        for user in bank.get_all_users():
            if (search_term.lower() in user.username.lower() or 
                search_term in user.account_number):
                results.append(user)
        
        # Log the search action
        self._log_action(f"Searched for users with term: {search_term}")
        
        return results
    
    def toggle_loan_feature(self, bank):
        """
        Enable or disable the loan feature.
        
        Args:
            bank (Bank): The bank instance to modify
            
        Returns:
            bool: New state of loan feature (True if enabled, False if disabled)
        """
        # Toggle the loan feature
        bank.toggle_loan_feature()
        
        # Get new state
        new_state = bank.is_loan_enabled()
        
        # Log the action
        self._log_action(f"{'Enabled' if new_state else 'Disabled'} loan feature")
        
        return new_state
    
    def generate_bank_report(self, bank):
        """
        Generate a comprehensive report of bank statistics.
        
        Args:
            bank (Bank): The bank instance to analyze
            
        Returns:
            dict: Dictionary containing various bank statistics
        """
        # Get all users
        users = bank.get_all_users()
        
        # Calculate statistics
        report = {
            "total_users": len(users),
            "total_balance": bank.get_total_balance(),
            "total_loan": bank.get_total_loan(),
            "average_balance": 0,
            "users_with_loans": 0,
            "largest_account": {"username": "None", "balance": 0},
            "newest_account": {"username": "None", "date": "None"},
            "loan_to_deposit_ratio": 0
        }
        
        # Calculate more detailed statistics
        if users:
            # Average balance
            report["average_balance"] = report["total_balance"] / report["total_users"]
            
            # Count users with loans
            for user in users:
                if user.get_loan_amount() > 0:
                    report["users_with_loans"] += 1
                
                # Find largest account
                if user.get_balance() > report["largest_account"]["balance"]:
                    report["largest_account"] = {
                        "username": user.username,
                        "balance": user.get_balance()
                    }
                    
                # Find newest account
                if report["newest_account"]["date"] == "None" or user.creation_date > report["newest_account"]["date"]:
                    report["newest_account"] = {
                        "username": user.username,
                        "date": user.creation_date
                    }
            
            # Calculate loan to deposit ratio
            if report["total_balance"] > 0:
                report["loan_to_deposit_ratio"] = (report["total_loan"] / report["total_balance"]) * 100
        
        # Log the action
        self._log_action("Generated bank report")
        
        return report
    
    def _log_action(self, action_description):
        """
        Log an administrative action with timestamp.
        
        Args:
            action_description (str): Description of the action performed
            
        Note:
            This is a private method (indicated by underscore prefix)
            In a real system, this would write to an admin audit log
        """
        # Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Format log entry (in a real system, this would be saved to a file)
        log_entry = f"[{timestamp}] Admin {self.username}: {action_description}"
        
        # For demonstration, just print the log entry
        # In a real system, this would be saved to a secure audit log
        print(f"ADMIN LOG: {log_entry}")


# Example usage (for testing)
if __name__ == "__main__":
    # This code only runs when you execute this file directly
    # It doesn't run when you import this file into another file
    
    print("Testing Admin class...")
    
    # Create a test admin
    test_admin = Admin("admin", "admin123")
    
    # Test authentication
    print(f"Authentication test: {test_admin.authenticate('admin123')}")
    
    print("\nAdmin testing completed.")