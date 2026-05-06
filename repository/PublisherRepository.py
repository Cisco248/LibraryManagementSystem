import csv
import os
from config.Configuration import (
    PUBLISHER_TABLE_QUERY,
    PUBLISHER_IMPORT_PATH,
    PUBLISHER_IMPORT_QUERY,
    PUBLISHER_EXPORT_PATH,
    PUBLISHER_EXPORT_QUERY,
    PUBLISHER_GET_ONE_QUERY,
    PUBLISHER_GET_ALL_QUERY,
    PUBLISHER_ADD_QUERY,
    PUBLISHER_UPDATE_QUERY,
    PUBLISHER_DELETE_QUERY,
)
from models.PublisherModel import PublisherModel
from repository._repository_class import Repository
from utils.DBConnection import DBConnection


class PublisherRepository(Repository):
    def __init__(self):
        self.database = DBConnection()
        self.database.execute(PUBLISHER_TABLE_QUERY)

    def import_data(self):
        csv_file = os.path.join(PUBLISHER_IMPORT_PATH)
        if os.path.exists(csv_file):
            with open(csv_file, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    self.database.execute(
                        PUBLISHER_IMPORT_QUERY,
                        (
                            row[0].strip(),
                            row[1].strip(),
                            row[2].strip(),
                            row[3].strip(),
                            row[4].strip(),
                        ),
                    )
                return f"Publishers {len(row)} Imported Successfully"
        return f"Data File Not Found"

    def export_data(self):
        try:
            self.rows = self.database.execute(PUBLISHER_EXPORT_QUERY, fetch=True)
            if not self.rows:
                return "No Data to Export"
            with open(
                file=PUBLISHER_EXPORT_PATH, mode="w", newline="", encoding="utf-8"
            ) as f:
                self.writer = csv.writer(f)
                self.writer.writerows(self.rows)
            return f"Data {len(self.rows)} Exported Successfully"
        except Exception as e:
            return f"{str(e)}"

    def get_one(self, id: str):
        try:
            rows = self.database.execute(
                PUBLISHER_GET_ONE_QUERY, params=(id,), fetch=True
            )
            if not rows:
                return "Values not found"
            self.response = rows[0]
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
            res = self.database.execute(
                query=PUBLISHER_GET_ALL_QUERY, params=(), fetch=True
            )
            return [r for r in res]
        except Exception as e:
            return f"{str(e)}"

    def add(self, publisher: PublisherModel):
        if self.get_one(publisher.publisher_id):
            return f"Publisher Already Exists."
        try:
            self.database.execute(
                PUBLISHER_ADD_QUERY,
                (
                    publisher.publisher_id,
                    publisher.publisher_name,
                    publisher.address,
                    publisher.gov_reg_no,
                    publisher.agreement_time,
                ),
            )
            return f"Data Added Successfully"
        except Exception as e:
            return f"{str(e)}"

    def update(self, data: PublisherModel):
        if not data.publisher_id:
            return "Values is missing!"
        try:
            self.database.execute(
                query=PUBLISHER_UPDATE_QUERY,
                params=(
                    data.publisher_id,
                    data.publisher_name,
                    data.address,
                    data.gov_reg_no,
                    data.agreement_time,
                ),
            )
            return "Data Updated Successfully!"
        except Exception as e:
            return f"{str(e)}"

    def delete(self, id: str):
        if not self.get_one(id):
            return "Publisher Not Found."
        try:
            self.database.execute(PUBLISHER_DELETE_QUERY, (id,))
            return "Publisher Deleted Successfully"
        except Exception as e:
            return f"{str(e)}"
