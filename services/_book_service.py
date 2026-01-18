"""
Book Service Module

This module provides business logic for book-related operations.
It acts as a bridge between the controller and repository layers.
"""

from models._book_model import BookModel
from repository._book_repository import BookRepository


class BookService:
    """
    Service class for managing book business logic.

    This class provides high-level operations on books, leveraging the repository
    for data persistence.

    Attributes:
        repository (BookRepository): The repository for data operations.

    Examples:
        >>> service = BookService()
        >>> books = service.get_all_available_books()
    """

    def __init__(self):
        """Initialize the BookService with a repository."""
        self.repository = BookRepository()

    def add_book(self, book_data: dict) -> BookModel:
        """
        Add a new book to the system.

        Args:
            book_data (dict): Dictionary containing book information.

        Returns:
            BookModel: The created book object.

        Raises:
            ValueError: If book data is invalid.

        Example:
            >>> service = BookService()
            >>> book = service.add_book({
            ...     'isbn': '978-0-123456-78-9',
            ...     'title': 'Python 101',
            ...     'author': 'John Doe',
            ...     'publisher': 'Tech Press',
            ...     'publication_year': 2023,
            ...     'quantity': 5
            ... })
        """
        try:
            book = BookModel(**book_data)
            return self.repository.add_book(book)
        except Exception as e:
            raise ValueError(f"Error adding book: {str(e)}")

    def get_book(self, isbn: str) -> dict:
        """
        Retrieve a book by ISBN.

        Args:
            isbn (str): The ISBN of the book.

        Returns:
            dict: Book data if found, None otherwise.

        Example:
            >>> book = service.get_book("978-0-123456-78-9")
        """
        return self.repository.get_book(isbn)

    def get_all_books(self) -> list:
        """
        Get all books in the system.

        Returns:
            list: List of all books.

        Example:
            >>> all_books = service.get_all_books()
        """
        return self.repository.get_all_books()

    def get_all_available_books(self) -> list:
        """
        Get all books currently available (quantity > 0).

        Returns:
            list: List of available books.

        Example:
            >>> available = service.get_all_available_books()
        """
        try:
            all_books = self.repository.get_all_books()
            return [book for book in all_books if int(book.get("quantity", 0)) > 0]
        except Exception as e:
            raise Exception(f"Error retrieving available books: {str(e)}")

    def update_book(self, isbn: str, updates: dict):
        """
        Update book information.

        Args:
            isbn (str): The ISBN of the book to update.
            updates (dict): Dictionary of fields to update.

        Returns:
            dict: Updated book data.

        Example:
            >>> updated = service.update_book("978-0-123456-78-9", {"quantity": 10})
        """
        return self.repository.update_book(isbn, updates)

    def delete_book(self, isbn: str) -> bool:
        """
        Delete a book from the system.

        Args:
            isbn (str): The ISBN of the book to delete.

        Returns:
            bool: True if successful.

        Example:
            >>> success = service.delete_book("978-0-123456-78-9")
        """
        return self.repository.delete_book(isbn)

    def search_books(self, **criteria) -> list:
        """
        Search for books by various criteria.

        Args:
            **criteria: Field-value pairs to search.

        Returns:
            list: List of matching books.

        Example:
            >>> results = service.search_books(author="John", title="Python")
        """
        return self.repository.search_book(**criteria)
