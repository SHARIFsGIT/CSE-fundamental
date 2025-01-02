class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)


class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def availability(self):
        return self.__availability

    def borrow_book(self):
        if self.__availability:
            print(f"You borrowed '{self.__title}' successfully.")
            self.__availability = False
        else:
            print(f"Error: This book '{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__availability:
            print(f"The book '{self.__title}' returned to the library.")
            self.__availability = True
        else:
            print(f"Error: Book '{self.__title}' is not borrowed yet.")

    def view_book_info(self):
        status = "Available" if self.__availability else "Not available now"
        print(f"Book ID: {self.__book_id}, Title: '{self.__title}', Author: '{self.__author}', Status: {status}")


def menu():
    Library.entry_book(Book('1', 'Python Programming', 'Mr. Python'))
    Library.entry_book(Book('2', 'Java Programming', 'Mr. Java'))
    Library.entry_book(Book('3', 'C++ Programming', 'Mrs. C++'))
    Library.entry_book(Book('4', 'JavaScript Programming', 'Mr. JavaScript'))

    while True:
        print("\n=================== X ===================")
        print("Welcome to the Library Management System!")
        print("\nLibrary Menu:")
        print("[1]. View All Books")
        print("[2]. Borrow Book")
        print("[3]. Return Book")
        print("[4]. Exit")
        print("=================== X ===================\n")

        
        choice_input = input("Enter your choice: ")
        if not choice_input.isdigit():
            print("Error: Please enter a valid number.")
            continue

        choice = int(choice_input)


        if choice == 1:
            if Library.book_list:
                for book in Library.book_list:
                    book.view_book_info()
            else:
                print("No books available in the library.")

        elif choice == 2:
            book_id = input("Enter the Book ID to borrow: ")
            for book in Library.book_list:
                if book.book_id == book_id:
                    book.borrow_book()
                    break
            else:
                print("Error: Book ID not found.")

        elif choice == 3:
            book_id = input("Enter the Book ID to return: ")
            for book in Library.book_list:
                if book.book_id == book_id:
                    book.return_book()
                    break
            else:
                print("Error: Book ID not found.")

        elif choice == 4:
            print("Exiting the library system. Have a good time!")
            break

        else:
            print("Invalid choice. Enter a valid number between 1 - 4.")


menu()
