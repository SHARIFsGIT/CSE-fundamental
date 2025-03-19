"""
Data models for the Library Management System.
Defines Book and User classes with their attributes and methods.
"""
from datetime import datetime

class Book:
    """
    Represents a book in the library.
    
    Attributes:
        id (int): Unique identifier for the book
        name (str): Name of the book
        quantity (int): Number of copies available
        author (str): Author of the book
        category (str): Category/genre of the book
        isbn (str): ISBN of the book
        borrowed_by (list): List of users who borrowed this book
        date_added (datetime): Date when the book was added to the library
    """
    def __init__(self, id, name, quantity, author="Unknown", category="General", isbn=""):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.author = author
        self.category = category
        self.isbn = isbn
        self.borrowed_by = []  # List of users who borrowed this book
        self.date_added = datetime.now()
        
    def __str__(self):
        return f"Book(id={self.id}, name='{self.name}', author='{self.author}', quantity={self.quantity})"
    
    def to_dict(self):
        """Convert book object to dictionary for JSON serialization"""
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "author": self.author,
            "category": self.category,
            "isbn": self.isbn,
            "date_added": self.date_added.isoformat() if hasattr(self, 'date_added') else None,
            # We don't include borrowed_by as it will be reconstructed from User objects
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a Book object from dictionary data"""
        book = cls(
            id=data["id"],
            name=data["name"],
            quantity=data["quantity"],
            author=data.get("author", "Unknown"),
            category=data.get("category", "General"),
            isbn=data.get("isbn", "")
        )
        
        # Set date_added if available
        if "date_added" in data and data["date_added"]:
            try:
                book.date_added = datetime.fromisoformat(data["date_added"])
            except (ValueError, TypeError):
                book.date_added = datetime.now()         
        return book
        
        
class User:
    """
    Represents a user of the library.
    
    Attributes:
        id (int): Unique identifier for the user
        name (str): Name of the user
        password (str): User's hashed password
        email (str): User's email address
        role (str): User's role (e.g., "admin", "user")
        borrowed_books (list): Books currently borrowed by the user
        return_history (list): Books previously returned by the user
        join_date (datetime): Date when the user joined the library
    """
    def __init__(self, id, name, password, email="", role="user"):
        self.id = id
        self.name = name
        self.password = password  # Hashed password
        self.email = email
        self.role = role
        self.borrowed_books = []  # Books currently borrowed
        self.return_history = []  # Books previously returned
        self.join_date = datetime.now()
        
    def __str__(self):
        return f"User(id={self.id}, name='{self.name}', role='{self.role}')"
    
    def is_admin(self):
        """Check if the user has admin privileges"""
        return self.role == "admin"
        
    def get_borrowed_books(self):
        """Returns a list of books currently borrowed by the user"""
        return self.borrowed_books
    
    def get_return_history(self):
        """Returns a list of books previously returned by the user"""
        return self.return_history
    
    def to_dict(self):
        """Convert user object to dictionary for JSON serialization"""
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,  # Already hashed
            "email": self.email,
            "role": self.role,
            "join_date": self.join_date.isoformat() if hasattr(self, 'join_date') else None,
            "borrowed_book_ids": [book.id for book in self.borrowed_books],
            "return_history_ids": [book.id for book in self.return_history]
        }
    
    @classmethod
    def from_dict(cls, data, books_map=None):
        """
        Create a User object from dictionary data
        
        Args:
            data (dict): User data dictionary
            books_map (dict): Dictionary mapping book IDs to Book objects for restoring relationships
        """
        user = cls(
            id=data["id"],
            name=data["name"],
            password=data["password"],
            email=data.get("email", ""),
            role=data.get("role", "user")
        )
        
        # Set join_date if available
        if "join_date" in data and data["join_date"]:
            try:
                user.join_date = datetime.fromisoformat(data["join_date"])
            except (ValueError, TypeError):
                user.join_date = datetime.now()
        
        # Restore borrowed books and history if books_map provided
        if books_map:
            if "borrowed_book_ids" in data:
                for book_id in data["borrowed_book_ids"]:
                    if book_id in books_map:
                        user.borrowed_books.append(books_map[book_id])
                        
            if "return_history_ids" in data:
                for book_id in data["return_history_ids"]:
                    if book_id in books_map:
                        user.return_history.append(books_map[book_id])
        return user


class BorrowRecord:
    """
    Represents a record of a book borrowing transaction.
    
    Attributes:
        user_id (int): ID of the user who borrowed the book
        book_id (int): ID of the borrowed book
        borrow_date (datetime): Date when the book was borrowed
        due_date (datetime): Date when the book is due to be returned
        return_date (datetime): Date when the book was returned (None if not returned)
    """
    def __init__(self, user_id, book_id, borrow_date=None, due_date=None):
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date or datetime.now()
        
        # Default due date is 14 days from borrow date
        if due_date is None:
            # For simplicity, set due date to 14 days from borrow
            from datetime import timedelta
            self.due_date = self.borrow_date + timedelta(days=14)
        else:
            self.due_date = due_date
            
        self.return_date = None
        
    def is_returned(self):
        """Check if the book has been returned"""
        return self.return_date is not None
        
    def is_overdue(self):
        """Check if the book is overdue"""
        if self.is_returned():
            return False
        return datetime.now() > self.due_date
        
    def mark_as_returned(self):
        """Mark the book as returned"""
        self.return_date = datetime.now()
        
    def to_dict(self):
        """Convert record to dictionary for JSON serialization"""
        return {
            "user_id": self.user_id,
            "book_id": self.book_id,
            "borrow_date": self.borrow_date.isoformat(),
            "due_date": self.due_date.isoformat(),
            "return_date": self.return_date.isoformat() if self.return_date else None
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a BorrowRecord from dictionary data"""
        record = cls(
            user_id=data["user_id"],
            book_id=data["book_id"]
        )
        
        # Parse dates
        if "borrow_date" in data:
            record.borrow_date = datetime.fromisoformat(data["borrow_date"])
            
        if "due_date" in data:
            record.due_date = datetime.fromisoformat(data["due_date"])
            
        if "return_date" in data and data["return_date"]:
            record.return_date = datetime.fromisoformat(data["return_date"])
            
        return record