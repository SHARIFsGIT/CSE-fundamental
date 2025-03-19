"""
Authentication system for the Library Management System.
Handles user login and registration.
"""
import getpass
import hashlib

class AuthenticationSystem:
    """
    Handles user authentication and registration.
    """
    def __init__(self, library):
        self.library = library
        
    def display_auth_menu(self):
        """Display authentication menu and handle login/registration"""
        while True:
            print("\n==== LIBRARY MANAGEMENT SYSTEM ====")
            print(f"Welcome to {self.library.name}")
            print("\n1. Login")
            print("2. Register")
            print("3. Exit")
            
            try:
                choice = input("\nEnter your choice (1-3): ").strip()
                
                if choice == "1":
                    user = self._login()
                    if user:
                        return user
                elif choice == "2":
                    self._register()
                elif choice == "3":
                    print("Exiting...")
                    exit(0)
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
                    
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
            except Exception as e:
                print(f"An error occurred: {e}")
                
    def _login(self):
        """
        Handle user login with secure password input.
        
        Returns:
            User: The authenticated user or None if login failed
        """
        print("\n-- Login --")
        try:
            user_id = input("Enter your ID: ").strip()
            
            if not user_id.isdigit():
                print("Please enter a valid ID (number).")
                return None
                
            user_id = int(user_id)
            
            # Use getpass for secure password input (no echo)
            try:
                password = getpass.getpass("Enter your password: ")
            except Exception:
                # Fallback to regular input if getpass is not available (e.g., in some IDEs)
                password = input("Enter your password: ")
            
            # Hash the password before checking
            hashed_password = self._hash_password(password)
            
            user = self.library.get_user_by_credentials(user_id, hashed_password)
            
            if user:
                print(f"Welcome back, {user.name}!")
                return user
            else:
                print("Invalid ID or password. Please try again.")
                return None
                
        except ValueError:
            print("Please enter a valid ID (number).")
            return None
            
    def _register(self):
        """Handle new user registration with password security and validation"""
        print("\n-- New User Registration --")
        try:
            # Validate user ID
            while True:
                user_id_input = input("Enter a new user ID (numbers only): ").strip()
                if not user_id_input.isdigit():
                    print("ID must be a number. Please try again.")
                    continue
                    
                user_id = int(user_id_input)
                
                # Check if ID already exists
                exists = False
                for user in self.library.get_all_users():
                    if user.id == user_id:
                        exists = True
                        break
                        
                if exists:
                    print("This ID is already taken. Please choose another one.")
                    continue
                
                break
            
            # Validate name
            while True:
                name = input("Enter your name: ").strip()
                if not name:
                    print("Name cannot be empty. Please try again.")
                    continue
                if len(name) < 3:
                    print("Name must be at least 3 characters long. Please try again.")
                    continue
                break
            
            # Validate password with minimum requirements
            while True:
                try:
                    password = getpass.getpass("Enter a password (at least 6 characters): ")
                except Exception:
                    password = input("Enter a password (at least 6 characters): ")
                
                if len(password) < 6:
                    print("Password must be at least 6 characters long.")
                    continue
                
                try:
                    confirm_password = getpass.getpass("Confirm your password: ")
                except Exception:
                    confirm_password = input("Confirm your password: ")
                
                if password != confirm_password:
                    print("Passwords do not match. Please try again.")
                    continue
                
                break
            
            # Hash the password before storing
            hashed_password = self._hash_password(password)
            
            user = self.library.add_user(user_id, name, hashed_password)
            
            if user:
                print("Registration successful!\nYou can now login.")
                
        except KeyboardInterrupt:
            print("\nRegistration cancelled by user.")
        except Exception as e:
            print(f"An error occurred during registration: {e}")
    
    def _hash_password(self, password):
        """Hash a password for secure storage using SHA-256"""
        # In a real system, you would use a salt and a more secure algorithm like bcrypt
        # This is a simplified version for demonstration purposes
        return hashlib.sha256(password.encode()).hexdigest()