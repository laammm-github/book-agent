"""Book library management."""


class BookLibrary:
    def __init__(self):
        self.books = []

    def add(self, title: str, content: str):
        book = {"title": title, "content": content}
        self.books.append(book)
        return book

    def list_books(self):
        return self.books
