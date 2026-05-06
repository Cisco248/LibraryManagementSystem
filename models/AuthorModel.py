from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass(slots=True)
class AuthorModel:
    author_id: str
    author_name: str
    address: str
    gov_reg_no: str
    agreement_time: str

    def validate(self):
        if not self.author_id:
            raise ValueError("author_id is required")

        if not self.author_name:
            raise ValueError("author_name is required")

        if not self.gov_reg_no:
            raise ValueError("gov_reg_no is required")

    def to_dict(self) -> dict:
        return {
            "author_id": self.author_id,
            "author_name": self.author_name,
            "address": self.address,
            "gov_reg_no": self.gov_reg_no,
            "agreement_time": self.agreement_time,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            author_id=str(data.get("author_id", "")).strip(),
            author_name=str(data.get("author_name", "")).strip(),
            address=str(data.get("address", "")).strip(),
            gov_reg_no=str(data.get("gov_reg_no", "")).strip(),
            agreement_time=str(data.get("agreement_time", "")).strip(),
        )

    def to_tuple(self):
        return (
            self.author_id,
            self.author_name,
            self.address,
            self.gov_reg_no,
            self.agreement_time,
        )

    @classmethod
    def from_tuple(cls, data: tuple):
        return cls(*map(str, data))

    def __repr__(self):
        return f"AuthorModel(id={self.author_id}, name='{self.author_name}', gov_reg_no='{self.gov_reg_no}')"

    def __str__(self):
        return (
            f"ID={self.author_id}, Name={self.author_name}, "
            f"Address={self.address}, Government Registration No={self.gov_reg_no}, "
            f"Agreement Time={self.agreement_time}"
        )
