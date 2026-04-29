"""
Author Model Module

This module defines the AuthorModel class representing an author entity
in the library management system.
"""


class AuthorModel:
    def __init__(
        self,
        author_id: str,
        author_name: str,
        address: str = "",
        gov_reg_no: str = "",
        agreement_time: int = 0,
    ):
        if not author_id or not isinstance(author_id, str):
            raise ValueError("Author ID must be a non-empty string.")
        if not author_name or not isinstance(author_name, str):
            raise ValueError("author_name must be a non-empty string.")

        self.author_id = author_id
        self.author_name = author_name
        self.address = address
        self.gov_reg_no = gov_reg_no
        self.agreement_time = agreement_time

    def to_dict(self) -> dict:
        return {
            "author_id": self.author_id,
            "author_name": self.author_name,
            "address": self.address,
            "gov_reg_no": self.gov_reg_no,
            "agreement_time": self.agreement_time,
        }

    def to_tuple(self):
        return (
            self.author_id,
            self.author_name,
            self.address,
            self.gov_reg_no,
            self.agreement_time,
        )

    def __repr__(self) -> str:
        return f"ID={self.author_id}, Name={self.author_name}"
