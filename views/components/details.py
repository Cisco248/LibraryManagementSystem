"""Book form component"""

from tkinter import ttk
import tkinter as tk
from ..widgets import DetailRow


class BookForm(tk.LabelFrame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, text="Book Details", padx=12, pady=12, **kwargs)

        self.columnconfigure(0, weight=1)

        self.build_form()

    def build_form(self):

        self.isbn_row = DetailRow(self, field_name="isbn", label_text="ISBN")
        self.isbn_row.pack(fill="x", pady=(10, 0))

        self.title_row = DetailRow(self, field_name="title", label_text="Title")
        self.title_row.pack(fill="x", pady=(10, 0))

        self.author_row = DetailRow(self, field_name="author", label_text="Author")
        self.author_row.pack(fill="x", pady=(10, 0))

        self.publisher_row = DetailRow(
            self, field_name="publisher", label_text="Publisher"
        )
        self.publisher_row.pack(fill="x", pady=(10, 0))

        self.year_row = DetailRow(self, field_name="year", label_text="Published Year")
        self.year_row.pack(fill="x", pady=(10, 0))

        submit_btn = ttk.Button(
            self, text="Submit", padding=(8, 4), command=self.on_submit
        )
        submit_btn.pack(pady=(10, 0))

    def on_submit(self) -> dict[str, str]:
        data = {
            "isbn": self.isbn_row.get_value(),
            "title": self.title_row.get_value(),
            "author": self.author_row.get_value(),
            "publisher": self.publisher_row.get_value(),
            "year": self.year_row.get_value(),
        }

        return data

    # Optional helper method
    def set_form_data(self, book_data: dict):
        self.isbn_row.set_value(book_data.get("isbn", ""))
        self.title_row.set_value(book_data.get("title", ""))
        self.author_row.set_value(book_data.get("author", ""))
        self.publisher_row.set_value(book_data.get("publisher", ""))
        self.year_row.set_value(book_data.get("publication_year", ""))
