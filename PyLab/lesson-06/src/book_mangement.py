import random


# Base class for all types of books
class Book:
    total_books = 0  # Class property to count total books

    def __init__(self, title, author, isbn):
        self.title = title  # Instance property
        self.author = author  # Instance property
        self.isbn = isbn  # Instance property
        Book.total_books += 1  # Increment total books when a book is created

    @classmethod
    def get_total_books(cls):  # Class method to get total books
        return cls.total_books

    def display_info(self):  # Instance method to display book info
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    @staticmethod
    def generate_random_isbn():  # Static method to generate a random ISBN
        # Generate a random 10 or 13 digit ISBN
        isbn_length = random.choice([10, 13])
        return "".join(random.choices("0123456789", k=isbn_length))


# Inherited class for EBook
class EBook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)  # Call parent constructor
        self.file_size = file_size  # Instance property

    def display_info(self):  # Polymorphism: overriding display_info method
        parent_info = super().display_info()
        return f"{parent_info}, File Size: {self.file_size} MB"


# Inherited class for PrintedBook
class PrintedBook(Book):
    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)  # Call parent constructor
        self.pages = pages  # Instance property

    def display_info(self):  # Polymorphism: overriding display_info method
        parent_info = super().display_info()
        return f"{parent_info}, Pages: {self.pages}"


# Library class to manage books
class Library:
    def __init__(self):
        self.books = []  # Instance property to hold books

    def add_book(self, book):
        self.books.append(book)  # Add book to library

    def display_books(self):
        for book in self.books:
            print(book.display_info())  # Display information for each book

    @staticmethod
    def is_valid_isbn(isbn):
        # Static method to validate ISBN
        return len(isbn) in {10, 13}


# Example usage
if __name__ == "__main__":
    library = Library()

    # Creating instances of books
    book1 = PrintedBook("1984", "George Orwell", "1234567890", 328)
    book2 = EBook("The Great Gatsby", "F. Scott Fitzgerald", "0987654321", 2.5)

    # Adding books to the library
    library.add_book(book1)
    library.add_book(book2)

    # Displaying all books in the library
    print("Books in the library:")
    library.display_books()

    # Display total number of books
    print(f"Total number of books: {Book.get_total_books()}")

    # Validate ISBN
    isbn_to_check = "1234567890"
    print(f"Is ISBN {isbn_to_check} valid? {Library.is_valid_isbn(isbn_to_check)}")
