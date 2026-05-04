from dataclasses import dataclass
from enum import Enum
from typing import Any


class FileFormat(Enum):
    HARDCOPY = "HARDCOPY"
    PDF = "PDF"
    EPUB = "EPUB"
    MOBI = "MOBI"


class BookType(Enum):
    PRINTED = "Printed"
    EBOOK = "Digital"


class BookStatus(Enum):
    AVAILABLE = "Available"
    UNAVAILABLE = "Unavailable"
    BARROWED = "Borrowed"
    RESERVED = "Reserved"


@dataclass
class BookModel:
    isbn: str
    title: str
    author: str
    publisher: str
    category: str
    publication_year: str
    book_type: BookType
    status: BookStatus
    file_format: FileFormat
    price: str
    ratings: str

    def to_tuple(self):
        return (
            self.isbn,
            self.title,
            self.author,
            self.publisher,
            self.category,
            self.publication_year,
            self.book_type.value,
            self.status.value,
            self.file_format.value,
            self.price,
            self.ratings,
        )

    def from_tuple(self):
        return (
            self.isbn,
            self.title,
            self.author,
            self.publisher,
            self.category,
            self.publication_year,
            self.book_type,
            self.status,
            self.file_format,
            self.price,
            self.ratings,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "publisher": self.publisher,
            "category": self.category,
            "publication_year": self.publication_year,
            "book_type": self.book_type.value,
            "status": self.status.value,
            "file_format": self.file_format.value,
            "price": self.price,
            "ratings": self.ratings,
        }

    def to_string(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author:{ self.author}, Publisher: {self.publisher}, Category:{ self.category}, Year: {self.publication_year}, Type: {self.book_type}, Status: {self.status}, File Format: {self.file_format}, Price: {self.price}, Ratings: {self.ratings}"
