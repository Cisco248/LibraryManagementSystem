"""
Author Repository Module

Handles data persistence operations for authors using CSV storage.
"""

import csv
import os
from config.settings import AUTHORS_CSV, AUTHOR_FIELDS
from models._author_model import AuthorModel


class AuthorRepository:
    """Repository class for managing author data persistence."""

    def __init__(self, csv_file: str = AUTHORS_CSV):
        """Initialize the AuthorRepository."""
        self.csv_file = csv_file
        self._ensure_csv_exists()

    def _ensure_csv_exists(self) -> None:
        """Ensure CSV file and directory exist."""
        os.makedirs(os.path.dirname(self.csv_file) or "database", exist_ok=True)

        if not os.path.exists(self.csv_file):
            with open(self.csv_file, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=AUTHOR_FIELDS)
                writer.writeheader()

    def add_author(self, author: AuthorModel) -> AuthorModel:
        """Add a new author."""
        if self.get_author(author.author_id):
            raise ValueError(f"Author with ID '{author.author_id}' already exists.")

        try:
            with open(self.csv_file, "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=AUTHOR_FIELDS)
                writer.writerow(author.to_dict())
            return author
        except Exception as e:
            raise Exception(f"Error adding author: {str(e)}")

    def get_author(self, author_id: str):
        """Retrieve an author by ID."""
        try:
            with open(self.csv_file, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["author_id"] == author_id:
                        return row
            return None
        except Exception as e:
            raise Exception(f"Error retrieving author: {str(e)}")

    def get_all_authors(self) -> list:
        """Retrieve all authors."""
        try:
            with open(self.csv_file, "r", newline="") as file:
                reader = csv.DictReader(file)
                return list(reader)
        except Exception as e:
            raise Exception(f"Error retrieving all authors: {str(e)}")

    def update_author(self, author_id: str, updates: dict):
        """Update an author's information."""
        authors = self.get_all_authors()
        author_found = False
        updated_authors = []

        for author in authors:
            if author["author_id"] == author_id:
                author_found = True
                author.update(updates)
            updated_authors.append(author)

        if not author_found:
            raise ValueError(f"Author with ID '{author_id}' not found.")

        try:
            with open(self.csv_file, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=AUTHOR_FIELDS)
                writer.writeheader()
                writer.writerows(updated_authors)
            return updated_authors[0] if updated_authors else None
        except Exception as e:
            raise Exception(f"Error updating author: {str(e)}")

    def delete_author(self, author_id: str) -> bool:
        """Delete an author."""
        authors = self.get_all_authors()
        original_count = len(authors)
        filtered_authors = [
            author for author in authors if author["author_id"] != author_id
        ]

        if len(filtered_authors) == original_count:
            raise ValueError(f"Author with ID '{author_id}' not found.")

        try:
            with open(self.csv_file, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=AUTHOR_FIELDS)
                writer.writeheader()
                writer.writerows(filtered_authors)
            return True
        except Exception as e:
            raise Exception(f"Error deleting author: {str(e)}")

    def search_author(self, **criteria) -> list:
        """Search for authors by criteria."""
        authors = self.get_all_authors()
        results = []

        for author in authors:
            match = True
            for field, value in criteria.items():
                if field not in author or value.lower() not in author[field].lower():
                    match = False
                    break
            if match:
                results.append(author)

        return results
