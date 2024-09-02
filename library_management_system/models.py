class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Book:
    def __init__(self, isbn, title, author, year):
                
        # Validate all parameters
        if(not isbn or not title or not author or not year):
            raise Exception("All parameters are necessary.")
        
        # Validate year as an integer
        if not isinstance(year, int) or year <= 0:
            raise Exception("Year must be a positive integer.")
        
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False