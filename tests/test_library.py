import pytest
from library_management_system.models import Book
from library_management_system.library import Library

def test_add_book():
    library = Library()
    book = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    assert len(library.available_books()) == 1
    
def test_borrow_book():
    library = Library()
    book = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    library.borrow_book("123456789")
    assert len(library.available_books()) == 0
    
def test_return_book():
    library = Library()
    book = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    library.borrow_book("123456789")
    library.return_book("123456789")
    assert len(library.available_books()) == 1