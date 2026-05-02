from tkinter import messagebox, ttk
from utils.DBConnection import DBConnection
from views.components.WindowComponent import AuthorWindow
from views.components import SearchComponent, ButtonToolBar, AuthorListView


class AuthorView(ttk.Frame):
    def __init__(self, parent: ttk.Notebook):
        super().__init__(parent)

        self.frame = ttk.Frame(parent)
        parent.add(self.frame, text="Author")
        self.tab_frame(self.frame)

    def tab_frame(self, Tab: ttk.Frame):

        def __add__():
            AuthorWindow(self.frame, title="Add Author to Library").add_event()

        def __delete__():
            AuthorWindow(self.frame, title="Delete Author in Library").delete_event()

        def __update__():
            AuthorWindow(self.frame, title="Update Author in Library").update_event()

        def __clear__():
            try:
                db = DBConnection()
                db.execute("DELETE FROM books")
                return messagebox.showinfo(
                    title="Clear Authors",
                    message="Are You Sure, You Want Clear Author List?",
                    detail=f'Press "OK" Delete the Author Data,  Press "Cancel" Discard Task',
                )
            except Exception as e:
                return messagebox.showerror("Error", str(e))

        self.search_widget = SearchComponent(
            Tab,
            title="Search Author",
            button_text="Search",
            lable_text="ID/Name: ",
            table="authors",
            parameter1="author_id",
            parameter2="author_name",
        )
        self.search_widget.pack(fill="x", padx=12, pady=12)

        button_tool = ButtonToolBar(
            Tab,
            on_add=__add__,
            on_delete=__delete__,
            on_update=__update__,
            on_clear=__clear__,
        )
        button_tool.pack(fill="x", padx=12, pady=6)

        AuthorListView(Tab)
