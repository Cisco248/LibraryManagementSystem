from tkinter import ttk
from tkinter import messagebox

from utils.DBConnection import DBConnection

from .components import (
    SearchComponent,
    ButtonToolBar,
    BookListView,
    BarrowBookListView,
    MiniButtonBar,
)

from .components import BookWindow


class BookView(ttk.Frame):
    def __init__(self, parent: ttk.Notebook) -> None:
        super().__init__(parent)

        self.frame = ttk.Frame(parent)
        parent.add(self.frame, text="Books")
        self.tab_frame(self.frame)

    def tab_frame(self, Tab: ttk.Frame):
        SearchComponent(
            Tab,
            title="Search Books",
            button_text="Search",
            lable_text="Title / ISBN",
            table="books",
            parameter1="isbn",
            parameter2="title",
        )

        def __add__():
            BookWindow(self.frame, "Add Book").add_event()

        def __delete__():
            BookWindow(self.frame, "Delete Book").delete_event()

        def __update__():
            BookWindow(self.frame, "Update Book").update_event()

        def __clear__():
            try:
                db = DBConnection()
                db.execute("DELETE FROM books")
                return messagebox.showinfo(
                    title="Clear Books",
                    message="Are You Sure, You Want Clear Book List?",
                    detail=f'Press "OK" Delete the Author Data, Press "Cancel" Discard Task',
                )
            except Exception as e:
                return messagebox.showerror("Error", str(e))

        ButtonToolBar(
            Tab,
            on_add=__add__,
            on_delete=__delete__,
            on_update=__update__,
            on_clear=__clear__,
        )

        BookListView(Tab)

        MiniButtonBar(Tab, "Reservation", "Return Back")

        BarrowBookListView(Tab)
