"""
Author Model Module

This module defines the AuthorModel class representing an author entity
in the library management system.
"""


class AuthorModel:
    """
    Represents an author entity in the library system.

    Attributes:
        author_id (str): Unique identifier for the author.
        name (str): Full name of the author.
        biography (str): Biography or description of the author.
        country (str): Country of origin.
        birth_year (int): Year the author was born.

    Examples:
        >>> author = AuthorModel(
        ...     author_id="A001",
        ...     name="J.K. Rowling",
        ...     biography="British author",
        ...     country="United Kingdom",
        ...     birth_year=1965
        ... )
    """

    def __init__(
        self,
        author_id: str,
        name: str,
        biography: str = "",
        country: str = "",
        birth_year: int = 0,
    ):
        """
        Initialize an AuthorModel instance.

        Args:
            author_id (str): Unique identifier.
            name (str): Author's full name.
            biography (str, optional): Author's biography. Defaults to "".
            country (str, optional): Author's country. Defaults to "".
            birth_year (int, optional): Birth year. Defaults to None.

        Raises:
            ValueError: If required fields are empty or invalid.
        """
        if not author_id or not isinstance(author_id, str):
            raise ValueError("Author ID must be a non-empty string.")
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")

        self.author_id = author_id
        self.name = name
        self.biography = biography
        self.country = country
        self.birth_year = birth_year

    def to_dict(self) -> dict:
        """
        Convert the AuthorModel instance to a dictionary.

        Returns:
            dict: Dictionary representation of the author.
        """
        return {
            "author_id": self.author_id,
            "name": self.name,
            "biography": self.biography,
            "country": self.country,
            "birth_year": self.birth_year,
        }

    def __repr__(self) -> str:
        """Return string representation of AuthorModel."""
        return f"AuthorModel(author_id='{self.author_id}', name='{self.name}')"
