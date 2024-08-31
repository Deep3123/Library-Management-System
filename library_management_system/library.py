class Library:
    def __init__(self):
        # Initialize with an empty book list
        self.books = []

    def add_book(self, book):
        # Add a book to the library.
        self.books.append(book)

    def available_books(self):
        # Get a list of available (not borrowed) books.
        return [book for book in self.books if not book.is_borrowed]
    
    def borrow_book(self, isbn):
        """
        Mark a book as borrowed if available.
        Raises an exception if the book is not available.
        """
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                return
        raise Exception("Book not available")

    def return_book(self, isbn):
        """
        Mark a borrowed book as returned.
        Raises an exception if the book is not found or was not borrowed.
        """
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                return
        raise Exception("Book not found or not borrowed")
