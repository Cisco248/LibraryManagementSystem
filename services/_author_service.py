"""
Author Service Module

Provides business logic for author-related operations.
"""

from models._author_model import AuthorModel
from repository._author_repository import AuthorRepository


class AuthorService:
    """Service class for managing author business logic."""

    def __init__(self):
        self.repository = AuthorRepository()

    def add_author(self, author_data: dict) -> AuthorModel:
        try:
            author = AuthorModel(**author_data)
            return self.repository.add_author(author)
        except Exception as e:
            raise ValueError(f"Error adding author: {str(e)}")

    def get_author(self, author_id: str) -> dict:
        return self.repository.get_author(author_id)

    def get_all_authors(self) -> list:
        return self.repository.get_all_authors()

    def update_author(self, author_id: str, updates: dict) -> dict:
        return self.repository.update_author(author_id, updates)

    def delete_author(self, author_id: str) -> bool:
        return self.repository.delete_author(author_id)

    def search_authors(self, **criteria) -> list:
        return self.repository.search_author(**criteria)
