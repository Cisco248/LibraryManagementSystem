from tkinter import messagebox, ttk
from utils.DBConnection import DBConnection
from views.components.WindowComponent import MemberWindow
from views.components import SearchComponent, ButtonToolBar, MemberListView


class MemberView(ttk.Frame):
    def __init__(self, parent: ttk.Notebook) -> None:
        super().__init__(parent)

        self.frame = ttk.Frame(parent)
        parent.add(self.frame, text="Member")
        self.tab_frame(self.frame)

    def tab_frame(self, Tab: ttk.Frame):

        def __add__():
            MemberWindow(self.frame, title="Addition Member to Library").add_event()

        def __delete__():
            MemberWindow(self.frame, title="Deletion Member in Library").delete_event()

        def __update__():
            MemberWindow(self.frame, title="Update Member in Library").update_event()

        def __clear__():
            try:
                db = DBConnection()
                db.execute("DELETE FROM members")
                return messagebox.showinfo(
                    title="Clear Members",
                    message="Are You Sure, You Want Clear Member List?",
                    detail=f'Press "OK" Delete the Member Data,  Press "Cancel" Discard Task',
                )
            except Exception as e:
                return messagebox.showerror("Error", str(e))

        SearchComponent(
            Tab,
            title="Search Member",
            button_text="Search",
            label_text="ID/Name: ",
            service=None,
        )

        ButtonToolBar(
            parent=Tab,
            title="Member Operations",
            on_add=__add__,
            on_delete=__delete__,
            on_update=__update__,
            on_clear=__clear__,
        )

        MemberListView().__view__(Tab)
