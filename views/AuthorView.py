from tkinter import messagebox, ttk
from services.AuthorService import AuthorActionController
from utils.DBConnection import DBConnection
from views.components import SearchComponent, ButtonToolBar, AuthorListView


class AuthorView(ttk.Frame):
    def __init__(self, parent: ttk.Notebook):
        super().__init__(parent)
        self.services = AuthorActionController()
        self.db = DBConnection()

        self.frame = ttk.Frame(parent)
        parent.add(self.frame, text="Author")

        self.__widget__(self.frame)

    def __widget__(self, Tab: ttk.Frame):
        self.search_widget = SearchComponent(
            Tab,
            title="Search Author",
            button_text="Search",
            label_text="ID/Name: ",
            service=self.services,
        )
        self.button_tool = ButtonToolBar(parent=Tab, title="Author Operations")
        self.list = AuthorListView().__view__(Tab)

    def __layout__(self):
        self.search_widget.pack(fill="x", padx=12, pady=12)
        self.button_tool.pack(fill="x", padx=12, pady=6)
        # self.list.grid()
