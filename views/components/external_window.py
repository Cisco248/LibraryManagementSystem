import tkinter as tk
from tkinter import ttk
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

        DetailRow(book_form, field_name="isbn", label_text="ISBN")

        def on_submit():
            print("hello")

        submit_btn = ttk.Button(
            book_form,
            text="Submit",
            padding=(8, 4),
            command=on_submit,
        )
        
        submit_btn.pack(pady=(0, 10), padx=4)

        return book_form
