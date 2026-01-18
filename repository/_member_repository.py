"""
Member Repository Module

Handles data persistence operations for members using CSV storage.
"""

import csv
import os
from config.settings import MEMBERS_CSV, MEMBER_FIELDS
from models._member_model import MemberModel


class MemberRepository:
    """Repository class for managing member data persistence."""

    def __init__(self, csv_file: str = MEMBERS_CSV):
        """Initialize the MemberRepository."""
        self.csv_file = csv_file
        self._ensure_csv_exists()

    def _ensure_csv_exists(self) -> None:
        """Ensure CSV file and directory exist."""
        os.makedirs(os.path.dirname(self.csv_file) or "database", exist_ok=True)

        if not os.path.exists(self.csv_file):
            with open(self.csv_file, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=MEMBER_FIELDS)
                writer.writeheader()

    def add_member(self, member: MemberModel) -> MemberModel:
        """Add a new member."""
        if self.get_member(member.member_id):
            raise ValueError(f"Member with ID '{member.member_id}' already exists.")

        try:
            with open(self.csv_file, "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=MEMBER_FIELDS)
                writer.writerow(member.to_dict())
            return member
        except Exception as e:
            raise Exception(f"Error adding member: {str(e)}")

    def get_member(self, member_id: str) -> dict:
        """Retrieve a member by ID."""
        try:
            with open(self.csv_file, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["member_id"] == member_id:
                        return row
            return None
        except Exception as e:
            raise Exception(f"Error retrieving member: {str(e)}")

    def get_all_members(self) -> list:
        """Retrieve all members."""
        try:
            with open(self.csv_file, "r", newline="") as file:
                reader = csv.DictReader(file)
                return list(reader)
        except Exception as e:
            raise Exception(f"Error retrieving all members: {str(e)}")

    def update_member(self, member_id: str, updates: dict) -> dict:
        """Update a member's information."""
        members = self.get_all_members()
        member_found = False
        updated_members = []

        for member in members:
            if member["member_id"] == member_id:
                member_found = True
                member.update(updates)
            updated_members.append(member)

        if not member_found:
            raise ValueError(f"Member with ID '{member_id}' not found.")

        try:
            with open(self.csv_file, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=MEMBER_FIELDS)
                writer.writeheader()
                writer.writerows(updated_members)
            return updated_members[0] if updated_members else None
        except Exception as e:
            raise Exception(f"Error updating member: {str(e)}")

    def delete_member(self, member_id: str) -> bool:
        """Delete a member."""
        members = self.get_all_members()
        original_count = len(members)
        filtered_members = [
            member for member in members if member["member_id"] != member_id
        ]

        if len(filtered_members) == original_count:
            raise ValueError(f"Member with ID '{member_id}' not found.")

        try:
            with open(self.csv_file, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=MEMBER_FIELDS)
                writer.writeheader()
                writer.writerows(filtered_members)
            return True
        except Exception as e:
            raise Exception(f"Error deleting member: {str(e)}")

    def search_member(self, **criteria) -> list:
        """Search for members by criteria."""
        members = self.get_all_members()
        results = []

        for member in members:
            match = True
            for field, value in criteria.items():
                if field not in member or value.lower() not in member[field].lower():
                    match = False
                    break
            if match:
                results.append(member)

        return results
