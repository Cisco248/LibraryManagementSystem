import requests
from abc import ABC, abstractmethod


class BookAPI(ABC):

    def __init__(self, isbn: str):
        self.isbn = isbn

    @abstractmethod
    def get_book_info(self) -> dict:
        pass


class GoogleBookAPI(BookAPI):

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


class OpenLibraryAPI(BookAPI):

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
