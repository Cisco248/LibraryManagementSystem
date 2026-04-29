from dataclasses import dataclass
from datetime import date
from enum import Enum


class FileFormat(Enum):
    PDF = "pdf"
    EPUB = "epub"
    MOBI = "mobi"


class BookType(Enum):
    PRINTED = "printed"
    EBOOK = "ebook"


class BookStatus(Enum):
    AVAILABLE = "available"
    CHECKED_OUT = "checked_out"
    DAMAGED = "damaged"
    LOST = "lost"


@dataclass
class BookModel:
    isbn: str
    title: str
    author: str
    publisher: str
    publication_year: date
    book_type: BookType
    status: BookStatus
    file_format: FileFormat
    file_size: float

    def to_tuple(self):
        return (
            self.isbn,
            self.title,
            self.author,
            self.publisher,
            self.publication_year,
            self.book_type.value,
            self.status.value,
            self.file_format.value,
            self.file_size,
        )

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "publisher": self.publisher,
            "publication_year": self.publication_year.isoformat(),
            "book_type": self.book_type.value,
            "status": self.status.value,
            "file_format": self.file_format.value,
            "file_size": self.file_size,
        }
