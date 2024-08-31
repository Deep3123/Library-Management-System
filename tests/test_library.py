import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from library_management_system.models import Book
from library_management_system.library import Library


# testing add book feature
def test_add_book():
    library = Library()
    book = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    assert len(library.available_books()) == 1


# testing add book feature without necessary parameters  
def test_add_book_missing_isbn():
    with pytest.raises(Exception):
        Book('', 'Test Book', 'Author', 2022)

def test_add_book_missing_title():
    with pytest.raises(Exception):
        Book('123', '', 'Author', 2022)

def test_add_book_missing_author():
    with pytest.raises(Exception):
        Book('123', 'Test Book', '', 2022)

def test_add_book_missing_year():
    with pytest.raises(Exception):
        Book('123', 'Test Book', 'Author', '')
    
    
# testing borrow book feature
def test_borrow_book():
    library = Library()
    book = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    library.borrow_book("123456789")
    assert len(library.available_books()) == 0
    

# testing borrow book feature if book is not available
def test_borrow_book_if_book_is_not_available():
    library = Library()
    with pytest.raises(Exception):
        library.borrow_book("123456789")


# testing return book feature
def test_return_book():
    library = Library()
    book = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    library.borrow_book("123456789")
    library.return_book("123456789")
    assert len(library.available_books()) == 1


# testing return book feature if book is not available
def test_return_book_if_book_is_not_available():
    library = Library()
    with pytest.raises(Exception):
        library.return_book("123456789")
        
        
# testing view available books feature    
def test_view_available_books():
    library = Library()
    book1 = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book2 = Book("987654321", "1984", "George Orwell",1949)
    library.add_book(book1)
    library.add_book(book2)
    library.borrow_book("123456789")
    available_books = library.available_books()
    assert len(available_books) == 1
    assert available_books[0].isbn == "987654321"