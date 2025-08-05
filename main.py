class Library:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def getBookData(bookData, maxQuantity=None):
        if not maxQuantity:
            return bookData  # Return the bookData
        if maxQuantity > len(bookData):
            print(
                f"That is too much, please select a value between 0 and {len(bookData)}"
            )
        return bookData[0:maxQuantity]

    @staticmethod
    def getBook(bookData, query):
        return [book for book in bookData if book["name"] == query]


bookData = [
    {"name": "Book 1", "author": "Author 1"},
    {"name": "Book 2", "author": "Author 2"},
]

books = Library.getBookData(bookData)
print(f"Requested books: {books}")

bookQuery = Library.getBook(bookData=bookData, query="Book 2")
print(f"Book Requested (Name): {bookQuery}")
