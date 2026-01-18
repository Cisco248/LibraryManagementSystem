"""
Search Controller Module

Provides search functionality across different entity types (Books, Members, Authors, Publishers).
"""

from repository._book_repository import BookRepository


class SearchController:
    """
    Controller for handling search operations across the system.

    This controller provides unified search functionality for different entity types,
    delegating to appropriate repositories.

    Attributes:
        book_repository (BookRepository): Repository for book search operations.

    Examples:
        >>> search_ctrl = SearchController()
        >>> results = search_ctrl.search_books(author="John Doe")
    """

    def __init__(self):
        """Initialize the SearchController with repositories."""
        self.book_repository = BookRepository()

    def search_books(self, **criteria) -> list:
        """
        Search for books using multiple criteria.

        Args:
            **criteria: Field-value pairs (isbn, title, author, publisher, etc.).

        Returns:
            list: List of matching books.

        Example:
            >>> results = search_ctrl.search_books(author="John", title="Python")
            >>> for book in results:
            ...     print(book['title'])
        """
        try:
            return self.book_repository.search_book(**criteria)
        except Exception as e:
            raise Exception(f"Error searching books: {str(e)}")

    def search_by_title(self, title: str) -> list:
        """
        Search for books by title.

        Args:
            title (str): The title to search for.

        Returns:
            list: List of matching books.

        Example:
            >>> books = search_ctrl.search_by_title("Python")
        """
        return self.search_books(title=title)

    def search_by_author(self, author: str) -> list:
        """
        Search for books by author.

        Args:
            author (str): The author to search for.

        Returns:
            list: List of matching books.

        Example:
            >>> books = search_ctrl.search_by_author("John Doe")
        """
        return self.search_books(author=author)

    def search_by_isbn(self, isbn: str) -> list:
        """
        Search for a book by ISBN.

        Args:
            isbn (str): The ISBN to search for.

        Returns:
            list: List containing the book if found, empty list otherwise.

        Example:
            >>> books = search_ctrl.search_by_isbn("978-0-123456-78-9")
        """
        book = self.book_repository.get_book(isbn)
        return [book] if book else []
