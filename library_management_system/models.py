class Book:
    def __init__(self, isbn, title, author, year):
        
        if(not isbn or not title or not author or not year):
            raise Exception("All parameters are necessary.")
        
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False