import csv
import logging
import os
from tkinter import messagebox
from models.PublisherModel import PublisherModel
from repository._repository_class import Repository
from utils.DBConnection import DBConnection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PublisherRepository(Repository):

    def __init__(self):
        self.database = DBConnection()

        self.database.execute("""
            CREATE TABLE IF NOT EXISTS publishers 
            ( publisher_id TEXT PRIMARY KEY, publisher_name TEXT, address TEXT, gov_reg_no TEXT, agreement_time TEXT );
            """)

    #     self.load_publishers()

    # def load_publishers(self):
    #     publisher_csv = os.path.join("database", "publisher_data.csv")
    #     if os.path.exists(publisher_csv):
    #         with open(publisher_csv, "r", encoding="utf-8") as f:
    #             reader = csv.reader(f)
    #             next(reader)
    #             for row in reader:
    #                 self.database.execute(
    #                     """
    #                     INSERT OR IGNORE INTO publishers (
    #                     publisher_id, publisher_name, address, gov_reg_no, agreement_time)
    #                     VALUES (?, ?, ?, ?, ?);
    #                     """,
    #                     (
    #                         row[0].strip(),
    #                         row[1].strip(),
    #                         row[2].strip(),
    #                         row[3].strip(),
    #                         row[4].strip(),
    #                     ),
    #                 )
    #             return "Publishers loaded successfully"
    #     return f"Publisher CSV file not found at {publisher_csv}"

    def get_one(self, id: str):
        try:
            rows = self.database.execute(
                "SELECT * FROM publisher WHERE publisher_id = %s",
                params=(id,),
                fetch=True,
            )
            if not rows:
                return "Publisher not found"
            res = rows[0]
            return PublisherModel(
                publisher_id=res.get("publisher_id", ""),
                publisher_name=res.get("publisher_name", ""),
                address=res.get("address", ""),
                gov_reg_no=res.get("gov_reg_no", ""),
                agreement_time=res.get("agreement_time", ""),
            )
        except Exception as e:
            return f"{str(e)}"

    def get_all(self):

        try:
            res = self.database.execute(
                query="SELECT * FROM publishers", params=(), fetch=True
            )
            return [
                PublisherModel(
                    publisher_id=r[0],
                    publisher_name=r[1],
                    address=r[2],
                    gov_reg_no=r[3],
                    agreement_time=r[4],
                )
                for r in res
            ]
        except Exception as e:
            return f"{str(e)}"

    def add(self, publisher: PublisherModel):
        if self.get_one(publisher.publisher_id):
            return f"Publisher with ID '{publisher.publisher_id}' already exists."

        try:
            self.database.execute(
                "INSERT INTO publisher (publisher_id, publisher_name, address, gov_reg_no, agreement_time) VALUES (%s, %s, %s, %s, %s)",
                (
                    publisher.publisher_id,
                    publisher.publisher_name,
                    publisher.address,
                    publisher.gov_reg_no,
                    publisher.agreement_time,
                ),
            )
            return f"Publisher with ID: {publisher.publisher_id} added successfully"
        except Exception as e:
            return f"Error adding publisher: {str(e)}"

    def update(self, id: str, updates: dict):
        if not updates:
            return self.get_one(id)

        try:
            set_clause = ", ".join([f"{key} = %s" for key in updates.keys()])
            values = list(updates.values())
            values.append(id)

            self.database.execute(
                f"UPDATE publisher SET {set_clause} WHERE publisher_id = %s",
                tuple(values),
            )
            return f"Publisher with ID: {id} updated successfully"
        except Exception as e:
            return f"{str(e)}"

    def delete(self, id: str):
        if not self.get_one(id):
            return f"Publisher with ID '{id}' not found."

        try:
            self.database.execute(
                "DELETE FROM publisher WHERE publisher_id = %s", (id,)
            )
            return f"Publisher with ID: {id} deleted successfully"
        except Exception as e:
            return f"{str(e)}"

    def search(self, **criteria):
        if not criteria:
            return f"At least one search criterion must be provided."
        try:
            conditions = " AND ".join([f"{key} LIKE %s" for key in criteria.keys()])
            values = tuple(f"%{val}%" for val in criteria.values())

            res = self.database.execute(
                f"SELECT * FROM publisher WHERE {conditions}", values, fetch=True
            )
            return [
                PublisherModel(
                    publisher_id=r[0],
                    publisher_name=r[1],
                    address=r[2],
                    gov_reg_no=r[3],
                    agreement_time=r[4],
                )
                for r in res
            ]
        except Exception as e:
            return f"{str(e)}"
