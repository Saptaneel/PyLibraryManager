class Library:
    def __init__(self):
        # Initialize the library with no books
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        # Add a book to the library and update the book count
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        # Display the number of books and list all book titles
        print(f"The library has {self.noBooks} books. The books are:")
        for book in self.books:
            print(book)

# Example usage
l1 = Library()
l1.addBook("Harry Potter1")
l1.addBook("Harry Potter2")
l1.addBook("Harry Potter3")
l1.showInfo()
