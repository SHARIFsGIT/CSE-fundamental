"""
Admin interface for the Library Management System.
Allows administrators to manage books, users, and generate reports.
"""

class AdminInterface:
    """
    Interface for library administrators to manage the library.
    """
    def __init__(self, library, admin_user):
        self.library = library
        self.admin_user = admin_user
        
    def display_menu(self):
        """Display admin menu and handle admin operations"""
        while True:
            print("\n" + "="*50)
            print(f"ADMIN DASHBOARD - {self.library.name}".center(50))
            print("="*50)
            print(f"Logged in as: {self.admin_user.name} (Admin)")
            
            print("\nMANAGE BOOKS:")
            print("  1. Add new book")
            print("  2. Update book")
            print("  3. Remove book")
            print("  4. View all books")
            print("  5. Search books")
            
            print("\nMANAGE USERS:")
            print("  6. View all users")
            print("  7. View borrowed books")
            print("  8. Check overdue books")
            
            print("\nREPORTS:")
            print("  9. Generate library reports")
            
            print("\nSYSTEM:")
            print("  0. Logout")
            
            try:
                choice = input("\nEnter your choice (0-9): ").strip()
                
                if choice == "1":
                    self._add_book()
                elif choice == "2":
                    self._update_book()
                elif choice == "3":
                    self._remove_book()
                elif choice == "4":
                    self._view_all_books()
                elif choice == "5":
                    self._search_books()
                elif choice == "6":
                    self._view_all_users()
                elif choice == "7":
                    self._view_borrowed_books()
                elif choice == "8":
                    self._check_overdue_books()
                elif choice == "9":
                    self._generate_reports()
                elif choice == "0":
                    print("\nLogging out from admin account...")
                    return None
                else:
                    print("\nInvalid choice. Please enter a number between 0 and 9.")
                
                # Pause before showing menu again
                input("\nPress Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                return None
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                
    def _add_book(self):
        """Add a new book to the library"""
        print("\n" + "-"*50)
        print("ADD NEW BOOK".center(50))
        print("-"*50)
        
        try:
            while True:
                book_id_input = input("Enter book ID (number): ").strip()
                if not book_id_input.isdigit():
                    print("Book ID must be a number. Please try again.")
                    continue
                book_id = int(book_id_input)
                break
                
            book_name = input("Enter book title: ").strip()
            if not book_name:
                print("Book title cannot be empty.")
                return
                
            author = input("Enter author name: ").strip()
            category = input("Enter category/genre: ").strip()
            isbn = input("Enter ISBN (optional): ").strip()
            
            while True:
                quantity_input = input("Enter quantity: ").strip()
                if not quantity_input.isdigit():
                    print("Quantity must be a number. Please try again.")
                    continue
                quantity = int(quantity_input)
                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue
                break
                
            self.library.add_book(book_id, book_name, quantity, author, category, isbn)
            
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error: {e}")
            
    def _update_book(self):
        """Update an existing book"""
        print("\n" + "-"*50)
        print("UPDATE BOOK".center(50))
        print("-"*50)
        
        try:
            while True:
                book_id_input = input("Enter ID of book to update: ").strip()
                if not book_id_input.isdigit():
                    print("Book ID must be a number. Please try again.")
                    continue
                book_id = int(book_id_input)
                break
                
            book = self.library.get_book_by_id(book_id)
            if not book:
                print(f"Book with ID {book_id} not found.")
                return
                
            print(f"\nUpdating Book: {book.name} (ID: {book.id})")
            print("Leave fields blank to keep current values.")
            
            name = input(f"Title [{book.name}]: ").strip()
            name = None if not name else name
            
            author = input(f"Author [{book.author}]: ").strip()
            author = None if not author else author
            
            category = input(f"Category [{book.category}]: ").strip()
            category = None if not category else category
            
            isbn = input(f"ISBN [{book.isbn}]: ").strip()
            isbn = None if not isbn else isbn
            
            quantity = None
            while True:
                quantity_input = input(f"Quantity [{book.quantity}]: ").strip()
                if not quantity_input:
                    break
                if not quantity_input.isdigit():
                    print("Quantity must be a number. Please try again.")
                    continue
                quantity = int(quantity_input)
                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue
                break
                
            self.library.update_book(book_id, name, quantity, author, category, isbn)
            
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error: {e}")
            
    def _remove_book(self):
        """Remove a book from the library"""
        print("\n" + "-"*50)
        print("REMOVE BOOK".center(50))
        print("-"*50)
        
        try:
            while True:
                book_id_input = input("Enter ID of book to remove: ").strip()
                if not book_id_input.isdigit():
                    print("Book ID must be a number. Please try again.")
                    continue
                book_id = int(book_id_input)
                break
                
            book = self.library.get_book_by_id(book_id)
            if not book:
                print(f"Book with ID {book_id} not found.")
                return
                
            print(f"\nAre you sure you want to remove: {book.name} (ID: {book.id})?")
            confirm = input("Type 'yes' to confirm: ").strip().lower()
            
            if confirm == 'yes':
                self.library.remove_book(book_id)
            else:
                print("Operation cancelled.")
                
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error: {e}")
            
    def _view_all_books(self):
        """View all books in the library"""
        books = self.library.get_all_books()
        
        print("\n" + "-"*82)
        print("ALL BOOKS".center(82))
        print("-"*82)
        
        if not books:
            print("\nNo books in the library.")
            return
            
        print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Category':<15} {'Available':<10}")
        print("-" * 82)
        
        for book in books:
            borrowed = len(book.borrowed_by)
            total = book.quantity + borrowed
            print(f"{book.id:<5} {book.name[:28]:<30} {book.author[:18]:<20} {book.category[:13]:<15} {book.quantity}/{total}")
            
        print(f"\nTotal Books: {len(books)}")
            
    def _view_all_users(self):
        """View all registered users"""
        users = self.library.get_all_users()
        
        print("\n" + "-"*60)
        print("ALL USERS".center(60))
        print("-"*60)
        
        if not users:
            print("\nNo registered users.")
            return
            
        print(f"{'ID':<5} {'Name':<20} {'Role':<10} {'Email':<20} {'Books':<5}")
        print("-" * 60)
        
        for user in users:
            borrowed = len(user.borrowed_books)
            email = user.email if hasattr(user, 'email') else ""
            role = user.role if hasattr(user, 'role') else "user"
            print(f"{user.id:<5} {user.name[:18]:<20} {role:<10} {email[:18]:<20} {borrowed:<5}")
            
        print(f"\nTotal Users: {len(users)}")
            
    def _view_borrowed_books(self):
        """View all currently borrowed books"""
        books = self.library.get_all_books()
        
        print("\n" + "-"*50)
        print("BORROWED BOOKS".center(50))
        print("-"*50)
        
        found = False
        
        for book in books:
            if book.borrowed_by:
                found = True
                print(f"\nBook: {book.name} (ID: {book.id})")
                print("Borrowed by:")
                for user in book.borrowed_by:
                    print(f"  - {user.name} (ID: {user.id})")
                    
        if not found:
            print("No books are currently borrowed.")
            
    def _check_overdue_books(self):
        """Check for overdue books"""
        overdue_books = self.library.get_overdue_books()
        
        print("\n" + "-"*70)
        print("OVERDUE BOOKS".center(70))
        print("-"*70)
        
        if not overdue_books:
            print("No overdue books.")
            return
            
        print(f"{'User':<20} {'Book':<30} {'Days Overdue':<15}")
        print("-" * 70)
        
        for user, book, days in overdue_books:
            print(f"{user.name[:18]:<20} {book.name[:28]:<30} {days:<15}")
            
        print(f"\nTotal Overdue: {len(overdue_books)} book(s)")
            
    def _search_books(self):
        """Search for books by name, author, or category"""
        print("\n" + "-"*50)
        print("SEARCH BOOKS".center(50))
        print("-"*50)
        
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
            borrowed = len(book.borrowed_by)
            total = book.quantity + borrowed
            print(f"{book.id:<5} {book.name[:28]:<30} {book.author[:18]:<20} {book.quantity}/{total}")
            
        print(f"\nFound {len(results)} book(s).")
            
    def _generate_reports(self):
        """Generate and display library reports"""
        print("\n" + "-"*50)
        print("LIBRARY REPORTS".center(50))
        print("-"*50)
        
        reports = self.library.generate_reports()
        
        # Display inventory summary
        inventory = reports.get("inventory", {})
        print("\nINVENTORY SUMMARY:")
        print(f"Total unique books: {inventory.get('total_books', 0)}")
        print(f"Total copies: {inventory.get('total_copies', 0)}")
        print(f"Available copies: {inventory.get('available_copies', 0)}")
        print(f"Borrowed copies: {inventory.get('borrowed_copies', 0)}")
        
        # Display popular books
        popular_books = reports.get("popular_books", [])
        if popular_books:
            print("\nMOST POPULAR BOOKS:")
            print(f"{'Rank':<5} {'Title':<30} {'Author':<20} {'Borrows':<8}")
            print("-" * 65)
            
            for i, (book, count) in enumerate(popular_books, 1):
                print(f"{i:<5} {book.name[:28]:<30} {book.author[:18]:<20} {count:<8}")
        
        # Display active users
        active_users = reports.get("active_users", [])
        if active_users:
            print("\nMOST ACTIVE USERS:")
            print(f"{'Rank':<5} {'Name':<20} {'Books Borrowed':<15}")
            print("-" * 42)
            
            for i, (user, count) in enumerate(active_users, 1):
                print(f"{i:<5} {user.name[:18]:<20} {count:<15}")
        
        # Display overdue books
        overdue_books = reports.get("overdue_books", [])
        if overdue_books:
            print("\nOVERDUE BOOKS:")
            print(f"{'User':<20} {'Book':<30} {'Days Overdue':<15}")
            print("-" * 70)
            
            for user, book, days in overdue_books:
                print(f"{user.name[:18]:<20} {book.name[:28]:<30} {days:<15}")
                
            print(f"\nTotal Overdue: {len(overdue_books)} book(s)")