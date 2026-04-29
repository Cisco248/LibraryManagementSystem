from tkinter import ttk
from .components import (
    SearchComponent,
    ButtonToolBar,
    BookListView,
    BarrowBookListView,
    MiniButtonBar,
)
from .components import BookExternalModels


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

        SearchComponent(
            container,
            title="Search Books",
            button_text="Search",
            lable_text="Title / ISBN",
            command=on_search,
        )

        def open_add_book_modal():
            BookExternalModels(container)

        def open_delete_book_model():
            from tkinter import messagebox
            messagebox.showinfo("Info", "Delete book feature coming soon!")

        def open_update_book_model():
            from tkinter import messagebox
            messagebox.showinfo("Info", "Update book feature coming soon!")

        def open_clear_book_model():
            from tkinter import messagebox
            messagebox.showinfo("Info", "Clear feature coming soon!")

        ButtonToolBar(
            container,
            on_add=open_add_book_modal,
            on_delete=open_delete_book_model,
            on_update=open_update_book_model,
            on_clear=open_clear_book_model,
        )

        BookListView(container)

        MiniButtonBar(container, "Reservation", "Return Back")

        BarrowBookListView(container)
