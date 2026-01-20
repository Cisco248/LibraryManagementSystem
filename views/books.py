from tkinter import ttk
import tkinter as tk
from .components import BookForm, SearchComponent, ButtonToolBar, BookListView
from utils import ExternalWindow


class BookView(ttk.Frame):
    """
    Manages the user interface for book operations.
    """

    def __init__(self, parent: ttk.Notebook) -> None:
        super().__init__(parent)

        self.frame = ttk.Frame(parent)
        parent.add(self.frame, text="Books")

        self._build_ui(self.frame)

    def _build_ui(self, container: ttk.Frame):

        def on_search(query: str):
            if len(query) < 3:
                print("Invalid search query")
            else:
                print(f"Searching: {query}")

        def open_add_book_modal():
            def on_submit(form_data):
                print("Book Added:", form_data)

            ExternalWindow(
                parent=container,
                title="Add New Book",
                content_class=BookForm,
                command=on_submit,
            )

        search_widget = SearchComponent(
            container,
            title="Search Books",
            button_text="Search",
            lable_text="Title / ISBN",
            command=on_search,
        )
        search_widget.pack(fill="x", padx=12, pady=12)

        button_tool = ButtonToolBar(
            container,
            on_add=open_add_book_modal,
            on_delete=lambda: print("Delete"),
            on_update=lambda: print("Update"),
            on_clear=lambda: print("Clear"),
        )
        button_tool.pack(fill="x", padx=12, pady=6)

        BookListView(container)
