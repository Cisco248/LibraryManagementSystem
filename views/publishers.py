from tkinter import ttk
from views.components.external_window import ExternalWindow
from views.components import SearchComponent, BookForm, ButtonToolBar, PublisherListView


class PublisherView(ttk.Frame):
    """
    Manages the user interface for author operations.
    """

    def __init__(self, parent: ttk.Notebook) -> None:
        super().__init__(parent)

        self.frame = ttk.Frame(parent)
        parent.add(self.frame, text="Publisher")

        self._setup_tab(self.frame)

    def _setup_tab(self, parent: ttk.Frame):

        def _on_search(isbn):
            print(f"Searching for ISBN: {isbn}")
            if len(isbn) < 5:
                print("Error: Invalid ISBN")
            else:
                print("Success: Book found")

        def _open_add_book_modal():

            def on_popup_submit(form_instance):
                print(f"Add Component")

            ExternalWindow(
                parent=parent,
                title="Add New Book",
                content_class=BookForm,
                command=on_popup_submit,
            )
            print("Modal window opened...")

        def on_delete():
            print("Deleting Component")

        def on_update():
            print("Deleting Component")

        def on_clear():
            print("Deleting Component")

        search_widget = SearchComponent(
            parent,
            title="Search Publisher",
            button_text="Search",
            lable_text="Name: ",
            command=_on_search,
        )
        search_widget.pack(fill="x", padx=12, pady=12)

        button_tool = ButtonToolBar(
            parent,
            on_add=_open_add_book_modal,
            on_delete=on_delete,
            on_update=on_update,
            on_clear=on_clear,
        )
        button_tool.pack(fill="x", padx=12, pady=6)

        PublisherListView(parent)
