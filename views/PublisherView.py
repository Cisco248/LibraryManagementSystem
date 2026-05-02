from tkinter import messagebox, ttk
from utils.DBConnection import DBConnection
from views.components.WindowComponent import PublisherWindow
from views.components import SearchComponent, ButtonToolBar, PublisherListView


class PublisherView(ttk.Frame):
    def __init__(self, parent: ttk.Notebook) -> None:
        super().__init__(parent)

        self.frame = ttk.Frame(parent)
        parent.add(self.frame, text="Publisher")
        self.tab_frame(self.frame)

    def tab_frame(self, Tab: ttk.Frame):

        def __add__():
            PublisherWindow(
                self.frame, title="Addition Publisher to Library"
            ).add_event()

        def __delete__():
            PublisherWindow(
                self.frame, title="Deletion Publisher in Library"
            ).delete_event()

        def __update__():
            PublisherWindow(
                self.frame, title="Update Publisher in Library"
            ).update_event()

        def __clear__():
            try:
                db = DBConnection()
                db.execute("DELETE FROM books")
                return messagebox.showinfo(
                    title="Clear Publishers",
                    message="Are You Sure, You Want Clear Publisher List?",
                    detail=f'Press "OK" Delete the Publisher Data,  Press "Cancel" Discard Task',
                )
            except Exception as e:
                return messagebox.showerror("Error", str(e))

        SearchComponent(
            Tab,
            title="Search Publisher",
            button_text="Search",
            lable_text="ID/Name: ",
            table="publishers",
            parameter1="publisher_id",
            parameter2="publisher_name",
        )

        ButtonToolBar(
            Tab,
            on_add=__add__,
            on_delete=__delete__,
            on_update=__update__,
            on_clear=__clear__,
        )

        PublisherListView(Tab)
