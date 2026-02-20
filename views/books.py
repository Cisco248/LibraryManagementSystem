from tkinter import ttk
from .components import SearchComponent, ButtonToolBar, BookListView
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
            bem = BookExternalModels(container)
            bem.book_add_model()

        def open_delete_book_model():
            pass

        def open_update_book_model():
            pass

        def open_clear_book_model():
            pass

        ButtonToolBar(
            container,
            on_add=open_add_book_modal,
            on_delete=open_delete_book_model,
            on_update=open_update_book_model,
            on_clear=open_clear_book_model,
        )

        BookListView(container)
