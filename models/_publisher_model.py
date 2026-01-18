"""
Publisher Model Module

This module defines the PublisherModel class representing a publisher entity
in the library management system.
"""


class PublisherModel:
    """
    Represents a publisher entity in the library system.

    Attributes:
        publisher_id (str): Unique identifier for the publisher.
        name (str): Name of the publisher.
        country (str): Country where the publisher is based.
        email (str): Contact email address.
        phone (str): Contact phone number.

    Examples:
        >>> publisher = PublisherModel(
        ...     publisher_id="P001",
        ...     name="Tech Press",
        ...     country="USA",
        ...     email="contact@techpress.com",
        ...     phone="555-0100"
        ... )
    """

    def __init__(
        self,
        publisher_id: str,
        name: str,
        country: str = "",
        email: str = "",
        phone: str = "",
    ):
        """
        Initialize a PublisherModel instance.

        Args:
            publisher_id (str): Unique publisher identifier.
            name (str): Publisher's name.
            country (str, optional): Publisher's country. Defaults to "".
            email (str, optional): Publisher's email. Defaults to "".
            phone (str, optional): Publisher's phone. Defaults to "".

        Raises:
            ValueError: If required fields are empty or invalid.
        """
        if not publisher_id or not isinstance(publisher_id, str):
            raise ValueError("Publisher ID must be a non-empty string.")
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")

        self.publisher_id = publisher_id
        self.name = name
        self.country = country
        self.email = email
        self.phone = phone

    def to_dict(self) -> dict:
        """
        Convert the PublisherModel instance to a dictionary.

        Returns:
            dict: Dictionary representation of the publisher.
        """
        return {
            "publisher_id": self.publisher_id,
            "name": self.name,
            "country": self.country,
            "email": self.email,
            "phone": self.phone,
        }

    def __repr__(self) -> str:
        """Return string representation of PublisherModel."""
        return f"PublisherModel(publisher_id='{self.publisher_id}', name='{self.name}')"
