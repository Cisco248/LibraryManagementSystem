import os
import csv
import requests
from config.Configuration import (
    BOOK_TABLE_QUERY,
    BOOK_IMPORT_PATH,
    BOOK_IMPORT_QUERY,
    BOOK_EXPORT_QUERY,
    BOOK_EXPORT_PATH,
    BOOK_GET_ONE_QUERY,
    BOOK_GET_ALL_QUERY,
    BOOK_ADD_QUERY,
    BOOK_UPDATE_QUERY,
    BOOK_DELETE_QUERY,
)
from models.BookModel import BookModel
from utils.DBConnection import DBConnection
from ._repository_class import API


class GoogleBookAPI(API):

    BASE_URL = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

    def fetch_data(self) -> dict:
        url = f"{self.BASE_URL}{self.isbn}"

        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()

    def get_book_info(self) -> dict:
        data = self.fetch_data()

        if "items" not in data:
            raise ValueError("Not found in Google Books")

        volume_info = data["items"][0]["volumeInfo"]

        return {
            "isbn": self.isbn,
            "title": volume_info.get("title", "Unknown"),
            "author": ", ".join(volume_info.get("authors", ["Unknown"])),
            "publisher": volume_info.get("publisher", "Unknown"),
            "publication_year": volume_info.get("publishedDate", "Unknown")[:4],
            "source": "Google Books",
        }


class OpenLibraryAPI(API):

    BASE_URL = "https://openlibrary.org/api/books?bibkeys=ISBN:"

    def fetch_data(self) -> dict:
        url = f"{self.BASE_URL}{self.isbn}&format=json&jscmd=data"

        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()

    def get_book_info(self) -> dict:
        data = self.fetch_data()

        key = f"ISBN:{self.isbn}"

        if key not in data:
            raise ValueError("Not found in Open Library")

        book = data[key]

        authors = (
            ", ".join([a["name"] for a in book.get("authors", [])])
            if book.get("authors")
            else "Unknown"
        )

        publishers = (
            ", ".join([p["name"] for p in book.get("publishers", [])])
            if book.get("publishers")
            else "Unknown"
        )

        publish_date = book.get("publish_date", "Unknown")
        year = (
            "".join(filter(str.isdigit, publish_date))[:4]
            if publish_date
            else "Unknown"
        )

        return {
            "isbn": self.isbn,
            "title": book.get("title", "Unknown"),
            "author": authors,
            "publisher": publishers,
            "publication_year": year,
            "source": "Open Library",
        }


class BookAPIFactory:

    @staticmethod
    def get_book_info(isbn: str) -> dict:

        providers = [
            GoogleBookAPI(isbn),
            OpenLibraryAPI(isbn),
        ]

        for provider in providers:
            try:
                return provider.get_book_info()
            except Exception:
                continue

        raise ValueError("Book not found in any provider.")


class BookRepository:
    def __init__(self):

        self.database = DBConnection()
        self.database.execute(query=BOOK_TABLE_QUERY)

    def import_data(self) -> str:
        self.csv = os.path.join(BOOK_IMPORT_PATH)
        if os.path.exists(self.csv):
            with open(self.csv, "r", encoding="utf-8") as f:
                self.reader = csv.reader(f)
                next(self.reader)
                for row in self.reader:
                    if not row:
                        return "No Data to Import"
                    self.database.execute(
                        BOOK_IMPORT_QUERY,
                        (
                            row[0].strip(),
                            row[1].strip(),
                            row[2].strip(),
                            row[3].strip(),
                            row[4].strip(),
                            row[5].strip(),
                            row[6].strip(),
                            row[7].strip(),
                            row[8].strip(),
                            row[9].strip(),
                            row[10].strip(),
                        ),
                    )
                return f"Data {len(row)} Imported Successfully"
        return "Data File Not Found!"

    def export_data(self) -> str:
        try:
            self.rows = self.database.execute(BOOK_EXPORT_QUERY, fetch=True)
            if not self.rows:
                return "No Data to Export"
            with open(
                file=BOOK_EXPORT_PATH, mode="w", newline="", encoding="utf-8"
            ) as f:
                self.writer = csv.writer(f)
                self.writer.writerows(self.rows)
            return f"Data {len(self.rows)} Exported Successfully"

        except Exception as e:
            return f"{str(e)}"

    def get_one(self, value: str):
        try:
            self.rows = self.database.execute(
                query=BOOK_GET_ONE_QUERY,
                params=(value,),
                fetch=True,
            )
            if not self.rows:
                return "Value Not Found."
            self.response = self.rows[0]
            self.result = (
                self.response[0],
                self.response[1],
                self.response[2],
                self.response[3],
                self.response[4],
                self.response[5],
                self.response[6],
                self.response[7],
                self.response[8],
                self.response[9],
                self.response[10],
            )
            return self.result
        except Exception as e:
            return f"{str(e)}"

    def get_all(self):
        try:
            self.res = self.database.execute(BOOK_GET_ALL_QUERY, fetch=True)
            return [r for r in self.res]
        except Exception as e:
            return f"{str(e)}"

    def add(self, data: BookModel):
        try:
            self.database.execute(
                BOOK_ADD_QUERY,
                BookModel(
                    isbn=data.isbn,
                    title=data.title,
                    author=data.author,
                    publisher=data.publisher,
                    category=data.category,
                    publication_year=data.publication_year,
                    book_type=data.book_type,
                    status=data.status,
                    file_format=data.file_format,
                    price=data.price,
                    ratings=data.ratings,
                ).to_tuple(),
            )
            return "Data Added Successfully!"
        except Exception as e:
            return f"{str(e)}"

    def update(self, data: BookModel):
        if not data.isbn:
            return "Values is missing!"
        try:
            self.database.execute(
                query=BOOK_UPDATE_QUERY,
                params=(
                    data.title,
                    data.author,
                    data.publisher,
                    data.category,
                    data.publication_year,
                    data.book_type.value,
                    data.status.value,
                    data.file_format.value,
                    data.price,
                    data.ratings,
                    data.isbn,
                ),
            )
            return "Data Updated Successfully!"
        except Exception as e:
            return f"{str(e)}"

    def delete(self, value: str):
        try:
            self.database.execute(BOOK_DELETE_QUERY, (value,))
            return "Data Deleted Successfully."
        except Exception as e:
            return f"{str(e)}"
