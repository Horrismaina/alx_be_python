# library_management.py

class Book:
    """Represents a book in the library system."""
    
    def __init__(self, title, author):
        """Initialize a new book.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Mark the book as checked out.
        
        Returns:
            bool: True if checkout was successful, False if book was already checked out
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned.
        
        Returns:
            bool: True if return was successful, False if book was not checked out
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available for checkout.
        
        Returns:
            bool: True if the book is available, False otherwise
        """
        return not self._is_checked_out
    
    def __str__(self):
        """Return string representation of the book.
        
        Returns:
            str: Book title and author in format "Title by Author"
        """
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of books and their availability."""
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []
    
    def add_book(self, book):
        """Add a book to the library.
        
        Args:
            book (Book): The book to add to the library
        """
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by its title.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if checkout was successful, False if book was not found or unavailable
        """
        book = self._find_book(title)
        if book and book.is_available():
            return book.check_out()
        return False
    
    def return_book(self, title):
        """Return a book to the library.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if return was successful, False if book was not found
        """
        book = self._find_book(title)
        if book:
            return book.return_book()
        return False
    
    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")
    
    def _find_book(self, title):
        """Find a book by its title.
        
        Args:
            title (str): The title of the book to find
            
        Returns:
            Book or None: The found book or None if not found
        """
        for book in self._books:
            if book.title == title:
                return book
        return None