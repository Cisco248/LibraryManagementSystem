"""
Publisher Model Module

This module defines the PublisherModel class representing a publisher entity
in the library management system.
"""


class PublisherModel:

    def __init__(
        self,
        publisher_id: str,
        publisher_name: str,
        address: str = "",
        gov_reg_no: str = "",
        agreement_time: str = "",
    ):
        if not publisher_id or not isinstance(publisher_id, str):
            raise ValueError("Publisher ID must be a non-empty string.")
        if not publisher_name or not isinstance(publisher_name, str):
            raise ValueError("Publisher Name must be a non-empty string.")

        self.publisher_id = publisher_id
        self.publisher_name = publisher_name
        self.address = address
        self.gov_reg_no = gov_reg_no
        self.agreement_time = agreement_time

    def to_dict(self) -> dict:
        return {
            "publisher_id": self.publisher_id,
            "publisher_name": self.publisher_name,
            "address": self.address,
            "gov_reg_no": self.gov_reg_no,
            "agreement_time": self.agreement_time,
        }

    def to_tuple(self) -> tuple:
        return (
            self.publisher_id,
            self.publisher_name,
            self.address,
            self.gov_reg_no,
            self.agreement_time,
        )

    def __repr__(self) -> str:
        return f"publisher_id={self.publisher_id}, publisher_name={self.publisher_name}"
