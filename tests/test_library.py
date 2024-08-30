import pytest
from library import Library, Book

def test_add_book():
    library = Library()
    book = Book("123456789", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    assert len(library.available_books()) == 1
