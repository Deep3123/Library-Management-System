class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def available_books(self):
        return [book for book in self.books if not book.is_borrowed]
    
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                return
        raise Exception("Book not available")
