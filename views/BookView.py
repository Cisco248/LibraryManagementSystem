from tkinter import messagebox, ttk

from services.BookService import BookActionController
from utils.DBConnection import DBConnection
from views.components import SearchComponent
from views.components.DashBoard import Dashboard
from views.components.FormComponent import BookForm
from views.components.ListViewComponents import BookListView
from views.components.ToolBarComponent import ButtonToolBar


class BookView(ttk.Frame):
    def __init__(self, parent: ttk.Notebook) -> None:
        super().__init__(parent)
        self.services = BookActionController()
        self.db = DBConnection()

        self.frame = ttk.Frame(parent)
        parent.add(self.frame, text="Books")

        for i in range(5):
            self.frame.rowconfigure(i)

        self.frame.rowconfigure(5)
        self.frame.columnconfigure(0, weight=1)

        self.__widget__(self.frame)
        self.__layout__()

    def __widget__(self, Tab: ttk.Frame):
        self.dashboard = Dashboard(Tab)
        self.search_component = SearchComponent(
            Tab,
            title="Search Books",
            button_text="Search",
            label_text="Title/ISBN",
            service=self.services,
        )
        self.bf = BookForm(Tab, title="Book Form")
        self.buttonbar = ButtonToolBar(
            parent=Tab,
            title="Book Operations",
            add_func=self._add_book,
            del_func=self._delete_book,
            update_func=self._update_book,
            clear_func=self.bf.__clear__,
            import_func=self._import_books,
            export_func=self.services.handle_export,
        )
        self.list = BookListView(Tab, form=self.bf)

    def __layout__(self):
        self.dashboard.grid(row=0, column=0, sticky="ew", padx=8, pady=4)
        self.search_component.grid(row=1, column=0, sticky="ew", padx=8, pady=4)
        self.bf.grid(row=2, column=0, sticky="ew", padx=8, pady=4)
        self.buttonbar.grid(row=3, column=0, sticky="ew", padx=8, pady=4)
        self.list.grid(row=4, column=0, sticky="nsew", padx=8)

    def _import_books(self):
        self.services.handle_import()

    def _export_books(self):
        self.services.handle_export()

    def _add_book(self):

        data = self.bf.__get__()
        if not data.isbn:
            return messagebox.showwarning(
                title="Error",
                message="ISBN are required!",
            )

        return self.services.handle_add(data)

    def _delete_book(self):
        try:
            self.data = self.bf.__get__()

            msg = messagebox.askyesno(
                title="question",
                message="Are You Sure, You Want To Delete This Book?",
                detail=f"ISBN: {self.data.isbn} Or Title: {self.data.title}",
            )

            if msg == True:
                return self.services.handle_delete(self.data.isbn)

            return messagebox.showinfo(
                title="Delete Book",
                message="Book Delete Unsuccessfully!",
                detail=f"You Discard Task.",
            )

        except Exception as e:
            return messagebox.showerror("Error", str(e))

    def _update_book(self):
        try:
            data = self.bf.__get__()
            if not data.isbn:
                return messagebox.showerror(
                    title="Error",
                    message="ISBN is required!",
                )
            return self.services.handle_update(data)
        except Exception as e:
            return messagebox.showerror(title="Error", message=str(e))
