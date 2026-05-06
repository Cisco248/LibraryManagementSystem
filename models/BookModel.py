from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Tuple


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


@dataclass(slots=True)
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

    def to_dict(self) -> Dict[str, str]:
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

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> BookModel:
        return cls(
            isbn=str(data.get("isbn", "")).strip(),
            title=str(data.get("title", "")).strip(),
            author=str(data.get("author", "")).strip(),
            publisher=str(data.get("publisher", "")).strip(),
            category=str(data.get("category", "")).strip(),
            publication_year=str(data.get("publication_year", "")).strip(),
            book_type=BookType(data.get("book_type", "")),
            status=BookStatus(data.get("status", "")),
            file_format=FileFormat(data.get("file_format", "")),
            price=str(data.get("price", "")).strip(),
            ratings=str(data.get("ratings", "")).strip(),
        )

    def to_tuple(self) -> Tuple[str, str, str, str, str, str, str, str, str, str, str]:
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

    @classmethod
    def from_tuple(cls, data: Tuple) -> BookModel:
        return cls(
            isbn=data[0],
            title=data[1],
            author=data[2],
            publisher=data[3],
            category=data[4],
            publication_year=data[5],
            book_type=data[6],
            status=data[7],
            file_format=data[8],
            price=data[9],
            ratings=data[10],
        )

    def __repr__(self) -> str:
        return f"BookModel(isbn={self.isbn}, title={self.title}, author={self.author}, publisher={self.publisher}, category={self.category}, publication_year={self.publication_year}, book_type={self.book_type.value}, status={self.status.value}, file_format={self.file_format.value}, price={self.price}, ratings={self.ratings})"

    def to_string(self) -> str:
        return f"ISBN:{self.isbn}, Title:{self.title}, Author:{ self.author}, Publisher:{self.publisher}, Category:{ self.category}, Year:{self.publication_year}, Type:{self.book_type}, Status:{self.status}, File Format:{self.file_format}, Price:{self.price}, Ratings:{self.ratings}"
