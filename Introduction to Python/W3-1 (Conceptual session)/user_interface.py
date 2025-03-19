"""
User interface for the Library Management System.
Allows users to browse, search, borrow, and return books.
"""
class UserInterface:
    """
    Interface for library users to interact with the library.
    """
    def __init__(self, library, user):
        self.library = library
        self.user = user
        
    def display_menu(self):
        """Display user menu and handle user operations"""
        while True:
            print("\n" + "="*50)
            print(f"USER DASHBOARD - {self.library.name}".center(50))
            print("="*50)
            print(f"Welcome, {self.user.name}!")
            
            # Show number of currently borrowed books
            borrowed_books = len(self.user.borrowed_books)
            if borrowed_books > 0:
                print(f"You currently have {borrowed_books} book(s) borrowed.")
            
            print("\nBOOKS:")
            print("  1. Browse all books")
            print("  2. Search for books")
            print("  3. Borrow a book")
            
            print("\nMY ACCOUNT:")
            print("  4. View my borrowed books")
            print("  5. Return a book")
            print("  6. View my borrowing history")
            
            print("\nSYSTEM:")
            print("  0. Logout")
            
            try:
                choice = input("\nEnter your choice (0-6): ").strip()
                
                if choice == "1":
                    self._browse_books()
                elif choice == "2":
                    self._search_books()
                elif choice == "3":
                    self._borrow_book()
                elif choice == "4":
                    self._view_borrowed_books()
                elif choice == "5":
                    self._return_book()
                elif choice == "6":
                    self._view_history()
                elif choice == "0":
                    print("\nLogging out...")
                    return None
                else:
                    print("\nInvalid choice. Please enter a number between 0 and 6.")
                
                # Pause before showing menu again
                input("\nPress Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                return None
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                
    def _browse_books(self):
        """Browse all available books"""
        books = self.library.get_all_books()
        
        print("\n" + "-"*82)
        print("AVAILABLE BOOKS".center(82))
        print("-"*82)
        
        if not books:
            print("\nNo books in the library.")
            return
            
        print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Category':<15} {'Available':<10}")
        print("-" * 82)
        
        available_count = 0
        for book in books:
            if book.quantity > 0:  # Only show books with available copies
                available_count += 1
                borrowed = len(book.borrowed_by)
                total = book.quantity + borrowed
                print(f"{book.id:<5} {book.name[:28]:<30} {book.author[:18]:<20} {book.category[:13]:<15} {book.quantity}/{total}")
                
        if available_count == 0:
            print("\nNo books are currently available for borrowing.")
        else:
            print(f"\nTotal Available: {available_count} book(s)")
                
    def _search_books(self):
        """Search for books by name, author, or category"""
        print("\n" + "-"*50)
        print("SEARCH BOOKS".center(50))
        print("-"*50)
        print("You can search by title, author, category, or ISBN")
        
        search_term = input("\nEnter search term: ").strip()
        if not search_term:
            print("Search term cannot be empty.")
            return
            
        results = self.library.search_books(search_term)
        
        if not results:
            print(f"No books found matching '{search_term}'.")
            return
            
        print(f"\n-- Search Results for '{search_term}' --")
        print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Available':<10}")
        print("-" * 70)
        
        for book in results:
            print(f"{book.id:<5} {book.name[:28]:<30} {book.author[:18]:<20} {book.quantity:<10}")
            
        print(f"\nFound {len(results)} book(s).")
            
    def _borrow_book(self):
        """Borrow a book"""
        print("\n" + "-"*50)
        print("BORROW A BOOK".center(50))
        print("-"*50)
        
        # Show current borrowed books count
        current_borrowed = len(self.user.borrowed_books)
        print(f"You currently have {current_borrowed} book(s) borrowed.")
        
        # Optional: Set a limit on how many books a user can borrow
        max_allowed = 5  # This could be a library policy
        if current_borrowed >= max_allowed:
            print(f"\nYou've reached the maximum limit of {max_allowed} books.")
            print("Please return some books before borrowing more.")
            return
            
        try:
            book_id_input = input("\nEnter the ID of the book you want to borrow: ").strip()
            if not book_id_input.isdigit():
                print("Book ID must be a number.")
                return
                
            book_id = int(book_id_input)
            
            # Check if book exists before trying to borrow
            book = self.library.get_book_by_id(book_id)
            if not book:
                print(f"Book with ID {book_id} not found.")
                return
                
            # Check if already borrowed by this user
            if book in self.user.borrowed_books:
                print(f"You have already borrowed '{book.name}'.")
                return
                
            # Check if book is available
            if book.quantity <= 0:
                print(f"Sorry, '{book.name}' is currently out of stock.")
                return
                
            # Ask for confirmation
            print(f"\nBook: {book.name}")
            print(f"Author: {book.author}")
            print(f"Category: {book.category}")
            
            confirm = input("\nDo you want to borrow this book? (yes/no): ").strip().lower()
            if confirm != 'yes':
                print("Borrowing cancelled.")
                return
                
            self.library.borrow_book(self.user, book_id)
            
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error: {e}")
            
    def _return_book(self):
        """Return a borrowed book"""
        borrowed_books = self.user.borrowed_books
        
        print("\n" + "-"*50)
        print("RETURN A BOOK".center(50))
        print("-"*50)
        
        if not borrowed_books:
            print("\nYou don't have any borrowed books to return.")
            return
            
        print(f"{'ID':<5} {'Title':<30} {'Author':<20}")
        print("-" * 55)
        
        for book in borrowed_books:
            print(f"{book.id:<5} {book.name[:28]:<30} {book.author[:18]:<20}")
            
        try:
            book_id_input = input("\nEnter the ID of the book you want to return: ").strip()
            if not book_id_input.isdigit():
                print("Book ID must be a number.")
                return
                
            book_id = int(book_id_input)
            
            # Check if book exists and is borrowed by the user
            book = self.library.get_book_by_id(book_id)
            if not book:
                print(f"Book with ID {book_id} not found.")
                return
                
            if book not in borrowed_books:
                print(f"You haven't borrowed '{book.name}'.")
                return
                
            # Ask for confirmation
            confirm = input(f"\nReturn '{book.name}'? (yes/no): ").strip().lower()
            if confirm != 'yes':
                print("Return cancelled.")
                return
                
            self.library.return_book(self.user, book_id)
            
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error: {e}")
            
    def _view_borrowed_books(self):
        """View books currently borrowed by the user"""
        borrowed_books = self.user.borrowed_books
        
        print("\n" + "-"*70)
        print("YOUR BORROWED BOOKS".center(70))
        print("-"*70)
        
        if not borrowed_books:
            print("\nYou don't have any borrowed books.")
            return
            
        print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Due Date':<15}")
        print("-" * 70)
        
        # Get borrow records to find due dates
        for book in borrowed_books:
            # Find due date for this book
            due_date = "Unknown"
            for record in self.library.borrow_records:
                if record.book_id == book.id and record.user_id == self.user.id and not record.is_returned():
                    due_date = record.due_date.strftime("%Y-%m-%d")
                    
                    # Check if overdue
                    if record.is_overdue():
                        due_date += " (OVERDUE)"
                    break
                    
            print(f"{book.id:<5} {book.name[:28]:<30} {book.author[:18]:<20} {due_date:<15}")
            
        print(f"\nTotal Borrowed: {len(borrowed_books)}")
            
    def _view_history(self):
        """View user's borrowing history"""
        history = self.user.return_history
        
        print("\n" + "-"*50)
        print("YOUR BORROWING HISTORY".center(50))
        print("-"*50)
        
        if not history:
            print("\nYou don't have any borrowing history.")
            return
            
        print(f"{'ID':<5} {'Title':<30} {'Author':<20}")
        print("-" * 55)
        
        for book in history:
            print(f"{book.id:<5} {book.name[:28]:<30} {book.author[:18]:<20}")
            
        print(f"\nTotal Books Previously Returned: {len(history)}")