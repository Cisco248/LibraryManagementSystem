"""
Book Repository Module

This module provides data persistence operations for books using CSV storage.
Implements the repository pattern for decoupling data access from business logic.
"""

import csv
import os
from models._book_model import BookModel


class BookRepository:
    """
    Repository class for managing book data persistence.

    This class handles all CRUD operations for books, storing data in a CSV file
    for simplicity. In a production system, this would interface with a database.

    Attributes:
        csv_file (str): Path to the CSV file storing book data.

    Examples:
        >>> repo = BookRepository()
        >>> book = BookModel(isbn="978-0-123456-78-9", title="Python 101", ...)
        >>> repo.add_book(book)
    """

    def __init__(self, csv_file: str = "data/books.csv"):
        """
        Initialize the BookRepository.

        Args:
            csv_file (str): Path to the CSV file. Defaults to 'data/books.csv'.
        """
        self.csv_file = csv_file
        self._ensure_csv_exists()

    def _ensure_csv_exists(self) -> None:
        """
        Ensure the CSV file and directory exist. Create if missing.

        This method creates the data directory and CSV file with headers
        if they don't already exist.
        """
        os.makedirs(os.path.dirname(self.csv_file) or "data", exist_ok=True)

        if not os.path.exists(self.csv_file):
            with open(self.csv_file, "w", newline="") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=[
                        "isbn",
                        "title",
                        "author",
                        "publisher",
                        "publication_year",
                        "quantity",
                        "book_type",
                        "status",
                        "file_format",
                        "file_size",
                    ],
                )
                writer.writeheader()

    def add_book(self, book: BookModel) -> BookModel:
        """
        Add a new book to the repository.

        Args:
            book (BookModel): The book to add.

        Returns:
            BookModel: The added book object.

        Raises:
            ValueError: If a book with the same ISBN already exists.

        Example:
            >>> book = BookModel(isbn="978-0-123456-78-9", ...)
            >>> added_book = repo.add_book(book)
        """
        # Check if book already exists
        if self.get_book(book.isbn):
            raise ValueError(f"Book with ISBN '{book.isbn}' already exists.")

        try:
            with open(self.csv_file, "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self._get_fieldnames())
                writer.writerow(book.to_dict())
            return book
        except Exception as e:
            raise Exception(f"Error adding book: {str(e)}")

    def get_book(self, isbn: str) -> dict:
        """
        Retrieve a book by ISBN.

        Args:
            isbn (str): The ISBN of the book to retrieve.

        Returns:
            dict: Book data if found, None otherwise.

        Example:
            >>> book = repo.get_book("978-0-123456-78-9")
            >>> if book:
            ...     print(book['title'])
        """
        try:
            with open(self.csv_file, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["isbn"] == isbn:
                        return row
            return row
        except Exception as e:
            raise Exception(f"Error retrieving book: {str(e)}")

    def get_all_books(self) -> list:
        """
        Retrieve all books from the repository.

        Returns:
            list: List of all books as dictionaries.

        Example:
            >>> all_books = repo.get_all_books()
            >>> for book in all_books:
            ...     print(book['title'])
        """
        try:
            with open(self.csv_file, "r", newline="") as file:
                reader = csv.DictReader(file)
                return list(reader)
        except Exception as e:
            raise Exception(f"Error retrieving all books: {str(e)}")

    def update_book(self, isbn: str, updates: dict):
        """
        Update a book's information.

        Args:
            isbn (str): The ISBN of the book to update.
            updates (dict): Dictionary of fields to update.

        Returns:
            dict: Updated book data if successful.

        Raises:
            ValueError: If book not found.

        Example:
            >>> repo.update_book("978-0-123456-78-9", {"quantity": 10})
        """
        books = self.get_all_books()
        book_found = False
        updated_books = []

        for book in books:
            if book["isbn"] == isbn:
                book_found = True
                book.update(updates)
            updated_books.append(book)

        if not book_found:
            raise ValueError(f"Book with ISBN '{isbn}' not found.")

        try:
            with open(self.csv_file, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self._get_fieldnames())
                writer.writeheader()
                writer.writerows(updated_books)
            return updated_books[0] if updated_books else None
        except Exception as e:
            raise Exception(f"Error updating book: {str(e)}")

    def delete_book(self, isbn: str) -> bool:
        """
        Delete a book from the repository.

        Args:
            isbn (str): The ISBN of the book to delete.

        Returns:
            bool: True if deletion successful, False otherwise.

        Example:
            >>> success = repo.delete_book("978-0-123456-78-9")
        """
        books = self.get_all_books()
        original_count = len(books)
        filtered_books = [book for book in books if book["isbn"] != isbn]

        if len(filtered_books) == original_count:
            raise ValueError(f"Book with ISBN '{isbn}' not found.")

        try:
            with open(self.csv_file, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self._get_fieldnames())
                writer.writeheader()
                writer.writerows(filtered_books)
            return True
        except Exception as e:
            raise Exception(f"Error deleting book: {str(e)}")

    def search_book(self, **criteria) -> list:
        """
        Search for books by multiple criteria.

        Args:
            **criteria: Field-value pairs to search for (isbn, title, author, etc.).

        Returns:
            list: List of books matching the criteria.

        Example:
            >>> results = repo.search_book(author="Python", title="Programming")
        """
        books = self.get_all_books()
        results = []

        for book in books:
            match = True
            for field, value in criteria.items():
                if field not in book or value.lower() not in book[field].lower():
                    match = False
                    break
            if match:
                results.append(book)

        return results

    def _get_fieldnames(self) -> list:
        """
        Get CSV fieldnames.

        Returns:
            list: List of field names for CSV.
        """
        return [
            "isbn",
            "title",
            "author",
            "publisher",
            "publication_year",
            "quantity",
            "book_type",
            "status",
            "file_format",
            "file_size",
        ]
