# Main Class, notice the static methods used to interact with the data 
# Notice there is no "state" assiend to the library other than the name used for placeholder
class Library:
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
