from tkinter import messagebox, ttk
from config.Configuration import MEMBER_DASHBOARD_QUERY
from services.MemberService import MemberActionController
from views.components.DashBoard import Dashboard
from views.components.FormComponent import MemberForm
from views.components import MemberSearchComponent, OtherButtonToolBar, MemberListView


class MemberView(ttk.Frame):
    def __init__(self, parent: ttk.Notebook) -> None:
        super().__init__(parent)
        self.service = MemberActionController()
        self.frame = ttk.Frame(parent)
        parent.add(self.frame, text="Member")

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
            query=MEMBER_DASHBOARD_QUERY,
            value_1="Total Members",
            value_2="Staff Members",
            value_3="Client Members",
            value_4="Bronze",
            value_5="Silver",
        )
        self.row_2 = MemberSearchComponent(
            Tab,
            title="Search Member",
            button_text="Search",
            label_text="ID/Name: ",
            service=self.service,
        )
        self.row_3 = MemberForm(Tab, "Add Member to Library")
        self.row_4 = OtherButtonToolBar(
            parent=Tab,
            title="Member Operations",
            add_func=self._add_member,
            del_func=self._delete_member,
            update_func=self._update_member,
            clear_func=self.row_3.__clear__,
            import_func=self._import_member,
            export_func=self._export_member,
        )
        self.row_5 = MemberListView(Tab, form=self.row_3)

    def __layout__(self):
        self.row_1.grid(row=0, column=0, padx=8, pady=8, sticky="ew")
        self.row_2.grid(row=1, column=0, padx=8, pady=8, sticky="ew")
        self.row_3.grid(row=2, column=0, padx=8, pady=8, sticky="ew")
        self.row_4.grid(row=3, column=0, padx=8, pady=8, sticky="ew")
        self.row_5.grid(row=4, rowspan=2, column=0, padx=8, pady=8, sticky="ew")

    def _import_member(self):
        self.service.handle_import()

    def _export_member(self):
        self.service.handle_export()

    def _add_member(self):
        data = self.row_3.__get__()
        if not data.member_id:
            return messagebox.showwarning(
                title="warning",
                message="Member ID is required!",
            )
        self.service.handle_add(data)

    def _delete_member(self):
        try:
            self.data = self.row_3.__get__()
            msg = messagebox.askyesno(
                title="question",
                message="Are You Sure, You Want To Delete This Member?",
                detail=f"ID: {self.data.member_id} Or Name: {self.data.member_name}",
            )
            if msg == True:
                return self.service.handle_delete(self.data.member_id)

            return messagebox.showinfo(
                title="Delete Member",
                message="Member Delete Unsuccessfully!",
                detail=f"You Discard Task.",
            )
        except Exception as e:
            return messagebox.showerror("Error", str(e))

    def _update_member(self):
        try:
            data = self.row_3.__get__()
            if not data.member_id:
                return messagebox.showerror(
                    title="Error",
                    message="Member ID is required!",
                )
            return self.service.handle_update(data)
        except Exception as e:
            return messagebox.showerror(title="Error", message=str(e))
