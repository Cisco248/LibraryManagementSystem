from tkinter import messagebox, ttk
from config.Configuration import AUTHOR_DASHBOARD_QUERY
from services.AuthorService import AuthorActionController
from utils.DBConnection import DBConnection
from views.components import AuthorSearchComponent, OtherButtonToolBar, AuthorListView
from views.components.DashBoard import Dashboard
from views.components.FormComponent import AuthorForm


class AuthorView(ttk.Frame):
    def __init__(self, parent: ttk.Notebook) -> None:
        super().__init__(parent)
        self.services = AuthorActionController()
        self.db = DBConnection()

        self.frame = ttk.Frame(parent)
        parent.add(self.frame, text="Author")

        for i in range(4):
            self.frame.rowconfigure(i)

        self.frame.rowconfigure(4, weight=1)
        self.frame.rowconfigure(5, weight=1)
        self.frame.columnconfigure(0, weight=1)

        self.__widget__(self.frame)
        self.__layout__()

    def __widget__(self, Tab: ttk.Frame):
        self.row_1 = Dashboard(
            Tab,
            query=AUTHOR_DASHBOARD_QUERY,
            value_1="Total Authors",
        )
        self.row_2 = AuthorSearchComponent(
            Tab,
            title="Search Author",
            button_text="Search",
            label_text="ID/Name: ",
            service=AuthorActionController(),
        )
        self.row_3 = AuthorForm(Tab, title="Add Author to Library")
        self.row_4 = OtherButtonToolBar(
            parent=Tab,
            title="Author Operations",
            add_func=self._add_authors,
            del_func=self._delete_authors,
            update_func=self._update_authors,
            clear_func=self.row_3.__clear__,
            import_func=self._import_authors,
            export_func=self._export_authors,
        )
        self.row_5 = AuthorListView(Tab, form=self.row_3)

    def __layout__(self):
        self.row_1.grid(row=0, column=0, padx=8, pady=8, sticky="ew")
        self.row_2.grid(row=1, column=0, padx=8, pady=8, sticky="ew")
        self.row_3.grid(row=2, column=0, padx=8, pady=8, sticky="ew")
        self.row_4.grid(row=3, column=0, padx=8, pady=8, sticky="ew")
        self.row_5.grid(row=4, rowspan=2, column=0, padx=8, pady=8, sticky="ew")

    def _import_authors(self):
        self.services.handle_import()

    def _export_authors(self):
        self.services.handle_export()

    def _add_authors(self):
        data = self.row_3.__get__()
        if not data.author_id:
            return messagebox.showwarning(
                title="warning",
                message="Author ID is required!",
            )
        return self.services.handle_add(data)

    def _delete_authors(self):
        try:
            self.data = self.row_3.__get__()
            msg = messagebox.askyesno(
                title="question",
                message="Are You Sure, You Want To Delete This Author?",
                detail=f"ID: {self.data.author_id} Or Name: {self.data.author_name}",
            )
            if msg == True:
                return self.services.handle_delete(self.data.author_id)

            return messagebox.showinfo(
                title="Delete Author",
                message="Author Delete Unsuccessfully!",
                detail=f"You Discard Task.",
            )
        except Exception as e:
            return messagebox.showerror("Error", str(e))

    def _update_authors(self):
        try:
            data = self.row_3.__get__()
            if not data.author_id:
                return messagebox.showerror(
                    title="Error",
                    message="Author ID is required!",
                )
            return self.services.handle_update(data)
        except Exception as e:
            return messagebox.showerror(title="Error", message=str(e))
