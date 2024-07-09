# programming_paradigm/library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False  # Book is already checked out

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            return False  # Book was not checked out

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"{title} has been checked out.")
                else:
                    print(f"{title} is not available for checkout.")
                return
        print(f"{title} is not in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"{title} has been returned.")
                else:
                    print(f"{title} was not checked out.")
                return
        print(f"{title} is not in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")
