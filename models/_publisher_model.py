from dataclasses import dataclass


@dataclass
class PublisherModel:

    pub_id: int
    name: str
    address: str
    contact_no: str
    gov_license: bool

    def to_dict(self):
        return {
            "author_id": self.pub_id,
            "name": self.name,
            "address": self.address,
            "contact_no": self.contact_no,
            "gov_license": self.gov_license,
        }

    def to_string(self):
        return f"\nID: {self.pub_id}\nName: {self.name}\nAddress: {self.address}\nContact No: {self.contact_no}\nGov_License: {self.gov_license}\n"
