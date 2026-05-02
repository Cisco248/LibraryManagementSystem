import csv
import logging
import os
from tkinter import messagebox
from models.AuthorModel import AuthorModel
from repository._repository_class import Repository

# from config.configure import ARGS
from utils.DBConnection import DBConnection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AuthorRepository(Repository):

    def __init__(self):
        self.database = DBConnection()

        self.database.execute("""
                CREATE TABLE IF NOT EXISTS authors (
                    author_id TEXT PRIMARY KEY,
                    author_name TEXT,
                    address TEXT,
                    gov_reg_no TEXT,
                    agreement_time DATE
                )
                """)

        self.load_authors()

    def load_authors(self) -> str:
        author_csv = os.path.join("database", "author_data.csv")
        if os.path.exists(author_csv):
            with open(author_csv, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    self.database.execute(
                        """
                        INSERT OR IGNORE INTO authors (
                        author_id, author_name, address, gov_reg_no, agreement_time) 
                        VALUES (?, ?, ?, ?, ?);
                        """,
                        (
                            row[0].strip(),
                            row[1].strip(),
                            row[2].strip(),
                            row[3].strip(),
                            row[4].strip(),
                        ),
                    )
                return "Authors loaded successfully"
        return "Author data file not found."

    def get_one(self, id: str):
        try:

            rows = self.database.execute(
                "SELECT * FROM author WHERE author_id = %s", params=(id,), fetch=True
            )

            if not rows:
                return f"Author with ID '{id}' not found."

            res = rows[0]
            return AuthorModel(
                author_id=res.get("author_id", ""),
                author_name=res.get("author_name", ""),
                address=res.get("address", ""),
                gov_reg_no=res.get("gov_reg_no", ""),
                agreement_time=res.get("agreement_time", 0),
            )

        except Exception as e:
            return f"{str(e)}"

    def get_all(self):
        try:

            res = self.database.execute(
                query="SELECT * FROM authors", params=(), fetch=True
            )
            return [
                AuthorModel(
                    author_id=r[0],
                    author_name=r[1],
                    address=r[2],
                    gov_reg_no=r[3],
                    agreement_time=r[4],
                )
                for r in res
            ]
        except Exception as e:
            return f"Error retrieving all authors: {str(e)}"

    def add(self, author: AuthorModel):
        if self.get_one(author.author_id):
            return f"Author with ID '{author.author_id}' already exists."

        try:
            self.database.execute(
                "INSERT INTO author (author_id, author_name, address, gov_reg_no, agreement_time) VALUES (%s, %s, %s, %s, %s)",
                (
                    author.author_id,
                    author.author_name,
                    author.address,
                    author.gov_reg_no,
                    author.agreement_time,
                ),
            )
            return f"Author added successfully: {author.author_name}"

        except Exception as e:
            return f"{str(e)}"

    def update(self, id: str, updates: dict):
        if not updates:
            return "No updates provided."

        try:
            set_clause = ", ".join([f"{key} = %s" for key in updates.keys()])
            values = list(updates.values())
            values.append(id)

            self.database.execute(
                f"UPDATE authors SET {set_clause} WHERE author_id = %s", tuple(values)
            )
            return f"Author with ID '{id}' updated successfully."

        except Exception as e:
            return f"Failed to update author: {str(e)}"

    def delete(self, id: str) -> str:
        if not self.get_one(id):
            return f"Author with ID '{id}' not found."

        try:
            self.database.execute("DELETE FROM authors WHERE author_id = %s", (id,))
            return f"Author with ID '{id}' deleted successfully."

        except Exception as e:
            return f"{str(e)}"

    def search(self, **criteria):
        if not criteria:
            return "No search criteria provided."
        try:
            conditions = " AND ".join([f"{key} LIKE %s" for key in criteria.keys()])
            values = tuple(f"%{val}%" for val in criteria.values())

            res = self.database.execute(
                f"SELECT * FROM authors WHERE {conditions}", values, fetch=True
            )
            return [
                AuthorModel(
                    author_id=r.get("author_id", ""),
                    author_name=r.get("author_name", ""),
                    address=r.get("address", ""),
                    gov_reg_no=r.get("gov_reg_no", ""),
                    agreement_time=r.get("agreement_time", 0),
                )
                for r in res
            ]
        except Exception as e:
            return f"{str(e)}"
