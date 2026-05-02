import csv
import logging
import os
from tkinter import messagebox
from models.MemberModel import MemberModel
from repository._repository_class import Repository
from utils.DBConnection import DBConnection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MemberRepository(Repository):

    def __init__(self):
        self.database = DBConnection()

        self.database.execute("""
            CREATE TABLE IF NOT EXISTS members 
            ( member_id TEXT PRIMARY KEY, member_name TEXT, contact_no TEXT, age INTEGER, membership_type TEXT, membership_status TEXT );
            """)

        self.load_members()

    def load_members(self) -> str:
        member_csv = os.path.join("database", "member_data.csv")
        if os.path.exists(member_csv):
            with open(member_csv, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    self.database.execute(
                        """
                        INSERT OR IGNORE INTO members (
                        member_id, member_name, contact_no, age, membership_type, membership_status) 
                        VALUES (?, ?, ?, ?, ?, ?);
                        """,
                        (
                            row[0].strip(),
                            row[1].strip(),
                            row[2].strip(),
                            row[3].strip(),
                            row[4].strip(),
                            row[5].strip(),
                        ),
                    )
                return "Members loaded successfully"
        return f"Member data file not found at {member_csv}"

    def get_one(self, id: str):
        try:
            rows = self.database.execute(
                "SELECT * FROM member WHERE member_id = %s", params=(id,), fetch=True
            )

            if not rows:
                return "Member doesn't exists!"

            res = rows[0]
            return MemberModel(
                member_id=res.get("member_id", ""),
                member_name=res.get("name", ""),
                contact_no=res.get("email", ""),
                age=res.get("phone", ""),
                membership_type=res.get("membership_date", ""),
                membership_status=res.get("status", "active"),
            )
        except Exception as e:
            return f"{str(e)}"

    def get_all(self):
        try:
            res = self.database.execute(
                query="SELECT * FROM members", params=(), fetch=True
            )
            return [
                MemberModel(
                    member_id=r[0],
                    member_name=r[1],
                    contact_no=r[2],
                    age=r[3],
                    membership_type=r[4],
                    membership_status=r[5],
                )
                for r in res
            ]
        except Exception as e:
            return f"{str(e)}"

    def add(self, member: MemberModel):
        if self.get_one(member.member_id):
            return "Member with ID '{member.member_id}' already exists."

        try:
            self.database.execute(
                "INSERT INTO members (member_id, member_name, contact_no, age, membership_type, membership_status) VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    member.member_id,
                    member.member_name,
                    member.contact_no,
                    member.age,
                    member.membership_type,
                    member.membership_status,
                ),
            )
            return "Member added successfully"
        except Exception as e:
            return f"{str(e)}"

    def update(self, id: str, updates: dict):
        if not updates:
            return "Update details are missing!"

        try:
            set_clause = ", ".join([f"{key} = %s" for key in updates.keys()])
            values = list(updates.values())
            values.append(id)

            self.database.execute(
                f"UPDATE member SET {set_clause} WHERE member_id = %s", tuple(values)
            )
            return f"Member with ID: {id} updated successfully!"
        except Exception as e:
            return f"{str(e)}"

    def delete(self, id: str):
        if not self.get_one(id):
            return "Member with ID '{id}' not found."

        try:
            self.database.execute("DELETE FROM member WHERE member_id = %s", (id,))
            return f"Member with ID: {id} deleted successfully!"
        except Exception as e:
            return f"{str(e)}"

    def search(self, **criteria):
        if not criteria:
            return "No search criteria provided."
        try:
            conditions = " AND ".join([f"{key} LIKE %s" for key in criteria.keys()])
            values = tuple(f"%{val}%" for val in criteria.values())

            res = self.database.execute(
                f"SELECT * FROM member WHERE {conditions}", values, fetch=True
            )
            return [
                MemberModel(
                    member_id=r.get("member_id", ""),
                    member_name=r.get("name", ""),
                    contact_no=r.get("email", ""),
                    age=r.get("phone", ""),
                    membership_type=r.get("membership_date", ""),
                    membership_status=r.get("status", "active"),
                )
                for r in res
            ]
        except Exception as e:
            return f"{str(e)}"
