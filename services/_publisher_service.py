"""
Publisher Service Module

Provides business logic for publisher-related operations.
"""

from models._publisher_model import PublisherModel
from repository._publisher_repository import PublisherRepository


class PublisherService:
    """Service class for managing publisher business logic."""

    def __init__(self):
        """Initialize the PublisherService with a repository."""
        self.repository = PublisherRepository()

    def add_publisher(self, publisher_data: dict) -> PublisherModel:
        """Add a new publisher to the system."""
        try:
            publisher = PublisherModel(**publisher_data)
            return self.repository.add_publisher(publisher)
        except Exception as e:
            raise ValueError(f"Error adding publisher: {str(e)}")

    def get_publisher(self, publisher_id: str) -> dict:
        """Retrieve a publisher by ID."""
        return self.repository.get_publisher(publisher_id)

    def get_all_publishers(self) -> list:
        """Get all publishers in the system."""
        return self.repository.get_all_publishers()

    def update_publisher(self, publisher_id: str, updates: dict) -> dict:
        """Update publisher information."""
        return self.repository.update_publisher(publisher_id, updates)

    def delete_publisher(self, publisher_id: str) -> bool:
        """Delete a publisher from the system."""
        return self.repository.delete_publisher(publisher_id)

    def search_publishers(self, **criteria) -> list:
        """Search for publishers by various criteria."""
        return self.repository.search_publisher(**criteria)
