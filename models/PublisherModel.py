from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass(slots=True)
class PublisherModel:
    publisher_id: str
    publisher_name: str
    address: str
    gov_reg_no: str
    agreement_time: str

    def validate(self):
        if not self.publisher_id or not isinstance(self.publisher_id, str):
            raise ValueError("Publisher ID must be a non-empty string.")
        if not self.publisher_name or not isinstance(self.publisher_name, str):
            raise ValueError("Publisher Name must be a non-empty string.")

    def to_dict(self) -> Dict[str, str]:
        return {
            "publisher_id": self.publisher_id,
            "publisher_name": self.publisher_name,
            "address": self.address,
            "gov_reg_no": self.gov_reg_no,
            "agreement_time": self.agreement_time,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> PublisherModel:
        return cls(
            publisher_id=str(data.get("publisher_id", "").strip()),
            publisher_name=str(data.get("publisher_name", "").strip()),
            address=str(data.get("address", "").strip()),
            gov_reg_no=str(data.get("gov_reg_no", "").strip()),
            agreement_time=str(data.get("agreement_time", "").strip()),
        )

    def to_tuple(self) -> Tuple[str, str, str, str, str]:
        return (
            self.publisher_id,
            self.publisher_name,
            self.address,
            self.gov_reg_no,
            self.agreement_time,
        )

    @classmethod
    def from_tuple(cls, data: Tuple[str, str, str, str, str]) -> PublisherModel:
        return cls(*map(str, data))

    def __repr__(self) -> str:
        return f"PublisherModel(publisher_id: {self.publisher_id}, publisher_name: {self.publisher_name}, address: {self.address}, gov_reg_no: {self.gov_reg_no}, agreement_time: {self.agreement_time})"

    def to_string(self) -> str:
        return f"ID={self.publisher_id}, Name={self.publisher_name}, Address= {self.address}, Government Registration No={self.gov_reg_no}, Agreement Time= {self.agreement_time}"
