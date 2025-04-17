"""
Banking Management System - Main Application
This module serves as the entry point for the banking system.

Features:
- User account management (create, login)
- Admin system management (login, overview)
- Banking operations (deposit, withdraw, transfer, loans)
- Transaction history tracking
- Account security features

For beginners:
- This is the main file that runs the entire application
- It contains the menu systems and connects all other parts
- Start the application by running: python main.py
"""

# Import necessary modules
import os                  # For clearing the screen
import time                # For adding delays
import getpass             # For hidden password input
import json                # For data persistence
import random              # For generating account numbers
import datetime            # For timestamps
from user import User      # Import the User class
from admin import Admin    # Import the Admin class
from bank import Bank      # Import the Bank class

# =================== UTILITY FUNCTIONS ===================

def clear_screen():
    """Clear the console screen for better UI experience."""
    # 'cls' command for Windows, 'clear' command for Unix/Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(title):
    """Display a formatted header with the given title."""
    clear_screen()
    print("\n" + "=" * 60)
    print(f"{title:^60}")
    print("=" * 60 + "\n")

def get_input(prompt, input_type=str, min_value=None, max_value=None):
    """
    Get and validate user input based on type and range.
    
    Args:
        prompt (str): The prompt to display to the user
        input_type (type): The expected type of input (str, int, float)
        min_value: Minimum acceptable value (for numeric inputs)
        max_value: Maximum acceptable value (for numeric inputs)
        
    Returns:
        The validated input value
    """
    while True:
        try:
            # Get input based on the type
            if input_type == str:
                value = input(prompt)
                if not value.strip():  # Check if input is empty
                    print("Input cannot be empty. Please try again.")
                    continue
            else:
                value = input_type(input(prompt))
                
                # Check range for numeric values
                if min_value is not None and value < min_value:
                    print(f"Value must be at least {min_value}. Please try again.")
                    continue
                if max_value is not None and value > max_value:
                    print(f"Value must be at most {max_value}. Please try again.")
                    continue
                    
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def get_secure_password(prompt="Enter Password: "):
    """
    Get password input securely (hidden while typing).
    
    Args:
        prompt (str): The prompt to display when asking for password
        
    Returns:
        str: The entered password
    """
    try:
        # Try to use getpass for hidden input
        return getpass.getpass(prompt)
    except:
        # Fallback to regular input if getpass is not available
        print("Secure password entry not available. Password will be visible:")
        return input(prompt)

def save_bank_data(bank):
    """
    Save bank data to a JSON file for persistence.
    
    Args:
        bank (Bank): The bank object containing all data
    """
    try:
        # Create data structure for serialization
        data = {
            "users": [],
            "admins": [],
            "total_loan": bank._total_loan,
            "loan_enabled": bank._loan_enabled,
            "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Add user data
        for user in bank._users:
            user_data = {
                "username": user.username,
                "password": user.password,  # Note: In a real system, this would be hashed
                "balance": user._balance,
                "account_number": user.account_number,
                "transactions": user._transactions,
                "loan_amount": user._loan_amount,
                "creation_date": user.creation_date,
                "last_login": user.last_login
            }
            data["users"].append(user_data)
            
        # Add admin data
        for admin in bank._admins:
            admin_data = {
                "username": admin.username,
                "password": admin.password,  # Note: In a real system, this would be hashed
                "last_login": admin.last_login if hasattr(admin, 'last_login') else None
            }
            data["admins"].append(admin_data)
            
        # Save to file
        with open("bank_data.json", "w") as file:
            json.dump(data, file, indent=4)
            
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def load_bank_data():
    """
    Load bank data from a JSON file.
    
    Returns:
        Bank: A bank object populated with saved data, or a new Bank if no data exists
    """
    try:
        # Check if data file exists
        if not os.path.exists("bank_data.json"):
            # Create a new bank with default admin
            bank = Bank()
            admin = Admin("admin", "admin123")
            admin.last_login = None
            bank.add_admin(admin)
            return bank
            
        # Read data from file
        with open("bank_data.json", "r") as file:
            data = json.load(file)
            
        # Create new bank object
        bank = Bank()
        bank._total_loan = data["total_loan"]
        bank._loan_enabled = data["loan_enabled"]
        
        # Recreate users
        for user_data in data["users"]:
            user = User(user_data["username"], user_data["password"])
            user._balance = user_data["balance"]
            user.account_number = user_data["account_number"]
            user._transactions = user_data["transactions"]
            user._loan_amount = user_data["loan_amount"]
            user.creation_date = user_data["creation_date"]
            user.last_login = user_data["last_login"]
            bank.add_user(user)
            
        # Recreate admins
        for admin_data in data["admins"]:
            admin = Admin(admin_data["username"], admin_data["password"])
            admin.last_login = admin_data.get("last_login")
            bank.add_admin(admin)
            
        return bank
    except Exception as e:
        print(f"Error loading data: {e}")
        print("Creating new bank with default settings...")
        # Create a new bank with default admin if loading fails
        bank = Bank()
        admin = Admin("admin", "admin123")
        bank.add_admin(admin)
        return bank

# =================== MENU FUNCTIONS ===================

def main_menu():
    """
    Display the main menu of the banking system.
    
    Returns:
        int: The user's choice
    """
    # Display header and menu options
    display_header("WELCOME TO BANKING MANAGEMENT SYSTEM")
    print("📋 MAIN MENU")
    print("-------------------")
    print("1. Login as User")
    print("2. Login as Admin")
    print("3. Create User Account")
    print("4. Exit")
    
    # Get user's choice
    choice = get_input("\nEnter your choice (1-4): ", int, 1, 4)
    return choice

def user_menu(user):
    """
    Display the user menu options.
    
    Args:
        user (User): The currently logged-in user
        
    Returns:
        int: The user's choice
    """
    # Display header with personalized greeting
    display_header(f"USER DASHBOARD - Welcome {user.username.title()}")
    
    # Show quick account overview
    print(f"Account Number: {user.account_number}")
    print(f"Current Balance: ${user.get_balance():.2f}")
    if user.get_loan_amount() > 0:
        print(f"Outstanding Loan: ${user.get_loan_amount():.2f}")
    print("\n📋 USER MENU")
    print("-------------------")
    print("1. Deposit Amount")
    print("2. Withdraw Amount")
    print("3. Check Detailed Account Information")
    print("4. Transfer Money")
    print("5. View Transaction History")
    print("6. Apply for Loan")
    print("7. Change Password")
    print("8. Logout")
    
    # Get user's choice
    choice = get_input("\nEnter your choice (1-8): ", int, 1, 8)
    return choice

def admin_menu(admin):
    """
    Display the admin menu options.
    
    Args:
        admin (Admin): The currently logged-in admin
        
    Returns:
        int: The admin's choice
    """
    # Display header with admin greeting
    display_header(f"ADMIN DASHBOARD - Welcome {admin.username}")
    
    # Display last login information if available
    if hasattr(admin, 'last_login') and admin.last_login:
        print(f"Last Login: {admin.last_login}")
    
    print("\n📋 ADMIN MENU")
    print("-------------------")
    print("1. Create New User Account")
    print("2. Check Total Bank Balance")
    print("3. Check Total Loan Amount")
    print("4. Toggle Loan Feature")
    print("5. View All Users")
    print("6. Search User")
    print("7. System Settings")
    print("8. Logout")
    
    # Get admin's choice
    choice = get_input("\nEnter your choice (1-8): ", int, 1, 8)
    return choice

# =================== MAIN FUNCTION ===================

def main():
    """Main function to run the banking system."""
    # Load bank data or create new bank if no saved data exists
    bank = load_bank_data()
    
    # Main program loop
    running = True
    while running:
        choice = main_menu()
        
        if choice == 1:  # Login as User
            display_header("USER LOGIN")
            username = input("Enter Username: ")
            password = get_secure_password()
            
            # Authenticate user
            user = bank.authenticate_user(username, password)
            if user:
                # Update last login time
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                user.last_login = current_time
                
                print("\nLogin successful!")
                print(f"Welcome back, {username.title()}!")
                time.sleep(1)
                
                # Start user session
                user_session(user, bank)
                
                # Save data after session ends
                save_bank_data(bank)
            else:
                print("\n❌ Invalid username or password.")
                time.sleep(2)
                
        elif choice == 2:  # Login as Admin
            display_header("ADMIN LOGIN")
            username = input("Enter Admin Username: ")
            password = get_secure_password()
            
            # Authenticate admin
            admin = bank.authenticate_admin(username, password)
            if admin:
                # Update last login time
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                admin.last_login = current_time
                
                print("\nAdmin login successful!")
                time.sleep(1)
                
                # Start admin session
                admin_session(admin, bank)
                
                # Save data after session ends
                save_bank_data(bank)
            else:
                print("\n❌ Invalid admin credentials.")
                time.sleep(2)
                
        elif choice == 3:  # Create User Account
            display_header("CREATE NEW USER ACCOUNT")
            
            # Get new user information
            username = get_input("Enter Username: ")
            
            # Check if username already exists
            if bank.user_exists(username):
                print("\n❌ Username already exists. Please choose another.")
                time.sleep(2)
                continue
                
            # Get password with confirmation
            while True:
                password = get_secure_password()
                confirm_password = get_secure_password("Confirm Password: ")
                
                if password == confirm_password:
                    break
                else:
                    print("❌ Passwords do not match. Please try again.\n")
            
            # Get initial deposit
            initial_deposit = get_input("Enter Initial Deposit Amount: $", float, 0)
            
            # Generate account number
            account_number = f"ACCT-{random.randint(10000, 99999)}"
            
            # Create new user
            user = User(username, password)
            user.account_number = account_number
            user.creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            bank.add_user(user)
            
            # Make initial deposit
            if initial_deposit > 0:
                user.deposit(initial_deposit)
                print(f"\n✅ Account created successfully!")
                print(f"Account Number: {account_number}")
                print(f"Initial deposit: ${initial_deposit:.2f}")
            else:
                print(f"\n✅ Account created successfully with $0 balance.")
                print(f"Account Number: {account_number}")
            
            # Save bank data after creating new user
            save_bank_data(bank)
            
            time.sleep(3)
            
        elif choice == 4:  # Exit
            print("\nThank you for using the Banking Management System!")
            print("Saving data before exit...")
            save_bank_data(bank)
            running = False
            
        else:
            print("\n❌ Invalid choice. Please try again.")
            time.sleep(1)

def user_session(user, bank):
    """
    Handle the user session after successful login.
    
    Args:
        user (User): The logged-in user
        bank (Bank): The bank instance
    """
    logged_in = True
    
    while logged_in:
        choice = user_menu(user)
        
        if choice == 1:  # Deposit
            display_header("DEPOSIT AMOUNT")
            
            # Show current balance
            print(f"Current Balance: ${user.get_balance():.2f}")
            
            # Get deposit amount
            amount = get_input("\nEnter amount to deposit: $", float, 0.01)
            
            # Process deposit
            if amount <= 0:
                print("❌ Amount must be positive.")
            else:
                # Simulate processing time
                print("\nProcessing deposit...")
                time.sleep(1.5)
                
                # Complete deposit
                user.deposit(amount)
                print(f"\n✅ Deposit successful!")
                print(f"New balance: ${user.get_balance():.2f}")
            
            input("\nPress Enter to continue...")
            
        elif choice == 2:  # Withdraw
            display_header("WITHDRAW AMOUNT")
            
            # Show current balance
            print(f"Current Balance: ${user.get_balance():.2f}")
            
            # Get withdrawal amount
            amount = get_input("\nEnter amount to withdraw: $", float, 0.01)
            
            # Process withdrawal
            if amount <= 0:
                print("❌ Amount must be positive.")
            else:
                # Simulate processing time
                print("\nProcessing withdrawal...")
                time.sleep(1.5)
                
                # Complete withdrawal
                result = user.withdraw(amount)
                if result == "BANK_BANKRUPT":
                    print("\n❌ The bank is bankrupt. Unable to process withdrawal.")
                    print("Please contact bank management for assistance.")
                elif result:
                    print(f"\n✅ Withdrawal successful!")
                    print(f"New balance: ${user.get_balance():.2f}")
                else:
                    print("\n❌ Insufficient funds.")
                    print(f"Available balance: ${user.get_balance():.2f}")
            
            input("\nPress Enter to continue...")
            
        elif choice == 3:  # Check Detailed Account Information
            display_header("ACCOUNT INFORMATION")
            
            # Display detailed account information
            print(f"Account Holder: {user.username.title()}")
            print(f"Account Number: {user.account_number}")
            print(f"Creation Date: {user.creation_date}")
            print(f"Last Login: {user.last_login}")
            print(f"Current Balance: ${user.get_balance():.2f}")
            
            # Show loan information if applicable
            if user.get_loan_amount() > 0:
                print(f"Outstanding Loan: ${user.get_loan_amount():.2f}")
                
            # Show account statistics
            num_transactions = len(user.get_transaction_history())
            print(f"\nTotal Transactions: {num_transactions}")
            
            # Recent activity
            if num_transactions > 0:
                print("\nRecent Activity (last 3 transactions):")
                for transaction in user.get_transaction_history()[-3:]:
                    print(f"  - {transaction}")
            
            input("\nPress Enter to continue...")
            
        elif choice == 4:  # Transfer Money
            display_header("TRANSFER MONEY")
            
            # Show current balance
            print(f"Current Balance: ${user.get_balance():.2f}")
            
            # Get transfer details
            recipient = input("\nEnter recipient's username or account number: ")
            
            # Check if recipient exists
            recipient_user = bank.get_user(recipient)
            if recipient_user and recipient_user.username != user.username:
                print(f"Recipient Found: {recipient_user.username.title()}")
                
                # Get transfer amount
                amount = get_input("Enter amount to transfer: $", float, 0.01)
                
                if amount <= 0:
                    print("❌ Amount must be positive.")
                elif amount > user.get_balance():
                    print("❌ Insufficient funds for transfer.")
                else:
                    # Get transfer confirmation
                    confirm = input(f"Confirm transfer of ${amount:.2f} to {recipient_user.username.title()}? (y/n): ")
                    
                    if confirm.lower() == 'y':
                        # Simulate processing time
                        print("\nProcessing transfer...")
                        time.sleep(2)
                        
                        # Complete transfer
                        user.transfer(amount, recipient_user)
                        print(f"\n✅ Transfer successful!")
                        print(f"New balance: ${user.get_balance():.2f}")
                    else:
                        print("\nTransfer cancelled.")
            else:
                print("\n❌ Recipient not found or cannot transfer to yourself.")
            
            input("\nPress Enter to continue...")
            
        elif choice == 5:  # Transaction History
            display_header("TRANSACTION HISTORY")
            
            transactions = user.get_transaction_history()
            
            if transactions:
                # Display filter options
                print("Filter Options:")
                print("1. All Transactions")
                print("2. Deposits Only")
                print("3. Withdrawals Only")
                print("4. Transfers Only")
                print("5. Loans Only")
                
                filter_choice = get_input("\nSelect filter (1-5): ", int, 1, 5)
                
                # Apply filter
                filtered_transactions = []
                if filter_choice == 1:
                    filtered_transactions = transactions
                elif filter_choice == 2:
                    filtered_transactions = [t for t in transactions if "Deposit" in t]
                elif filter_choice == 3:
                    filtered_transactions = [t for t in transactions if "Withdrawal" in t]
                elif filter_choice == 4:
                    filtered_transactions = [t for t in transactions if "Transfer" in t]
                elif filter_choice == 5:
                    filtered_transactions = [t for t in transactions if "Loan" in t]
                
                # Display transactions with pagination
                page_size = 5
                total_pages = (len(filtered_transactions) + page_size - 1) // page_size
                current_page = 1
                
                while True:
                    display_header(f"TRANSACTION HISTORY (Page {current_page}/{total_pages})")
                    
                    # Calculate slice for current page
                    start_idx = (current_page - 1) * page_size
                    end_idx = start_idx + page_size
                    page_transactions = filtered_transactions[start_idx:end_idx]
                    
                    # Display transactions on current page
                    if page_transactions:
                        for i, transaction in enumerate(page_transactions, start_idx + 1):
                            print(f"{i}. {transaction}")
                    else:
                        print("No transactions match the selected filter.")
                    
                    # Navigation options
                    print("\nNavigation:")
                    if current_page > 1:
                        print("P - Previous Page")
                    if current_page < total_pages:
                        print("N - Next Page")
                    print("X - Return to Menu")
                    
                    # Get navigation choice
                    nav_choice = input("\nEnter choice: ").upper()
                    
                    if nav_choice == 'P' and current_page > 1:
                        current_page -= 1
                    elif nav_choice == 'N' and current_page < total_pages:
                        current_page += 1
                    elif nav_choice == 'X':
                        break
                    else:
                        print("Invalid choice. Please try again.")
                        time.sleep(1)
            else:
                print("No transaction history available.")
                input("\nPress Enter to continue...")
            
        elif choice == 6:  # Apply for Loan
            display_header("LOAN APPLICATION")
            
            if not bank.is_loan_enabled():
                print("❌ Loan feature is currently disabled by the bank.")
            else:
                # Calculate maximum loan available
                max_loan = user.get_balance() * 2
                print(f"Account Balance: ${user.get_balance():.2f}")
                print(f"Maximum loan amount available: ${max_loan:.2f}")
                
                # Check eligibility
                if max_loan <= 0:
                    print("❌ You need to have some deposit to be eligible for a loan.")
                else:
                    # Get loan details
                    amount = get_input("\nEnter loan amount: $", float, 0.01)
                    
                    if amount <= 0:
                        print("❌ Loan amount must be positive.")
                    elif amount > max_loan:
                        print("❌ Loan amount exceeds your eligibility.")
                        print(f"Maximum eligible amount: ${max_loan:.2f}")
                    else:
                        # Display loan terms
                        interest_rate = 8.5  # Example interest rate
                        term_years = 2
                        monthly_payment = (amount + (amount * interest_rate / 100)) / (term_years * 12)
                        
                        print(f"\nLoan Amount: ${amount:.2f}")
                        print(f"Interest Rate: {interest_rate}%")
                        print(f"Term: {term_years} years")
                        print(f"Estimated Monthly Payment: ${monthly_payment:.2f}")
                        
                        # Get confirmation
                        confirm = input("\nDo you want to proceed with this loan? (y/n): ")
                        
                        if confirm.lower() == 'y':
                            # Simulate processing time
                            print("\nProcessing your loan application...")
                            time.sleep(2)
                            
                            # Complete loan
                            user.take_loan(amount)
                            bank.add_to_total_loan(amount)
                            print(f"\n✅ Loan approved and deposited to your account!")
                            print(f"New balance: ${user.get_balance():.2f}")
                        else:
                            print("\nLoan application cancelled.")
            
            input("\nPress Enter to continue...")
            
        elif choice == 7:  # Change Password
            display_header("CHANGE PASSWORD")
            
            # Verify current password
            current_password = get_secure_password("Enter current password: ")
            
            if current_password == user.password:
                # Get new password with confirmation
                while True:
                    new_password = get_secure_password("Enter new password: ")
                    confirm_password = get_secure_password("Confirm new password: ")
                    
                    if new_password == confirm_password:
                        # Update password
                        user.password = new_password
                        print("\n✅ Password changed successfully!")
                        break
                    else:
                        print("❌ Passwords do not match. Please try again.\n")
            else:
                print("\n❌ Incorrect current password.")
            
            input("\nPress Enter to continue...")
            
        elif choice == 8:  # Logout
            logged_in = False
            print("\nLogging out...")
            time.sleep(1)
            
        else:
            print("\n❌ Invalid choice. Please try again.")
            time.sleep(1)

def admin_session(admin, bank):
    """
    Handle the admin session after successful login.
    
    Args:
        admin (Admin): The logged-in admin
        bank (Bank): The bank instance
    """
    logged_in = True
    
    while logged_in:
        choice = admin_menu(admin)
        
        if choice == 1:  # Create User Account
            display_header("CREATE NEW USER ACCOUNT")
            
            # Get new user information
            username = get_input("Enter Username: ")
            
            # Check if username already exists
            if bank.user_exists(username):
                print("\n❌ Username already exists. Please choose another.")
            else:
                # Get password
                password = get_secure_password()
                
                # Get initial deposit
                initial_deposit = get_input("Enter Initial Deposit Amount: $", float, 0)
                
                # Generate account number
                account_number = f"ACCT-{random.randint(10000, 99999)}"
                
                # Create new user
                user = User(username, password)
                user.account_number = account_number
                user.creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                bank.add_user(user)
                
                # Make initial deposit
                if initial_deposit > 0:
                    user.deposit(initial_deposit)
                    print(f"\n✅ Account created successfully with initial deposit of ${initial_deposit:.2f}")
                    print(f"Account Number: {account_number}")
                else:
                    print(f"\n✅ Account created successfully with $0 balance.")
                    print(f"Account Number: {account_number}")
            
            input("\nPress Enter to continue...")
            
        elif choice == 2:  # Check Total Bank Balance
            display_header("TOTAL BANK BALANCE")
            
            # Calculate and display statistics
            total_balance = bank.get_total_balance()
            total_users = len(bank.get_all_users())
            average_balance = total_balance / total_users if total_users > 0 else 0
            
            print(f"Total Bank Balance: ${total_balance:.2f}")
            print(f"Number of Accounts: {total_users}")
            print(f"Average Account Balance: ${average_balance:.2f}")
            
            # Show daily comparison if available
            # (This would be more sophisticated in a real system)
            print("\nDaily Comparison:")
            print("Yesterday's Total: $---.--")
            print("Change: +$---.--")
            
            input("\nPress Enter to continue...")
            
        elif choice == 3:  # Check Total Loan Amount
            display_header("TOTAL LOAN AMOUNT")
            
            # Calculate and display loan statistics
            total_loan = bank.get_total_loan()
            total_balance = bank.get_total_balance()
            loan_ratio = (total_loan / total_balance * 100) if total_balance > 0 else 0
            
            print(f"Total Loan Amount: ${total_loan:.2f}")
            print(f"Loan to Deposit Ratio: {loan_ratio:.2f}%")
            
            # Count users with loans
            users_with_loans = sum(1 for user in bank.get_all_users() if user.get_loan_amount() > 0)
            print(f"Number of Borrowers: {users_with_loans}")
            
            # Display risk assessment
            if loan_ratio < 30:
                risk_level = "Low"
            elif loan_ratio < 70:
                risk_level = "Moderate"
            else:
                risk_level = "High"
                
            print(f"Current Risk Level: {risk_level}")
            
            input("\nPress Enter to continue...")
            
        elif choice == 4:  # Toggle Loan Feature
            display_header("TOGGLE LOAN FEATURE")
            
            # Show current loan status
            loan_status = "enabled" if bank.is_loan_enabled() else "disabled"
            print(f"Loan feature is currently {loan_status}.")
            
            # Get confirmation to toggle
            confirm = input(f"Do you want to {'disable' if bank.is_loan_enabled() else 'enable'} it? (y/n): ")
            if confirm.lower() == 'y':
                # Toggle loan feature
                bank.toggle_loan_feature()
                new_status = "enabled" if bank.is_loan_enabled() else "disabled"
                print(f"\n✅ Loan feature is now {new_status}.")
            
            input("\nPress Enter to continue...")
            
        elif choice == 5:  # View All Users
            display_header("ALL USERS")
            
            users = bank.get_all_users()
            
            if users:
                # Show sort options
                print("Sort by:")
                print("1. Username")
                print("2. Balance (Highest to Lowest)")
                print("3. Balance (Lowest to Highest)")
                print("4. Creation Date (Newest First)")
                
                # Get sort choice
                sort_choice = get_input("\nSelect sorting option (1-4): ", int, 1, 4)
                
                # Sort users based on selection
                if sort_choice == 1:
                    sorted_users = sorted(users, key=lambda u: u.username.lower())
                elif sort_choice == 2:
                    sorted_users = sorted(users, key=lambda u: u.get_balance(), reverse=True)
                elif sort_choice == 3:
                    sorted_users = sorted(users, key=lambda u: u.get_balance())
                elif sort_choice == 4:
                    sorted_users = sorted(users, key=lambda u: u.creation_date, reverse=True)
                
                # Display user table with pagination
                page_size = 5
                total_pages = (len(sorted_users) + page_size - 1) // page_size
                current_page = 1
                
                while True:
                    display_header(f"ALL USERS (Page {current_page}/{total_pages})")
                    
                    # Calculate slice for current page
                    start_idx = (current_page - 1) * page_size
                    end_idx = start_idx + page_size
                    page_users = sorted_users[start_idx:end_idx]
                    
                    # Display column headers
                    print(f"{'#':<3} {'Username':<15} {'Account Number':<15} {'Balance':<12} {'Loan Amount':<12} {'Creation Date':<20}")
                    print("-" * 75)
                    
                    # Display users on current page
                    for i, user in enumerate(page_users, start_idx + 1):
                        print(f"{i:<3} {user.username:<15} {user.account_number:<15} ${user.get_balance():<10.2f} ${user.get_loan_amount():<10.2f} {user.creation_date}")
                    
                    # Navigation options
                    print("\nNavigation:")
                    if current_page > 1:
                        print("P - Previous Page")
                    if current_page < total_pages:
                        print("N - Next Page")
                    print("V - View User Details")
                    print("X - Return to Menu")
                    
                    # Get navigation choice
                    nav_choice = input("\nEnter choice: ").upper()
                    
                    if nav_choice == 'P' and current_page > 1:
                        current_page -= 1
                    elif nav_choice == 'N' and current_page < total_pages:
                        current_page += 1
                    elif nav_choice == 'V':
                        # View user details
                        user_idx = get_input("Enter user number to view details: ", int, 1, len(sorted_users)) - 1
                        if 0 <= user_idx < len(sorted_users):
                            view_user_details(sorted_users[user_idx])
                        else:
                            print("Invalid user number.")
                            time.sleep(1)
                    elif nav_choice == 'X':
                        break
                    else:
                        print("Invalid choice. Please try again.")
                        time.sleep(1)
            else:
                print("No users registered in the system.")
                input("\nPress Enter to continue...")
            
        elif choice == 6:  # Search User
            display_header("SEARCH USER")
            
            # Get search term
            search_term = input("Enter username or account number to search: ")
            
            if search_term:
                # Search for users matching the search term
                results = []
                for user in bank.get_all_users():
                    if (search_term.lower() in user.username.lower() or 
                        search_term in user.account_number):
                        results.append(user)
                
                # Display search results
                if results:
                    print(f"\nFound {len(results)} matching user(s):\n")
                    print(f"{'#':<3} {'Username':<15} {'Account Number':<15} {'Balance':<12}")
                    print("-" * 50)
                    
                    for i, user in enumerate(results, 1):
                        print(f"{i:<3} {user.username:<15} {user.account_number:<15} ${user.get_balance():<10.2f}")
                    
                    # Option to view user details
                    view_option = input("\nEnter user number to view details (or 0 to return): ")
                    if view_option.isdigit() and 1 <= int(view_option) <= len(results):
                        view_user_details(results[int(view_option) - 1])
                else:
                    print("\nNo users found matching your search.")
            else:
                print("Search term cannot be empty.")
            
            input("\nPress Enter to continue...")
            
        elif choice == 7:  # System Settings
            display_header("SYSTEM SETTINGS")
            
            print("1. Backup System Data")
            print("2. Restore System Data")
            print("3. Create New Admin Account")
            print("4. View System Info")
            print("5. Return to Admin Menu")
            
            setting_choice = get_input("\nSelect option (1-5): ", int, 1, 5)
            
            if setting_choice == 1:  # Backup
                # Simulate backup
                print("\nBacking up system data...")
                time.sleep(2)
                backup_filename = f"bank_backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                save_bank_data(bank)
                print(f"✅ Backup completed: {backup_filename}")
                
            elif setting_choice == 2:  # Restore
                # Simulate restore
                print("\nThis would restore system data from a backup.")
                print("Feature not implemented in this demo.")
                
            elif setting_choice == 3:  # Create Admin
                # Create new admin account
                print("\nCreate New Admin Account")
                admin_username = get_input("Enter new admin username: ")
                
                # Check if admin already exists
                if any(a.username == admin_username for a in bank._admins):
                    print("❌ Admin username already exists.")
                else:
                    # Get password with confirmation
                    while True:
                        admin_password = get_secure_password("Enter admin password: ")
                        confirm_password = get_secure_password("Confirm password: ")
                        
                        if admin_password == confirm_password:
                            break
                        else:
                            print("❌ Passwords do not match. Please try again.\n")
                    
                    # Create new admin
                    new_admin = Admin(admin_username, admin_password)
                    bank.add_admin(new_admin)
                    print(f"\n✅ Admin account '{admin_username}' created successfully!")
                
            elif setting_choice == 4:  # System Info
                # Display system information
                print("\nSystem Information:")
                print(f"Total Users: {len(bank.get_all_users())}")
                print(f"Total Admins: {len(bank._admins)}")
                print(f"Total Bank Balance: ${bank.get_total_balance():.2f}")
                print(f"Total Loan Amount: ${bank.get_total_loan():.2f}")
                print(f"Loan Feature: {'Enabled' if bank.is_loan_enabled() else 'Disabled'}")
                print(f"Last Data Save: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                
            input("\nPress Enter to continue...")
            
        elif choice == 8:  # Logout
            logged_in = False
            print("\nLogging out...")
            time.sleep(1)
            
        else:
            print("\n❌ Invalid choice. Please try again.")
            time.sleep(1)

def view_user_details(user):
    """
    Display detailed information about a user.
    
    Args:
        user (User): The user to display details for
    """
    display_header(f"USER DETAILS: {user.username}")
    
    # Display account information
    print(f"Username: {user.username}")
    print(f"Account Number: {user.account_number}")
    print(f"Creation Date: {user.creation_date}")
    print(f"Last Login: {user.last_login}")
    print(f"Current Balance: ${user.get_balance():.2f}")
    
    # Show loan information if applicable
    if user.get_loan_amount() > 0:
        print(f"Outstanding Loan: ${user.get_loan_amount():.2f}")
    
    # Display transaction count
    transactions = user.get_transaction_history()
    print(f"\nTotal Transactions: {len(transactions)}")
    
    # Display last few transactions
    if transactions:
        print("\nRecent Transactions:")
        for transaction in transactions[-5:]:
            print(f"  - {transaction}")
    
    input("\nPress Enter to return...")

# =================== START POINT ===================

if __name__ == "__main__":
    try:
        print("Starting Banking Management System...")
        # Display a welcome message with ASCII art
        print("""
        💰💰💰 BANKING MANAGEMENT SYSTEM 💰💰💰
        ==========================================
                 Welcome to BankPython
        ==========================================
        """)
        time.sleep(1)
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
        print("Saving data before exit...")
        try:
            # Try to save bank data if it exists
            if 'bank' in locals() or 'bank' in globals():
                save_bank_data(bank)
            else:
                print("No bank data to save.")
        except:
            pass
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        input("\nPress Enter to exit...")
    finally:
        print("\nThank you for using the Banking Management System!")
        print("Goodbye!")
        time.sleep(1)
        exit(0)
        