from dataclasses import dataclass
from typing import Any, Dict, Tuple


@dataclass(slots=True)
class MemberModel:
    member_id: str
    member_name: str
    contact_no: str
    age: int
    membership_type: str
    membership_status: str

    def validate(self):
        if not self.member_id or not isinstance(self.member_id, str):
            raise ValueError("Member ID must be a non-empty string.")
        if not self.member_name or not isinstance(self.member_name, str):
            raise ValueError("Member name must be a non-empty string.")
        if not self.contact_no or not isinstance(self.contact_no, str):
            raise ValueError("Contact number must be a non-empty string.")
        if not isinstance(self.age, int):
            raise ValueError("Age must be an integer.")
        if not self.membership_type or not isinstance(self.membership_type, str):
            raise ValueError("Membership type must be a non-empty string.")

    def to_dict(self) -> Dict[str, str]:
        return {
            "member_id": self.member_id,
            "member_name": self.member_name,
            "contact_no": self.contact_no,
            "age": str(self.age),
            "membership_type": self.membership_type,
            "membership_status": self.membership_status,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> MemberModel:
        return cls(
            member_id=str(data.get("member_id", "")).strip(),
            member_name=str(data.get("member_name", "")).strip(),
            contact_no=str(data.get("contact_no", "")).strip(),
            age=int(data.get("age", "")),
            membership_type=str(data.get("membership_type", "")).strip(),
            membership_status=str(data.get("membership_status", "")).strip(),
        )

    def to_tuple(self) -> Tuple[str, str, str, str, str, str]:
        return (
            self.member_id,
            self.member_name,
            self.contact_no,
            self.age.__str__(),
            self.membership_type,
            self.membership_status,
        )

    @classmethod
    def from_tupple(cls, data: Tuple[str, str, str, str, str, str]) -> MemberModel:
        return cls(
            member_id=data[0],
            member_name=data[1],
            contact_no=data[2],
            age=int(data[3]),
            membership_type=data[4],
            membership_status=data[5],
        )

    def __repr__(self) -> str:
        return f"MemberModel(member_id={self.member_id}, name={self.member_name}, contact_no={self.contact_no}, age={self.age}, membership_type={self.membership_type}, membership_status={self.membership_status})"

    def to_string(self) -> str:
        return f"ID={self.member_id}, Name={self.member_name}, Contact No={self.contact_no}, Age={self.age}, Membership Type={self.membership_type}, Membership Status={self.membership_status}"
