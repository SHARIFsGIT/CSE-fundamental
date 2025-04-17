"""
Banking Management System - User Module
This module defines the User class and its functionality.

For beginners:
- This file contains all the operations a bank user can perform
- Each method represents a different banking action (deposit, withdraw, etc.)
- The User class keeps track of a user's balance and transaction history
"""

from datetime import datetime
import random

class User:
    """
    Represents a bank user with various banking operations.
    
    Attributes:
        username (str): The user's username for login
        password (str): The user's password for authentication
        account_number (str): Unique account identifier
        _balance (float): Current account balance (private)
        _transactions (list): History of all transactions (private)
        _loan_amount (float): Outstanding loan amount (private)
        creation_date (str): When the account was created
        last_login (str): When the user last logged in
    """
    
    def __init__(self, username, password):
        """
        Initialize a new user with default values.
        
        Args:
            username (str): The user's username
            password (str): The user's password
        """
        # Public attributes
        self.username = username
        self.password = password
        self.account_number = f"ACCT-{random.randint(10000, 99999)}"
        self.creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.last_login = None
        
        # Private attributes (indicated by underscore prefix)
        self._balance = 0.0
        self._transactions = []
        self._loan_amount = 0.0
        
        # Record account creation
        self._add_transaction("Account Created")
    
    def authenticate(self, password):
        """
        Authenticate the user with the given password.
        
        Args:
            password (str): The password to verify
            
        Returns:
            bool: True if authentication is successful, False otherwise
        """
        return self.password == password
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit
            
        Returns:
            bool: True if deposit is successful, False otherwise
        """
        # Validate deposit amount
        if amount <= 0:
            return False
        
        # Process deposit
        self._balance += amount
        self._add_transaction(f"Deposit: +${amount:.2f}")
        return True
    
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        
        Args:
            amount (float): The amount to withdraw
            
        Returns:
            bool or str: True if withdrawal is successful, False if insufficient funds,
                         "BANK_BANKRUPT" if bank cannot process withdrawal
        """
        # Validate withdrawal amount
        if amount <= 0:
            return False
        
        # Check if user has sufficient funds
        if amount > self._balance:
            return False
        
        # Simulate bank bankruptcy (for demonstration purposes)
        # In a real system, this would use more sophisticated logic
        if self._balance > 1000000:  # Arbitrary high value
            return "BANK_BANKRUPT"
        
        # Process withdrawal
        self._balance -= amount
        self._add_transaction(f"Withdrawal: -${amount:.2f}")
        return True
    
    def transfer(self, amount, recipient):
        """
        Transfer money to another user's account.
        
        Args:
            amount (float): The amount to transfer
            recipient (User): The recipient user object
            
        Returns:
            bool: True if transfer is successful, False otherwise
        """
        # Validate transfer amount and recipient
        if amount <= 0 or amount > self._balance:
            return False
        
        # Process transfer (subtract from sender, add to recipient)
        self._balance -= amount
        recipient._balance += amount
        
        # Record transaction in both accounts
        self._add_transaction(f"Transfer to {recipient.username}: -${amount:.2f}")
        recipient._add_transaction(f"Transfer from {self.username}: +${amount:.2f}")
        
        return True
    
    def take_loan(self, amount):
        """
        Take a loan from the bank.
        
        Args:
            amount (float): The loan amount requested
            
        Returns:
            bool: True if loan is approved, False otherwise
        """
        # Validate loan amount
        if amount <= 0:
            return False
        
        # User can take a loan up to twice their balance (basic eligibility check)
        max_loan = self._balance * 2
        
        # Check if loan amount exceeds eligibility
        if amount > max_loan:
            return False
        
        # Process loan (add to balance and record loan amount)
        self._balance += amount
        self._loan_amount += amount
        self._add_transaction(f"Loan Approved: +${amount:.2f}")
        
        return True
    
    def repay_loan(self, amount):
        """
        Repay part or all of an outstanding loan.
        
        Args:
            amount (float): The amount to repay
            
        Returns:
            bool: True if repayment is successful, False otherwise
        """
        # Validate repayment amount
        if amount <= 0 or amount > self._balance:
            return False
        
        # Check if user has an outstanding loan
        if self._loan_amount <= 0:
            return False
        
        # Calculate actual repayment amount (cannot exceed outstanding loan)
        actual_repayment = min(amount, self._loan_amount)
        
        # Process repayment
        self._balance -= actual_repayment
        self._loan_amount -= actual_repayment
        self._add_transaction(f"Loan Repayment: -${actual_repayment:.2f}")
        
        return True
    
    def get_balance(self):
        """
        Get the current account balance.
        
        Returns:
            float: The current balance
        """
        return self._balance
    
    def get_loan_amount(self):
        """
        Get the outstanding loan amount.
        
        Returns:
            float: The current loan amount
        """
        return self._loan_amount
    
    def get_transaction_history(self):
        """
        Get the complete transaction history.
        
        Returns:
            list: List of transaction strings
        """
        return self._transactions
    
    def _add_transaction(self, description):
        """
        Add a transaction to the history with timestamp and balance.
        
        Args:
            description (str): Description of the transaction
            
        Note:
            This is a private method (indicated by underscore prefix)
        """
        # Create timestamp for the transaction
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Format the transaction entry with timestamp, description and current balance
        transaction = f"[{timestamp}] {description} (Balance: ${self._balance:.2f})"
        
        # Add to transaction history
        self._transactions.append(transaction)


# Example usage (for testing)
if __name__ == "__main__":
    # This code only runs when you execute this file directly
    # It doesn't run when you import this file into another file
    
    print("Testing User class...")
    
    # Create a test user
    test_user = User("testuser", "password123")
    
    # Test deposit
    test_user.deposit(1000)
    print(f"Balance after deposit: ${test_user.get_balance()}")
    
    # Test withdrawal
    test_user.withdraw(500)
    print(f"Balance after withdrawal: ${test_user.get_balance()}")
    
    # Test transaction history
    print("\nTransaction History:")
    for transaction in test_user.get_transaction_history():
        print(f"  - {transaction}")
    
    print("\nUser testing completed.")