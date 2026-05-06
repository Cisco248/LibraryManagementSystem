import csv
import os
from config.Configuration import (
    MEMBER_TABLE_QUERY,
    MEMBER_IMPORT_PATH,
    MEMBER_IMPORT_QUERY,
    MEMBER_EXPORT_QUERY,
    MEMBER_EXPORT_PATH,
    MEMBER_GET_ONE_QUERY,
    MEMBER_GET_ALL_QUERY,
    MEMBER_ADD_QUERY,
    MEMBER_UPDATE_QUERY,
    MEMBER_DELETE_QUERY,
)
from models.MemberModel import MemberModel
from repository._repository_class import Repository
from utils.DBConnection import DBConnection


class MemberRepository(Repository):
    def __init__(self):
        self.database = DBConnection()
        self.database.execute(MEMBER_TABLE_QUERY)

    def import_data(self) -> str:
        csv_data = os.path.join(MEMBER_IMPORT_PATH)
        if os.path.exists(csv_data):
            with open(csv_data, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    self.database.execute(
                        MEMBER_IMPORT_QUERY,
                        (
                            row[0].strip(),
                            row[1].strip(),
                            row[2].strip(),
                            row[3].strip(),
                            row[4].strip(),
                            row[5].strip(),
                        ),
                    )
                return f"Data {len(row)} Imported Successfully"
        return f"Data File Not Found"

    def export_data(self):
        try:
            self.rows = self.database.execute(MEMBER_EXPORT_QUERY, fetch=True)
            if not self.rows:
                return "No Data to Export"
            with open(
                file=MEMBER_EXPORT_PATH, mode="w", newline="", encoding="utf-8"
            ) as f:
                self.writer = csv.writer(f)
                self.writer.writerows(self.rows)
            return f"Data {len(self.rows)} Exported Successfully"
        except Exception as e:
            return f"{str(e)}"

    def get_one(self, id: str):
        try:
            self.rows = self.database.execute(
                MEMBER_GET_ONE_QUERY, params=(id,), fetch=True
            )
            if not self.rows:
                return "Value Not Found!"
            self.response = self.rows[0]
            self.result = (
                self.response[0],
                self.response[1],
                self.response[2],
                self.response[3],
                self.response[4],
                self.response[5],
            )
            return self.result
        except Exception as e:
            return f"{str(e)}"

    def get_all(self):
        try:
            self.res = self.database.execute(
                query=MEMBER_GET_ALL_QUERY, params=(), fetch=True
            )
            return [r for r in self.res]
        except Exception as e:
            return f"{str(e)}"

    def add(self, member: MemberModel):
        if self.get_one(member.member_id):
            return "Member Already Exists."
        try:
            self.database.execute(
                MEMBER_ADD_QUERY,
                (
                    member.member_id,
                    member.member_name,
                    member.contact_no,
                    member.age,
                    member.membership_type,
                    member.membership_status,
                ),
            )
            return "Data Added Successfully"
        except Exception as e:
            return f"{str(e)}"

    def update(self, data: MemberModel):
        if not data.member_id:
            return "Values is missing!"
        try:
            self.database.execute(
                query=MEMBER_UPDATE_QUERY,
                params=(
                    data.member_id,
                    data.member_name,
                    data.contact_no,
                    data.age,
                    data.membership_type,
                    data.membership_status,
                ),
            )
            return "Data Updated Successfully!"
        except Exception as e:
            return f"{str(e)}"

    def delete(self, id: str):
        if not self.get_one(id):
            return "Member Not Found"
        try:
            self.database.execute(MEMBER_DELETE_QUERY, (id,))
            return f"Member Deleted Successfully!"
        except Exception as e:
            return f"{str(e)}"
