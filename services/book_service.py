import sys
from pathlib import Path
from tkinter import messagebox

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services._controller_class import Controller
from models._book_model import BookModel
from repository import BookRepository


class BookActionController(Controller):

    def __init__(self):
        self.repository = BookRepository()

    def handle_get_one(self, isbn: str):
        try:
            return self.repository.get_one(isbn)
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_get_all(self):
        try:
            return self.repository.get_all()
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_add(self, data: BookModel):
        try:
            res = self.repository.add(data)
            return messagebox.showinfo(
                "Book Added", f"Book '{res.title}' added successfully!"
            )
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_update(self, isbn: str, data: dict):
        if not isbn:
            return messagebox.showwarning(
                "Warning", "Error: ISBN is required for update"
            )
        try:
            book = self.repository.update(isbn, data)
            return messagebox.showinfo(
                "Book Updated", f"Book '{book.title}' updated successfully!"
            )
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_delete(self, isbn: str):
        if not isbn:
            return messagebox.showwarning(
                "Warning", "Error: ISBN is required for deletion"
            )
        try:
            self.repository.delete(isbn)
            return messagebox.showinfo(
                "Book Deleted", f"Book with ISBN '{isbn}' deleted successfully!"
            )
        except Exception as e:

            return messagebox.showerror("Error", f"{str(e)}")
