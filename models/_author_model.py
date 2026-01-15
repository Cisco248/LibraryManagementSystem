from dataclasses import dataclass


@dataclass
class Author:

    author_id: int
    name: str
    address: str
    contact_no: str
    gov_license: bool

    def to_dict(self):
        return {
            "author_id": self.author_id,
            "name": self.name,
            "address": self.address,
            "contact_no": self.contact_no,
            "gov_license": self.gov_license,
        }

    def to_string(self):
        return f"\nID: {self.author_id}\nName: {self.name}\nAddress: {self.address}\nContact No: {self.contact_no}\nGov License: {self.gov_license}\n"
