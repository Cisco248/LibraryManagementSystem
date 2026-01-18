"""
Member Model Module

This module defines the MemberModel class representing a library member entity
in the library management system.
"""


class MemberModel:
    """
    Represents a library member in the system.

    Attributes:
        member_id (str): Unique identifier for the member.
        name (str): Full name of the member.
        email (str): Email address.
        phone (str): Phone number.
        membership_date (str): Date when membership was created (YYYY-MM-DD).
        status (str): Membership status ('active', 'inactive', 'suspended').

    Examples:
        >>> member = MemberModel(
        ...     member_id="M001",
        ...     name="John Smith",
        ...     email="john@example.com",
        ...     phone="555-1234",
        ...     membership_date="2023-01-15",
        ...     status="active"
        ... )
    """

    def __init__(
        self,
        member_id: str,
        name: str,
        email: str,
        phone: str,
        membership_date: str,
        status: str = "active",
    ):
        """
        Initialize a MemberModel instance.

        Args:
            member_id (str): Unique member identifier.
            name (str): Member's full name.
            email (str): Member's email address.
            phone (str): Member's phone number.
            membership_date (str): Date of membership in YYYY-MM-DD format.
            status (str, optional): Membership status. Defaults to 'active'.

        Raises:
            ValueError: If required fields are empty or invalid.
        """
        if not member_id or not isinstance(member_id, str):
            raise ValueError("Member ID must be a non-empty string.")
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if not email or not isinstance(email, str):
            raise ValueError("Email must be a non-empty string.")
        if not phone or not isinstance(phone, str):
            raise ValueError("Phone must be a non-empty string.")
        if not membership_date or not isinstance(membership_date, str):
            raise ValueError(
                "Membership date must be a non-empty string in YYYY-MM-DD format."
            )
        if status not in ("active", "inactive", "suspended"):
            raise ValueError(
                "Status must be one of: 'active', 'inactive', 'suspended'."
            )

        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.membership_date = membership_date
        self.status = status

    def to_dict(self) -> dict:
        """
        Convert the MemberModel instance to a dictionary.

        Returns:
            dict: Dictionary representation of the member.
        """
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "membership_date": self.membership_date,
            "status": self.status,
        }

    def __repr__(self) -> str:
        """Return string representation of MemberModel."""
        return f"MemberModel(member_id='{self.member_id}', name='{self.name}')"
