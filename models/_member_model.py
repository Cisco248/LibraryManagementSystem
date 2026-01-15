from dataclasses import asdict, dataclass


@dataclass
class MemberModel:

    member_id: int
    member_name: str
    contact_no: int
    age: int
    membership_status: str

    def to_dict(self):
        return asdict(self)

    def __post_init__(self):
        if not self.member_id:
            raise ValueError("ID Cannot be empty!")
        if not self.member_name:
            raise ValueError("Name Cannot be empty")
