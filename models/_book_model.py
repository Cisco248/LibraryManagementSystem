from dataclasses import dataclass


@dataclass
class BookModel:
    """
    A class representing a Book in a library system.

    Attributes:
        isbn (int): The unique ISBN number of the book.
        title (str): The title of the book.
        author (str): The author of the book.
        publisher (str): The publisher of the book.
        status (bool): Availability status of the book. True if available, False if unavailable.

    Methods:
        to_dict() -> dict:
            Converts the BookModel instance into a dictionary.
        __post_init__():
            Validate data after initialization.
    """

    isbn: str
    title: str
    author: str
    publisher: str
    category: str
    status: str

    def to_dict(self) -> dict:
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "publisher": self.publisher,
            "category": self.category,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            isbn=data["isbn"],
            title=data["title"],
            author=data["author"],
            publisher=data["publisher"],
            category=data["category"],
            status=data["status"],
        )

    def to_string(self):
        return f"ISBN: {self.isbn}\n Title: {self.title}\n Author: {self.author}\n Publisher: {self.publisher}\n Category: {self.category}\n Status: {self.status}"
