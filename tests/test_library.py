import sys
import os
import pytest

# Add the parent directory to the system path so that library modules can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from library_management_system.models import Book
from library_management_system.library import Library


# Test case for adding a book to the library
def test_add_book():
    library = Library()
    book = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    assert len(library.available_books()) == 1


# Test cases for adding a book without necessary parameters

# Test case where ISBN is missing
def test_add_book_missing_isbn():
    with pytest.raises(Exception, match="All parameters are necessary."):
        Book('', 'Test Book', 'Author', 2022)

# Test case where title is missing
def test_add_book_missing_title():
    with pytest.raises(Exception, match="All parameters are necessary."):
        Book('123', '', 'Author', 2022)

# Test case where author is missing
def test_add_book_missing_author():
    with pytest.raises(Exception, match="All parameters are necessary."):
        Book('123', 'Test Book', '', 2022)

# Test case where publication year is missing
def test_add_book_missing_year():
    with pytest.raises(Exception, match="All parameters are necessary."):
        Book('123', 'Test Book', 'Author', '')

# Test case where publication year is invalid (not a positive integer)
def test_add_book_invalid_year():
    with pytest.raises(Exception, match="Year must be a positive integer."):
        Book('123', 'Test Book', 'Author', -2022)


# Test case for borrowing a book from the library
def test_borrow_book():
    library = Library()
    book = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    library.borrow_book("123456789")
    assert len(library.available_books()) == 0


# Test case for attempting to borrow a book that is not available
def test_borrow_book_if_book_is_not_available():
    library = Library()
    with pytest.raises(Exception, match="Book not available"):
        library.borrow_book("123456789")

def test_borrow_book_if_book_is_not_available():
    library = Library()
    book = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    library.borrow_book("123456789")
    with pytest.raises(Exception, match="Book not available"):
        library.borrow_book("123456789")


# Test case for returning a borrowed book to the library
def test_return_book():
    library = Library()
    book = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    library.borrow_book("123456789")
    library.return_book("123456789")
    assert len(library.available_books()) == 1


# Test case for attempting to return a book that is not available in the library
def test_return_book_if_book_is_not_available():
    library = Library()
    with pytest.raises(Exception, match="Book not found or not borrowed"):
        library.return_book("123456789")


# Test case for viewing the list of available books in the library
def test_view_available_books():
    library = Library()
    book1 = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book2 = Book("987654321", "1984", "George Orwell", 1949)
    library.add_book(book1)
    library.add_book(book2)
    library.borrow_book("123456789")
    available_books = library.available_books()
    
    # Check if only one book is available
    assert len(available_books) == 1
    
    # Check if the available book has the correct ISBN
    assert available_books[0].isbn == "987654321"

if __name__ == "__main__":
    pytest.main()