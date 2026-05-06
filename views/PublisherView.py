from tkinter import messagebox, ttk
from config.Configuration import PUBLISHER_DASHBOARD_QUERY
from services.PublisherService import PublisherActionController
from views.components.DashBoard import Dashboard
from views.components.FormComponent import PublisherForm
from views.components import (
    PublisherSearchComponent,
    OtherButtonToolBar,
    PublisherListView,
)


class PublisherView(ttk.Frame):
    def __init__(self, parent: ttk.Notebook) -> None:
        super().__init__(parent)
        self.service = PublisherActionController()
        self.frame = ttk.Frame(parent)
        parent.add(self.frame, text="Publisher")

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
            query=PUBLISHER_DASHBOARD_QUERY,
            value_1="Total Publishers",
        )
        self.row_2 = PublisherSearchComponent(
            Tab,
            title="Search Publisher",
            button_text="Search",
            label_text="ID/Name: ",
            service=self.service,
        )
        self.row_3 = PublisherForm(Tab, title="Add Publisher to Library")
        self.row_4 = OtherButtonToolBar(
            parent=Tab,
            title="Publisher Operations",
            add_func=self._add_publishers,
            del_func=self._delete_publishers,
            update_func=self._update_publisher,
            clear_func=self.row_3.__clear__,
            import_func=self._import_publishers,
            export_func=self._export_publishers,
        )
        self.row_5 = PublisherListView(Tab, self.row_3)

    def __layout__(self):
        self.row_1.grid(row=0, column=0, padx=8, pady=8, sticky="ew")
        self.row_2.grid(row=1, column=0, padx=8, pady=8, sticky="ew")
        self.row_3.grid(row=2, column=0, padx=8, pady=8, sticky="ew")
        self.row_4.grid(row=3, column=0, padx=8, pady=8, sticky="ew")
        self.row_5.grid(row=4, rowspan=2, column=0, padx=8, pady=8, sticky="ew")

    def _import_publishers(self):
        self.service.handle_import()

    def _export_publishers(self):
        self.service.handle_export()

    def _add_publishers(self):
        data = self.row_3.__get__()
        if not data.publisher_id:
            return messagebox.showwarning(
                title="warning",
                message="Publisher ID is required!",
            )
        self.service.handle_add(data)

    def _delete_publishers(self):
        try:
            self.data = self.row_3.__get__()
            msg = messagebox.askyesno(
                title="question",
                message="Are You Sure, You Want To Delete This Publisher?",
                detail=f"ID: {self.data.publisher_id} Or Name: {self.data.publisher_name}",
            )
            if msg == True:
                return self.service.handle_delete(self.data.publisher_id)

            return messagebox.showinfo(
                title="Delete Publisher",
                message="Publisher Delete Unsuccessfully!",
                detail=f"You Discard Task.",
            )
        except Exception as e:
            return messagebox.showerror("Error", str(e))

    def _update_publisher(self):
        try:
            data = self.row_3.__get__()
            if not data.publisher_id:
                return messagebox.showerror(
                    title="Error",
                    message="Publisher ID is required!",
                )
            return self.service.handle_update(data)
        except Exception as e:
            return messagebox.showerror(title="Error", message=str(e))
