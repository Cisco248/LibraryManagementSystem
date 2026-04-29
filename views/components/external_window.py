import tkinter as tk
from tkinter import ttk

from utils.barcode_scanner import BarCodeScanner
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

    def book_add_model(self) -> None:

        self.form_container = tk.Frame(self)
        self.form_container.pack(fill="both", padx=12, pady=12)

        self.bf = BookForm(self.form_container, command=None)
        self.bf.pack(fill="both", expand=True, padx=12, pady=12)

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
            self.form_container,
            button_name="Scan Now!",
            func_name=scanner.start_scanner,
        ).pack(fill="both")
