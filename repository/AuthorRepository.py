import csv
import os
from config.Configuration import (
    AUTHOR_TABLE_QUERY,
    AUTHOR_IMPORT_QUERY,
    AUTHOR_IMPORT_PATH,
    AUTHOR_UPDATE_QUERY,
    AUTHOR_GET_ONE_QUERY,
    AUTHOR_GET_ALL_QUERY,
    AUTHOR_ADD_QUERY,
    AUTHOR_DELETE_QUERY,
    AUTHOR_EXPORT_QUERY,
    AUTHOR_EXPORT_PATH,
)
from models.AuthorModel import AuthorModel
from repository._repository_class import Repository
from utils.DBConnection import DBConnection


class AuthorRepository(Repository):

    def __init__(self):
        self.database = DBConnection()

        self.database.execute(AUTHOR_TABLE_QUERY)

    def import_data(self):
        author_csv = os.path.join(AUTHOR_IMPORT_PATH)
        if os.path.exists(author_csv):
            with open(author_csv, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    self.database.execute(
                        AUTHOR_IMPORT_QUERY,
                        (
                            row[0].strip(),
                            row[1].strip(),
                            row[2].strip(),
                            row[3].strip(),
                            row[4].strip(),
                        ),
                    )
                return f"Data {len(row)} Imported Successfully"
        return "Data File Not Found."

    def export_data(self):
        try:
            self.rows = self.database.execute(AUTHOR_EXPORT_QUERY, fetch=True)
            if not self.rows:
                return "No Data to Export"
            with open(
                file=AUTHOR_EXPORT_PATH, mode="w", newline="", encoding="utf-8"
            ) as f:
                self.writer = csv.writer(f)
                self.writer.writerows(self.rows)
            return f"Data {len(self.rows)} Exported Successfully"

        except Exception as e:
            return f"{str(e)}"

    def get_one(self, id: str):
        try:
            self.rows = self.database.execute(
                AUTHOR_GET_ONE_QUERY, params=(id,), fetch=True
            )
            if not self.rows:
                return f"Value Not Found."
            self.response = self.rows[0]
            self.result = (
                self.response[0],
                self.response[1],
                self.response[2],
                self.response[3],
                self.response[4],
            )
            return self.result

        except Exception as e:
            return f"{str(e)}"

    def get_all(self):
        try:
            self.res = self.database.execute(
                query=AUTHOR_GET_ALL_QUERY, params=(), fetch=True
            )
            return [r for r in self.res]
        except Exception as e:
            return f"{str(e)}"

    def add(self, author: AuthorModel):
        if self.get_one(author.author_id):
            return f"Author Already Exists."
        try:
            self.database.execute(
                AUTHOR_ADD_QUERY,
                (
                    author.author_id,
                    author.author_name,
                    author.address,
                    author.gov_reg_no,
                    author.agreement_time,
                ),
            )
            return f"Author Added Successfully"
        except Exception as e:
            return f"{str(e)}"

    def update(self, data: AuthorModel):
        if not data.author_id:
            return "Values is missing!"
        try:
            self.database.execute(
                query=AUTHOR_UPDATE_QUERY,
                params=(
                    data.author_id,
                    data.author_name,
                    data.address,
                    data.gov_reg_no,
                    data.agreement_time,
                ),
            )
            return "Data Updated Successfully!"
        except Exception as e:
            return f"{str(e)}"

    def delete(self, id: str) -> str:
        if not self.get_one(id):
            return f"Author Not Found."
        try:
            self.database.execute(AUTHOR_DELETE_QUERY, (id,))
            return f"Author Deleted Successfully."
        except Exception as e:
            return f"{str(e)}"
