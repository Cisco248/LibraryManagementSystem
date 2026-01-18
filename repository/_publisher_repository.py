"""
Publisher Repository Module

Handles data persistence operations for publishers using CSV storage.
"""

import csv
import os
from config.settings import PUBLISHERS_CSV, PUBLISHER_FIELDS
from models._publisher_model import PublisherModel


class PublisherRepository:
    """Repository class for managing publisher data persistence."""

    def __init__(self, csv_file: str = PUBLISHERS_CSV):
        """Initialize the PublisherRepository."""
        self.csv_file = csv_file
        self._ensure_csv_exists()

    def _ensure_csv_exists(self) -> None:
        """Ensure CSV file and directory exist."""
        os.makedirs(os.path.dirname(self.csv_file) or "database", exist_ok=True)

        if not os.path.exists(self.csv_file):
            with open(self.csv_file, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=PUBLISHER_FIELDS)
                writer.writeheader()

    def add_publisher(self, publisher: PublisherModel) -> PublisherModel:
        """Add a new publisher."""
        if self.get_publisher(publisher.publisher_id):
            raise ValueError(
                f"Publisher with ID '{publisher.publisher_id}' already exists."
            )

        try:
            with open(self.csv_file, "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=PUBLISHER_FIELDS)
                writer.writerow(publisher.to_dict())
            return publisher
        except Exception as e:
            raise Exception(f"Error adding publisher: {str(e)}")

    def get_publisher(self, publisher_id: str) -> dict:
        """Retrieve a publisher by ID."""
        try:
            with open(self.csv_file, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["publisher_id"] == publisher_id:
                        return row
            return None
        except Exception as e:
            raise Exception(f"Error retrieving publisher: {str(e)}")

    def get_all_publishers(self) -> list:
        """Retrieve all publishers."""
        try:
            with open(self.csv_file, "r", newline="") as file:
                reader = csv.DictReader(file)
                return list(reader)
        except Exception as e:
            raise Exception(f"Error retrieving all publishers: {str(e)}")

    def update_publisher(self, publisher_id: str, updates: dict) -> dict:
        """Update a publisher's information."""
        publishers = self.get_all_publishers()
        publisher_found = False
        updated_publishers = []

        for publisher in publishers:
            if publisher["publisher_id"] == publisher_id:
                publisher_found = True
                publisher.update(updates)
            updated_publishers.append(publisher)

        if not publisher_found:
            raise ValueError(f"Publisher with ID '{publisher_id}' not found.")

        try:
            with open(self.csv_file, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=PUBLISHER_FIELDS)
                writer.writeheader()
                writer.writerows(updated_publishers)
            return updated_publishers[0] if updated_publishers else None
        except Exception as e:
            raise Exception(f"Error updating publisher: {str(e)}")

    def delete_publisher(self, publisher_id: str) -> bool:
        """Delete a publisher."""
        publishers = self.get_all_publishers()
        original_count = len(publishers)
        filtered_publishers = [
            publisher
            for publisher in publishers
            if publisher["publisher_id"] != publisher_id
        ]

        if len(filtered_publishers) == original_count:
            raise ValueError(f"Publisher with ID '{publisher_id}' not found.")

        try:
            with open(self.csv_file, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=PUBLISHER_FIELDS)
                writer.writeheader()
                writer.writerows(filtered_publishers)
            return True
        except Exception as e:
            raise Exception(f"Error deleting publisher: {str(e)}")

    def search_publisher(self, **criteria) -> list:
        """Search for publishers by criteria."""
        publishers = self.get_all_publishers()
        results = []

        for publisher in publishers:
            match = True
            for field, value in criteria.items():
                if (
                    field not in publisher
                    or value.lower() not in publisher[field].lower()
                ):
                    match = False
                    break
            if match:
                results.append(publisher)

        return results
