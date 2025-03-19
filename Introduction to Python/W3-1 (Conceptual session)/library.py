"""
Library class for the Library Management System.
Manages books, users, and borrowing operations.
"""
from datetime import datetime, timedelta
import json
import os
from models import Book, User, BorrowRecord

class Library:
    """
    Represents a library with books and users.
    
    Attributes:
        name (str): Name of the library
        books (list): List of books in the library
        users (list): List of registered users
        borrow_records (list): List of borrowing records
    """
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []
        self.borrow_records = []
        
        # Create data directory if it doesn't exist
        os.makedirs("data", exist_ok=True)
        
        # Load existing data if available
        self._load_data()
        
    def _load_data(self):
        """Load library data from files if they exist"""
        try:
            # First load books as they are needed for user borrowing relationships
            if os.path.exists("data/books.json"):
                with open("data/books.json", "r") as f:
                    books_data = json.load(f)
                    for book_data in books_data:
                        book = Book.from_dict(book_data)
                        self.books.append(book)
            
            # Create a book ID to book object mapping for relationship restoration
            books_map = {book.id: book for book in self.books}
            
            # Load users
            if os.path.exists("data/users.json"):
                with open("data/users.json", "r") as f:
                    users_data = json.load(f)
                    for user_data in users_data:
                        user = User.from_dict(user_data, books_map)
                        self.users.append(user)
                        
                        # Restore borrowed_by relationship for books
                        for book in user.borrowed_books:
                            if user not in book.borrowed_by:
                                book.borrowed_by.append(user)
            
            # Load borrow records
            if os.path.exists("data/borrow_records.json"):
                with open("data/borrow_records.json", "r") as f:
                    records_data = json.load(f)
                    for record_data in records_data:
                        record = BorrowRecord.from_dict(record_data)
                        self.borrow_records.append(record)
                        
        except Exception as e:
            print(f"Error loading data: {e}")
            # Initialize with empty lists to prevent crashes
            self.books = []
            self.users = []
            self.borrow_records = []
    
    def _save_data(self):
        """Save library data to files"""
        try:
            # Save books
            books_data = [book.to_dict() for book in self.books]
            with open("data/books.json", "w") as f:
                json.dump(books_data, f, indent=4)
            
            # Save users
            users_data = [user.to_dict() for user in self.users]
            with open("data/users.json", "w") as f:
                json.dump(users_data, f, indent=4)
            
            # Save borrow records
            records_data = [record.to_dict() for record in self.borrow_records]
            with open("data/borrow_records.json", "w") as f:
                json.dump(records_data, f, indent=4)
                
        except Exception as e:
            print(f"Error saving data: {e}")
            
    def add_book(self, id, name, quantity, author="Unknown", category="General", isbn=""):
        """
        Add a new book to the library.
        
        Args:
            id (int): Book ID
            name (str): Book name
            quantity (int): Number of copies
            author (str): Book author
            category (str): Book category/genre
            isbn (str): Book ISBN
            
        Returns:
            Book: The newly created book or None if already exists
        """
        # Check if book with same ID already exists
        for book in self.books:
            if book.id == id:
                print(f"Book with ID {id} already exists")
                return None
        
        # Create and add new book
        book = Book(id, name, quantity, author, category, isbn)
        self.books.append(book)
        
        # Save changes
        self._save_data()
        
        print(f"Book '{name}' (ID: {id}) added successfully")
        return book
        
    def add_user(self, id, name, password, email="", role="user"):
        """
        Register a new user.
        
        Args:
            id (int): User ID
            name (str): Username
            password (str): User password (should be pre-hashed)
            email (str): User email
            role (str): User role ("user" or "admin")
            
        Returns:
            User: The newly created user or None if already exists
        """
        # Check if user with same ID already exists
        for user in self.users:
            if user.id == id:
                print(f"User with ID {id} already exists")
                return None
        
        # Create and add new user
        user = User(id, name, password, email, role)
        self.users.append(user)
        
        # Save changes
        self._save_data()
        
        print(f"\n'{name}' with ID: {id} registered successfully as a new user.")
        return user
        
    def get_user_by_credentials(self, id, password):
        """
        Find a user by their ID and password.
        
        Args:
            id (int): User ID
            password (str): User password (hashed)
            
        Returns:
            User: The user if found, None otherwise
        """
        for user in self.users:
            if user.id == id and user.password == password:
                return user
        return None
        
    def borrow_book(self, user, book_id):
        """
        Allow a user to borrow a book.
        
        Args:
            user (User): The user borrowing the book
            book_id (int): ID of the book to borrow
            
        Returns:
            bool: True if successful, False otherwise
        """
        # Find the book
        book = None
        for b in self.books:
            if b.id == book_id:
                book = b
                break
                
        if not book:
            print(f"Book with ID {book_id} not found")
            return False
            
        # Check if already borrowed by this user
        if book in user.borrowed_books:
            print(f"Book '{book.name}' is already borrowed by you")
            return False
            
        # Check if book is available
        if book.quantity <= 0:
            print(f"Book '{book.name}' is out of stock")
            return False
            
        # Borrow the book
        book.quantity -= 1
        user.borrowed_books.append(book)
        book.borrowed_by.append(user)
        
        # Create a borrow record
        borrow_date = datetime.now()
        due_date = borrow_date + timedelta(days=14)  # Default loan period: 14 days
        record = BorrowRecord(user.id, book.id, borrow_date, due_date)
        self.borrow_records.append(record)
        
        # Save changes
        self._save_data()
        
        print(f"Book '{book.name}' borrowed successfully by {user.name}")
        print(f"Due date: {due_date.strftime('%Y-%m-%d')}")
        return True
                
    def return_book(self, user, book_id):
        """
        Allow a user to return a book.
        
        Args:
            user (User): The user returning the book
            book_id (int): ID of the book to return
            
        Returns:
            bool: True if successful, False otherwise
        """
        # Find the book
        book = None
        for b in self.books:
            if b.id == book_id:
                book = b
                break
                
        if not book:
            print(f"Book with ID {book_id} not found")
            return False
            
        # Check if borrowed by this user
        if book not in user.borrowed_books:
            print(f"Book '{book.name}' is not borrowed by you")
            return False
            
        # Return the book
        book.quantity += 1
        user.return_history.append(book)
        user.borrowed_books.remove(book)
        book.borrowed_by.remove(user)
        
        # Update borrow record
        for record in self.borrow_records:
            if record.book_id == book.id and record.user_id == user.id and not record.is_returned():
                record.mark_as_returned()
                
                # Check if book is overdue
                if record.is_overdue():
                    days_overdue = (record.return_date - record.due_date).days
                    print(f"Warning: Book returned {days_overdue} days late")
                    # In a real system, you might calculate a fine here
                break
        
        # Save changes
        self._save_data()
        
        print(f"Book '{book.name}' returned successfully by {user.name}")
        return True
        
    def get_all_books(self):
        """Returns all books in the library"""
        return self.books
        
    def get_all_users(self):
        """Returns all registered users"""
        return self.users
        
    def search_books(self, search_term):
        """
        Search for books by name, author, or category.
        
        Args:
            search_term (str): The term to search for
            
        Returns:
            list: Books matching the search term
        """
        results = []
        search_term = search_term.lower()
        
        for book in self.books:
            if (search_term in book.name.lower() or
                search_term in book.author.lower() or
                search_term in book.category.lower() or
                search_term in book.isbn.lower()):
                results.append(book)
                
        return results
    
    def get_overdue_books(self):
        """
        Get a list of overdue books.
        
        Returns:
            list: A list of tuples (user, book, days_overdue) for overdue books
        """
        overdue_list = []
        today = datetime.now()
        
        for record in self.borrow_records:
            if not record.is_returned() and record.is_overdue():
                # Find the user and book
                user = next((u for u in self.users if u.id == record.user_id), None)
                book = next((b for b in self.books if b.id == record.book_id), None)
                
                if user and book:
                    days_overdue = (today - record.due_date).days
                    overdue_list.append((user, book, days_overdue))
                    
        return overdue_list
    
    def get_book_by_id(self, book_id):
        """
        Get a book by its ID.
        
        Args:
            book_id (int): The book ID
            
        Returns:
            Book: The book if found, None otherwise
        """
        for book in self.books:
            if book.id == book_id:
                return book
        return None
    
    def get_user_by_id(self, user_id):
        """
        Get a user by their ID.
        
        Args:
            user_id (int): The user ID
            
        Returns:
            User: The user if found, None otherwise
        """
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def remove_book(self, book_id):
        """
        Remove a book from the library.
        
        Args:
            book_id (int): ID of the book to remove
            
        Returns:
            bool: True if successful, False otherwise
        """
        book = self.get_book_by_id(book_id)
        if not book:
            print(f"Book with ID {book_id} not found")
            return False
            
        # Check if the book is currently borrowed
        if book.borrowed_by:
            print(f"Cannot remove book '{book.name}' as it is currently borrowed by users")
            return False
            
        self.books.remove(book)
        self._save_data()
        
        print(f"Book '{book.name}' removed successfully")
        return True
    
    def update_book(self, book_id, name=None, quantity=None, author=None, category=None, isbn=None):
        """
        Update book information.
        
        Args:
            book_id (int): ID of the book to update
            name (str): New name (or None to keep current)
            quantity (int): New quantity (or None to keep current)
            author (str): New author (or None to keep current)
            category (str): New category (or None to keep current)
            isbn (str): New ISBN (or None to keep current)
            
        Returns:
            bool: True if successful, False otherwise
        """
        book = self.get_book_by_id(book_id)
        if not book:
            print(f"Book with ID {book_id} not found")
            return False
            
        if name is not None:
            book.name = name
            
        if quantity is not None:
            # Ensure quantity is not less than number of borrowed books
            borrowed_count = len(book.borrowed_by)
            if quantity < borrowed_count:
                print(f"Cannot set quantity less than borrowed count ({borrowed_count})")
                return False
            book.quantity = quantity
            
        if author is not None:
            book.author = author
            
        if category is not None:
            book.category = category
            
        if isbn is not None:
            book.isbn = isbn
            
        self._save_data()
        
        print(f"Book '{book.name}' updated successfully")
        return True
    
    def generate_reports(self):
        """
        Generate various library reports.
        
        Returns:
            dict: A dictionary containing various reports
        """
        reports = {}
        
        # Most popular books
        book_borrow_counts = {}
        for record in self.borrow_records:
            book_id = record.book_id
            if book_id in book_borrow_counts:
                book_borrow_counts[book_id] += 1
            else:
                book_borrow_counts[book_id] = 1
                
        popular_books = []
        for book_id, count in sorted(book_borrow_counts.items(), key=lambda x: x[1], reverse=True):
            book = self.get_book_by_id(book_id)
            if book:
                popular_books.append((book, count))
                
        reports["popular_books"] = popular_books[:10]  # Top 10 books
        
        # Overdue books
        reports["overdue_books"] = self.get_overdue_books()
        
        # Active users
        user_borrow_counts = {}
        for record in self.borrow_records:
            user_id = record.user_id
            if user_id in user_borrow_counts:
                user_borrow_counts[user_id] += 1
            else:
                user_borrow_counts[user_id] = 1
                
        active_users = []
        for user_id, count in sorted(user_borrow_counts.items(), key=lambda x: x[1], reverse=True):
            user = self.get_user_by_id(user_id)
            if user:
                active_users.append((user, count))
                
        reports["active_users"] = active_users[:10]  # Top 10 users
        
        # Book inventory summary
        total_books = len(self.books)
        total_copies = sum(book.quantity + len(book.borrowed_by) for book in self.books)
        available_copies = sum(book.quantity for book in self.books)
        borrowed_copies = sum(len(book.borrowed_by) for book in self.books)
        
        reports["inventory"] = {
            "total_books": total_books,
            "total_copies": total_copies,
            "available_copies": available_copies,
            "borrowed_copies": borrowed_copies
        }
        
        return reports