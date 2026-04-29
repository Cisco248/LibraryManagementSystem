from tkinter import ttk
from views.components.external_window import ExternalWindow
from views.components import SearchComponent, ButtonToolBar, BookForm, MemberListView


class MemberView(ttk.Frame):
    """
    Manages the user interface for members operations.
    """

    def __init__(self, parent: ttk.Notebook) -> None:
        super().__init__(parent)

        self.frame = ttk.Frame(parent)
        parent.add(self.frame, text="Member")

        self._setup_tab(self.frame)

    def _setup_tab(self, parent_container: ttk.Frame):
        def on_search(isbn):
            print(f"Searching for ISBN: {isbn}")
            if len(isbn) < 5:
                print("Error: Invalid ISBN")
            else:
                print("Success: Book found")

        def open_add_book_modal():

            def on_popup_submit(form_instance):
                print(f"Add Component")

            ExternalWindow(
                parent=parent_container,
                title="Add New Book",
                content_class=BookForm,
                command=on_popup_submit,
            )
            print("Modal window opened...")

        search_widget = SearchComponent(
            parent_container,
            title="Search Member",
            button_text="Search",
            lable_text="Name: ",
            command=on_search,
        )
        search_widget.pack(fill="x", padx=12, pady=12)

        button_tool = ButtonToolBar(
            parent_container,
            on_add=open_add_book_modal,
            on_delete=lambda: print("Delete"),
            on_update=lambda: print("Update"),
            on_clear=lambda: print("Clear"),
        )
        button_tool.pack(fill="both", padx=12, pady=6)

        MemberListView(parent_container)
