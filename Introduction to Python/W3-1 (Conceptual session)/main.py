"""
Library Management System

A simple system to manage books, users, borrowing, and returning in a library.
Complete with secure authentication, persistence, and separate interfaces for
users and administrators.
"""

import os
import hashlib
import time

from library import Library
from authentication import AuthenticationSystem
from user_interface import UserInterface
from admin_interface import AdminInterface

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def setup_library():
    """Initialize the library with some sample data if it's a new installation"""
    library = Library("Central Library")
    
    # Check if this is a new installation (no users exist)
    if not library.get_all_users():
        print("First-time setup: Creating admin account and sample data...")
        print("This might take a moment...")
        time.sleep(3)
        
        # Create data directory
        os.makedirs("data", exist_ok=True)
        
        # Add admin user with hashed password
        admin_password = hashlib.sha256("admin123".encode()).hexdigest()
        admin = library.add_user(1, "admin", admin_password, role="admin")
        
        # Add some sample books
        library.add_book(101, "Python Programming", 5, "John Smith", "Programming", "9781234567890")
        library.add_book(102, "Java Essentials", 3, "Alice Johnson", "Programming", "9789876543210")
        library.add_book(103, "Data Structures and Algorithms", 4, "Bob Davis", "Computer Science", "9780123456789")
        library.add_book(104, "Web Development Basics", 2, "Sarah Wilson", "Web Development", "9785432167890")
        library.add_book(105, "Introduction to Database Systems", 3, "Michael Brown", "Database", "9789874561230")
        library.add_book(106, "Machine Learning Fundamentals", 2, "Emily Taylor", "Data Science", "9783216549870")
        library.add_book(107, "The Art of Fiction", 3, "David Miller", "Literature", "9786549873210")
        library.add_book(108, "History of Ancient Civilizations", 1, "James Wilson", "History", "9784567891230")
        library.add_book(109, "Modern Physics", 2, "Robert Johnson", "Science", "9781597534682")
        library.add_book(110, "Financial Management", 3, "Patricia Lee", "Business", "9789517534682")
        
        print("Sample data created successfully!")
        print("Default admin credentials:\n")
        print("ID: 1")
        print("Password: admin123")
        
        time.sleep(2)  # Give user time to read the message
        
    return library

def display_welcome():
    """Display welcome message"""
    clear_screen()
    print("\n" + "="*60)
    print("LIBRARY MANAGEMENT SYSTEM".center(60))
    print("="*60)
    print("\nWelcome to the Library Management System!")
    print("This application allows users to browse, borrow, and return books.")
    print("Administrators can manage books, users, and generate reports.")
    print("\nVersion: 1.0.0")
    print("Created: March 2025 by Shariful Islam")
    
    print("\nPress Enter to continue...")
    input()

def main():
    """Main function to run the library management system"""
    try:
        # Display welcome message
        display_welcome()
        
        # Setup library
        library = setup_library()
        
        # Create authentication system
        auth_system = AuthenticationSystem(library)
        
        while True:
            # Clear screen
            clear_screen()
            
            # Handle authentication
            user = auth_system.display_auth_menu()
            
            if user:
                clear_screen()
                
                # Check if user has admin role
                if hasattr(user, 'role') and user.role == "admin":
                    # Show admin interface
                    admin_interface = AdminInterface(library, user)
                    admin_interface.display_menu()
                else:
                    # Show regular user interface
                    user_interface = UserInterface(library, user)
                    user_interface.display_menu()
    
    except KeyboardInterrupt:
        clear_screen()
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\nThank you for using the Library Management System!")
        print("Goodbye!")


if __name__ == "__main__":
    main()