class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"{title} checked out.")
                return
        print(f"{title} not found or already checked out.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"{title} returned.")
                return
        print(f"{title} not found or already available.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")


book1 = Book("Animal farm", "orwell")
lib = Library()
lib.add_book(book1)
lib.list_available_books()