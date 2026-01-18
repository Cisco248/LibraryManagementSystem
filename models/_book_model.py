"""
Book Model Module

This module defines the BookModel class representing a book entity
in the library management system.
"""


class BookModel:
    """
    Represents a book entity in the library system.

    Attributes:
        isbn (str): International Standard Book Number (unique identifier).
        title (str): The title of the book.
        author (str): The author of the book.
        publisher (str): The publisher of the book.
        publication_year (int): The year the book was published.
        book_type (str): Type of book ('printed' or 'ebook').
        status (str): Status of printed books ('available', 'checked_out', 'damaged', 'lost').
        file_format (str): Format of e-book ('pdf', 'epub', 'mobi').
        file_size (float): Size of e-book file in MB.

    Examples:
        >>> book = BookModel(
        ...     isbn="978-0-123456-78-9",
        ...     title="Python Programming",
        ...     author="John Doe",
        ...     publisher="Tech Press",
        ...     publication_year=2023,
        ...     book_type="printed",
        ...     status="available"
        ... )
    """

    def __init__(
        self,
        isbn: str,
        title: str,
        author: str,
        publisher: str,
        publication_year: int,
        book_type: str = "printed",
        status: str = "available",
        file_format: str = "",
        file_size: float = 0.0,
    ):
        """
        Initialize a BookModel instance.

        Args:
            isbn (str): Unique identifier for the book.
            title (str): Title of the book.
            author (str): Author of the book.
            publisher (str): Publisher of the book.
            publication_year (int): Year of publication.
            book_type (str, optional): 'printed' or 'ebook'. Defaults to 'printed'.
            status (str, optional): Book status. Defaults to 'available'.
            file_format (str, optional): E-book format. Defaults to None.
            file_size (float, optional): E-book size in MB. Defaults to None.

        Raises:
            ValueError: If required fields are empty or invalid.
        """
        if not isbn or not isinstance(isbn, str):
            raise ValueError("ISBN must be a non-empty string.")

        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")

        if not author or not isinstance(author, str):
            raise ValueError("Author must be a non-empty string.")

        if not publisher or not isinstance(publisher, str):
            raise ValueError("Publisher must be a non-empty string.")

        if not isinstance(publication_year, int) or publication_year < 1000:
            raise ValueError("Publication year must be a valid year (>= 1000).")

        if book_type not in ("printed", "ebook"):
            raise ValueError("Book type must be 'printed' or 'ebook'.")

        if status not in ("available", "checked_out", "damaged", "lost"):
            raise ValueError(
                "Status must be one of: 'available', 'checked_out', 'damaged', 'lost'."
            )

        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_year = publication_year
        self.book_type = book_type
        self.status = status
        self.file_format = file_format
        self.file_size = file_size

    def to_dict(self) -> dict:
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "publisher": self.publisher,
            "publication_year": self.publication_year,
            "book_type": self.book_type,
            "status": self.status,
            "file_format": self.file_format,
            "file_size": self.file_size,
        }

    def to_string(self) -> str:
        return f"ISBN: {self.isbn}\n Title: {self.title}\n Author: {self.author}"
