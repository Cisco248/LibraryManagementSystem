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
        self.repository = BookRepository()

    def add_book(self, book_data: dict) -> BookModel:
        try:
            book = BookModel(**book_data)
            return self.repository.add_book(book)
        except Exception as e:
            raise ValueError(f"Error adding book: {str(e)}")

    def get_book(self, isbn: str) -> dict:
        return self.repository.get_book(isbn)

    def get_all_books(self) -> list:
        return self.repository.get_all_books()

    def get_all_available_books(self) -> list:
        try:
            all_books = self.repository.get_all_books()
            return [book for book in all_books if int(book.get("quantity", 0)) > 0]
        except Exception as e:
            raise Exception(f"Error retrieving available books: {str(e)}")

    def update_book(self, isbn: str, updates: dict):
        return self.repository.update_book(isbn, updates)

    def delete_book(self, isbn: str) -> bool:
        return self.repository.delete_book(isbn)

    def search_books(self, **criteria) -> list:
        return self.repository.search_book(**criteria)
