"""
Member Service Module

Provides business logic for member-related operations.
"""

from models._member_model import MemberModel
from repository._member_repository import MemberRepository


class MemberService:
    """Service class for managing member business logic."""

    def __init__(self):
        """Initialize the MemberService with a repository."""
        self.repository = MemberRepository()

    def add_member(self, member_data: dict) -> MemberModel:
        """Add a new member to the system."""
        try:
            member = MemberModel(**member_data)
            return self.repository.add_member(member)
        except Exception as e:
            raise ValueError(f"Error adding member: {str(e)}")

    def get_member(self, member_id: str) -> dict:
        """Retrieve a member by ID."""
        return self.repository.get_member(member_id)

    def get_all_members(self) -> list:
        """Get all members in the system."""
        return self.repository.get_all_members()

    def update_member(self, member_id: str, updates: dict) -> dict:
        """Update member information."""
        return self.repository.update_member(member_id, updates)

    def delete_member(self, member_id: str) -> bool:
        """Delete a member from the system."""
        return self.repository.delete_member(member_id)

    def search_members(self, **criteria) -> list:
        """Search for members by various criteria."""
        return self.repository.search_member(**criteria)

    def get_active_members(self) -> list:
        """Get all active members."""
        all_members = self.repository.get_all_members()
        return [m for m in all_members if m.get("status", "").lower() == "active"]
