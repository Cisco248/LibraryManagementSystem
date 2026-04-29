import requests
import os
import csv
from models._book_model import BookModel
from utils.db_connection import DBConnection
from ._repository_class import API, Repository


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


class BookRepository(Repository):

    def __init__(self):
        self.database = DBConnection()

        self.database.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    isbn TEXT PRIMARY KEY,
                    title TEXT,
                    author TEXT,
                    publisher TEXT,
                    publication_year INTEGER,
                    book_type TEXT,
                    status TEXT,
                    file_format TEXT,
                    file_size TEXT
                )
                """)

        self.load_books()

    def load_books(self):
        book_csv = os.path.join("database", "book_data.csv")
        if os.path.exists(book_csv):
            with open(book_csv, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:

                    self.database.execute(
                        """
                            INSERT OR IGNORE INTO books (isbn, title, author, publisher, publication_year, book_type, status, file_format, file_size) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
                            """,
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
                        ),
                    )
                return "Books loaded successfully"
        else:
            return "Book data file not found"

    def get_one(self, isbn: str):
        try:
            rows = self.database.execute(
                "SELECT * FROM books WHERE isbn = ?", params=(isbn,), fetch=True
            )

            if not rows:
                return f"Book with ISBN '{isbn}' not found."

            res = rows[0]
            return BookModel(
                isbn=res["isbn"],
                title=res["title"],
                author=res["author"],
                publisher=res["publisher"],
                publication_year=res["publication_year"],
                book_type=res["book_type"],
                status=res["status"],
                file_format=res["file_format"],
                file_size=res["file_size"],
            )

        except Exception as e:
            return f"{str(e)}"

    def get_all(self):
        try:
            res = self.database.execute("SELECT * FROM books", fetch=True)
            return [
                BookModel(
                    isbn=r[0],
                    title=r[1],
                    author=r[2],
                    publisher=r[3],
                    publication_year=r[4],
                    book_type=r[5],
                    status=r[6],
                    file_format=r[7],
                    file_size=r[8],
                )
                for r in res
            ]
        except Exception as e:
            return f"{str(e)}"

    def add(self, data: BookModel):
        try:
            self.database.execute(
                "INSERT INTO books (isbn, title, author, publisher, publication_year, book_type, status, file_format, file_size) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                data.to_tuple(),
            )
            return f"Book Added Successfully --> ISBN: {data.isbn}"
        except Exception as e:
            return f"{str(e)}"

    def update(self, isbn: str, updates: dict):
        if not updates:
            return f"Warning: Update details are missing!"

        try:
            set_clause = ", ".join([f"{key} = ?" for key in updates.keys()])
            values = list(updates.values())
            values.append(isbn)

            self.database.execute(
                f"UPDATE books SET {set_clause} WHERE isbn = ?", tuple(values)
            )
            return f"Book with ISBN '{isbn}' updated successfully."
        except Exception as e:
            return f"{str(e)}"

    def delete(self, isbn: str):
        try:
            self.database.execute("DELETE FROM books WHERE isbn = ?", (isbn,))
            return f"Book with ISBN '{isbn}' deleted successfully."
        except Exception as e:
            return f"{str(e)}"

    def search(self, **data):
        if not data:
            return f"No search criteria provided."
        try:
            conditions = " AND ".join([f"{key} LIKE ?" for key in data.keys()])
            values = tuple(f"%{val}%" for val in data.values())

            res = self.database.execute(
                f"SELECT * FROM books WHERE {conditions}", values, fetch=True
            )
            return [
                BookModel(
                    isbn=r["isbn"],
                    title=r["title"],
                    author=r["author"],
                    publisher=r["publisher"],
                    publication_year=r["publication_year"],
                    book_type=r["book_type"],
                    status=r["status"],
                    file_format=r["file_format"],
                    file_size=r["file_size"],
                )
                for r in res
            ]
        except Exception as e:
            return f"{str(e)}"
