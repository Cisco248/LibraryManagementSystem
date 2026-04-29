"""
Member Model Module

This module defines the MemberModel class representing a library member entity
in the library management system.
"""


class MemberModel:

    def __init__(
        self,
        member_id: str,
        member_name: str,
        contact_no: str,
        age: int,
        membership_type: str,
        membership_status: str = "active",
    ):

        if not member_id or not isinstance(member_id, str):
            raise ValueError("Member ID must be a non-empty string.")
        if not member_name or not isinstance(member_name, str):
            raise ValueError("Member name must be a non-empty string.")
        if not contact_no or not isinstance(contact_no, str):
            raise ValueError("Contact number must be a non-empty string.")
        if not isinstance(age, int):
            raise ValueError("Age must be an integer.")
        if not membership_type or not isinstance(membership_type, str):
            raise ValueError("Membership type must be a non-empty string.")

        self.member_id = member_id
        self.member_name = member_name
        self.contact_no = contact_no
        self.age = age
        self.membership_type = membership_type
        self.membership_status = membership_status

    def to_dict(self) -> dict:
        return {
            "member_id": self.member_id,
            "name": self.member_name,
            "contact_no": self.contact_no,
            "age": self.age,
            "membership_type": self.membership_type,
            "membership_status": self.membership_status,
        }

    def to_tuple(self) -> tuple:
        return (
            self.member_id,
            self.member_name,
            self.contact_no,
            self.age,
            self.membership_type,
            self.membership_status,
        )

    def __repr__(self) -> str:
        return f"member_id={self.member_id}, name={self.member_name}"
