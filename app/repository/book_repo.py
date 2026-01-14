from models import BookModel


class BookRepository:

    def __init__(self) -> None:
        self.books: list[dict] = []
        pass

    def add_book(self, data: BookModel) -> str | BookModel:

        if any(book["isbn"] == data.isbn for book in self.books):
            return f"Error: Book with ISBN {data.isbn} already exists"

        self.books.append(data.to_dict())
        return data

    def get_book(self, isbn: str) -> dict | None:
        for book in self.books:
            if book["isbn"] == isbn:
                return book

        return None

    def update_book(self, isbn: str, data: dict) -> str | dict:
        book = self.get_book(isbn)
        if not book:
            return f"Error: Book with ISBN {isbn} not found"

        book.update(data)
        return book

    def delete_book(self, **criteria) -> list[dict]:
        results = self.books
        for key, value in criteria.items():
            results = [
                b for b in results if str(value).lower() in str(b.get(key, "")).lower()
            ]
        return results

    def search_book(self, **criteria) -> list[dict]:
        results = self.books
        for key, val in criteria.items():
            if val:
                results = [
                    b
                    for b in results
                    if str(val).lower() in str(b.get(key, "")).lower()
                ]
        return results

    def get_all_books(self) -> list[dict]:
        return self.books.copy()
