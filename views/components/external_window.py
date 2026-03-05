import tkinter as tk
from tkinter import ttk

from utils import BarCodeScanner
from views.components.buttons import ScanButton
from views.components.details import BookForm
from ..widgets import DetailRow


class ExternalWindow(tk.Toplevel):
    """
    A generic modal popup window.
    """

    def __init__(self, parent, title: str):
        super().__init__(parent)

        self.title(title)
        self.transient(parent)
        self.grab_set()
        self.focus_set()


class BookExternalModels(ExternalWindow):

    def __init__(self, parent):
        super().__init__(parent, "Add Book")

        self.columnconfigure(0, weight=1)
        self.book_add_model()

    def book_add_model(self):

        book_form = tk.Frame(self)
        book_form.pack(fill="both", padx=12, pady=12)

        DetailRow(book_form, field_name="isbn", label_text="ISBN").pack(
            fill="both", padx=12, pady=12
        )

        def handle_submit(data):
            print("Form Data:", data)

        form = BookForm(self, command=handle_submit)
        form.pack(fill="both", expand=True, padx=12, pady=12)

        # submit_btn = ttk.Button(
        #     book_form,
        #     text="Submit",
        #     padding=(8, 4),
        #     command=handle_submit,
        # )

        # submit_btn.pack(pady=(0, 10), padx=4)

        scanner = BarCodeScanner(
            out_path="books.csv",
            column_titles=[
                "ISBN",
                "Title",
                "Author",
                "Publisher",
                "Published",
                "Scanned At",
            ],
        )

        ScanButton(
            book_form, button_name="Scan Now!", func_name=scanner.start_scanner()
        ).pack(fill="both")
