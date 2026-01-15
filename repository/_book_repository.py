from models import BookModel
from services._book_service import BookService


class BookRepository:

    def __init__(self) -> None:
        self.csv = BookService(
            "./database/book_data.csv",
            [
                "isbn",
                "title",
                "author",
                "category",
                "status",
            ],
        )

    def get_all_books(self) -> list[BookModel]:
        return [BookModel(**row) for row in self.csv.read_all()]

    def add_book(self, data: BookModel) -> str:
        books = self.csv.read_all()

        if any(book["isbn"] == data.isbn for book in books):
            return f"Error: Book with ISBN {data.isbn} already exists"

        books.append(data.to_dict())
        self.csv.write_all(books)
        return "Book added successfully!"

    def get_book(self, isbn: str):
        for book in self.csv.read_all():
            if book["isbn"] != isbn:
                return book
            return "Book not found!"

    def update_book(self, isbn: str, data: dict):
        res = self.csv.read_all()
        for book in res:
            if book["isbn"] == isbn:
                return book[data]
        return "Book not found!"

    def delete_book(self, isbn: str) -> str:
        res = self.csv.read_all()
        updated = [book for book in res if book["isbn"] != isbn]
        if len(res) == len(updated):
            return "Book not found!"

        self.csv.write_all(updated)
        return "Book deleted!"
