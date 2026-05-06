import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from config.Configuration import COLUMN_TITLES
from utils.DBConnection import DBConnection
from utils.BarcodeScanner import BarCodeScanner
from views.components.ListViewComponents import BookListView
from views.components.ToolBarComponent import ScanButton
from views.components.FormComponent import (
    BookForm,
    AuthorForm,
    PublisherForm,
    MemberForm,
)
from views.widgets.FormEntry import FormEntry


class WindowClass(tk.Toplevel):
    def __init__(self, parent, title: str):
        super().__init__(parent)
        self.title(title)
        self.transient(parent)


class BookWindow(WindowClass):
    def __init__(self, parent, title: str):
        super().__init__(parent, title)
        self.columnconfigure(0, weight=1)
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", padx=12, pady=12)

    def add_event(self):
        pass

    def delete_event(self):
        pass
        # self.isbn = FormEntry(
        #     self.container,
        #     direction="horizontal",
        #     name="isbn",
        #     label="ISBN",
        #     type="entry",
        # )
        # self.isbn.pack(fill="both", pady=12)

        # ttk.Separator(self.container, orient="horizontal").pack(
        #     fill="x", padx=12, pady=12
        # )

        # self.title = FormEntry(
        #     self.container,
        #     direction="horizontal",
        #     name="title",
        #     label="Title",
        #     type="entry",
        # )
        # self.title.pack(fill="both", pady=12)

        # def on_submit():

        # ttk.Button(self, text="Submit", padding=(8, 4), command=on_submit).pack(
        #     pady=(10, 0)
        # )

    def update_event(self):
        pass
        # def on_submit():

        # self.bf = BookForm(self.container, command=on_submit, title="")
        # self.bf.pack(fill="both", expand=True, padx=12, pady=12)


class AuthorWindow(WindowClass):
    def __init__(self, parent, title: str):
        super().__init__(parent, title)
        self.columnconfigure(0, weight=1)
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", padx=12, pady=12)

    def add_event(self):
        def on_submit():
            try:
                db = DBConnection()
                if (
                    not self.af.id.__get__()
                    or not self.af.name.__get__()
                    or not self.af.address.__get__()
                    or not self.af.gov_reg_no.__get__()
                    or not self.af.agree_time.__get__()
                ):
                    return messagebox.showerror("Error", "All fields are required!")

                db.execute(
                    """
                        INSERT INTO authors (author_id, author_name, address, gov_reg_no, agreement_time) 
                        VALUES (?, ?, ?, ?, ?)
                        """,
                    (
                        self.af.id.__get__(),
                        self.af.name.__get__(),
                        self.af.address.__get__(),
                        self.af.gov_reg_no.__get__(),
                        self.af.agree_time.__get__(),
                    ),
                )

                return messagebox.showinfo(
                    "Author Data",
                    message="Author Added Successfully!",
                    detail=f"""
                    ID: {self.af.id.__get__()}\n
                    Name: {self.af.name.__get__()}\n
                    Address: {self.af.address.__get__()}\n
                    Government Registration Number: {self.af.gov_reg_no.__get__()}\n
                    Agreement Time: {self.af.agree_time.__get__()}
                    """,
                    icon="info",
                )

            except Exception as e:
                return messagebox.showerror("Error", f"{str(e)}")

        self.af = AuthorForm(self.container, command=on_submit)
        self.af.pack(fill="both", expand=True, padx=12, pady=12)

    def delete_event(self):
        self.id = FormEntry(
            self.container,
            direction="horizontal",
            name="author_id",
            label="Author_ID",
            type="entry",
        )
        self.id.pack(fill="both", pady=12)

        ttk.Separator(self.container, orient="horizontal").pack(
            fill="x", padx=12, pady=12
        )

        self.name = FormEntry(
            self.container,
            direction="horizontal",
            name="name",
            label="Author Name",
            type="entry",
        )
        self.name.pack(fill="both", pady=12)

        def on_submit():
            try:
                id_value = self.id.__get__()
                name_value = self.name.__get__()

                db = DBConnection()
                db.execute(
                    """
                        DELETE FROM authors
                        WHERE author_id = ? OR author_name = ?
                        """,
                    (id_value, name_value),
                )

                messagebox.showinfo(
                    title="question",
                    message="Author deleted successfully!",
                    detail=f"ID: {id_value} Or Name: {name_value}",
                    icon="info",
                )

            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(self, text="Submit", padding=(8, 4), command=on_submit).pack(
            pady=(10, 0)
        )

    def update_event(self):
        def on_submit():
            try:
                db = DBConnection()

                id = self.af.id.__get__()
                name = self.af.name.__get__()
                address = self.af.address.__get__()
                gov_reg = self.af.gov_reg_no.__get__()
                agree_time = self.af.agree_time.__get__()

                if not id:
                    return messagebox.showerror("Error", "ID is required!")

                db.execute(
                    """
                        UPDATE authors
                        SET 
                            author_id = ?,
                            author_name = ?,
                            address = ?,
                            gov_reg_no = ?,
                            agreement_time = ?,
                        WHERE author_id = ?
                        """,
                    (name, address, gov_reg, agree_time, id),
                )

                return messagebox.showinfo(
                    title="Success",
                    message="Author updated successfully!",
                    detail=f"""
                    ID: {id}\n
                    Name: {name}\n
                    Address: {address}\n
                    Government Registration Number: {gov_reg}\n
                    Agreement Time: {agree_time}
                    """,
                    icon="info",
                )

            except Exception as e:
                return messagebox.showerror("Error", str(e))

        self.af = AuthorForm(self.container, command=on_submit)
        self.af.pack(fill="both", expand=True, padx=12, pady=12)


class PublisherWindow(WindowClass):
    def __init__(self, parent, title: str):
        super().__init__(parent, title)
        self.columnconfigure(0, weight=1)
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", padx=12, pady=12)

    def add_event(self):
        def on_submit():
            try:
                db = DBConnection()
                if (
                    not self.pf.id.__get__()
                    or not self.pf.name.__get__()
                    or not self.pf.address.__get__()
                    or not self.pf.gov_reg_no.__get__()
                    or not self.pf.agree_time.__get__()
                ):
                    return messagebox.showerror("Error", "All fields are required!")

                db.execute(
                    """
                        INSERT INTO publishers (publisher_id, publisher_name, address, gov_reg_no, agreement_time) 
                        VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        self.pf.id.__get__(),
                        self.pf.name.__get__(),
                        self.pf.address.__get__(),
                        self.pf.gov_reg_no.__get__(),
                        self.pf.agree_time.__get__(),
                    ),
                )

                return messagebox.showinfo(
                    title="Publisher Addition",
                    message="Publisher Added Successfully!",
                    detail=f"""
                    ID: {self.pf.id.__get__()}\n
                    Name: {self.pf.name.__get__()}\n
                    Address: {self.pf.address.__get__()}\n
                    Government Registration Number: {self.pf.gov_reg_no.__get__()}\n
                    Agreement Time: {self.pf.agree_time.__get__()}\n
                    """,
                    icon="info",
                )
            except Exception as e:
                return messagebox.showerror("Error", f"{str(e)}")

        self.pf = PublisherForm(self.container, command=on_submit)
        self.pf.pack(fill="both", expand=True, padx=12, pady=12)

    def delete_event(self):
        self.id = FormEntry(
            self.container,
            direction="horizontal",
            name="publisher_id",
            label="Publisher ID",
            type="entry",
        )
        self.id.pack(fill="both", pady=12)

        ttk.Separator(self.container, orient="horizontal").pack(
            fill="x", padx=12, pady=12
        )

        self.name = FormEntry(
            self.container,
            direction="horizontal",
            name="publisher_name",
            label="Publisher Name",
            type="entry",
        )
        self.name.pack(fill="both", pady=12)

        def on_submit():
            try:
                id_value = self.id.__get__()
                name_value = self.name.__get__()

                db = DBConnection()
                db.execute(
                    """
                            DELETE FROM publishers
                            WHERE publisher_id = ? OR publisher_name = ?
                            """,
                    (id_value, name_value),
                )

                messagebox.showinfo(
                    title="Publisher Deletion",
                    message="Publisher deleted successfully!",
                    icon="info",
                )

            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(self, text="Submit", padding=(8, 4), command=on_submit).pack(
            pady=(10, 0)
        )

    def update_event(self):
        def on_submit():
            try:
                db = DBConnection()

                id = self.pf.id.__get__()
                name = self.pf.name.__get__()
                address = self.pf.address.__get__()
                gov_reg_no = self.pf.gov_reg_no.__get__()
                agree_time = self.pf.agree_time.__get__()

                if not id:
                    return messagebox.showerror("Error", "ID is required!")

                db.execute(
                    """
                    UPDATE publishers
                    SET 
                        publisher_name = ?,
                        address = ?,
                        gov_reg_no = ?,
                        agreement_time = ?
                    WHERE publisher_id = ?
                    """,
                    (
                        id,
                        name,
                        address,
                        gov_reg_no,
                        agree_time,
                    ),
                )

                return messagebox.showinfo(
                    title="Publisher Update",
                    message="Publisher Updated Successfully!",
                    detail=f"""
                    ID: {id}\n
                    Name: {name}
                    """,
                    icon="info",
                )

            except Exception as e:
                return messagebox.showerror(title="Error", message=str(e))

        self.pf = PublisherForm(self.container, command=on_submit)
        self.pf.pack(fill="both", expand=True, padx=12, pady=12)


class MemberWindow(WindowClass):
    def __init__(self, parent, title: str):
        super().__init__(parent, title)
        self.columnconfigure(0, weight=1)
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", padx=12, pady=12)

    def add_event(self):
        def on_submit():
            try:
                db = DBConnection()
                if (
                    not self.mf.id.__get__()
                    or not self.mf.name.__get__()
                    or not self.mf.contact_no.__get__()
                    or not self.mf.age.__get__()
                    or not self.mf.member_type.__get__()
                    or not self.mf.membership_status.__get__()
                ):
                    return messagebox.showerror("Error", "All fields are required!")

                db.execute(
                    """
                    INSERT INTO members (member_id, name_name, contact_no, age, membership_type, membership_status) 
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        self.mf.id.__get__(),
                        self.mf.name.__get__(),
                        self.mf.contact_no.__get__(),
                        self.mf.age.__get__(),
                        self.mf.member_type.__get__(),
                        self.mf.membership_status.__get__(),
                    ),
                )

                return messagebox.showinfo(
                    title="Member Addition",
                    message="Member Added Successfully!",
                    detail=f"""
                        ID: {self.mf.id.__get__()}\n
                        Name: {self.mf.name.__get__()}\n
                        Contact Number: {self.mf.contact_no.__get__()}\n
                        Age: {self.mf.age.__get__()}\n
                        Membership Type: {self.mf.member_type.__get__()}\n
                        Membership Status: {self.mf.membership_status.__get__()}
                        """,
                    icon="info",
                )
            except Exception as e:
                return messagebox.showerror("Error", f"{str(e)}")

        self.mf = MemberForm(self.container, command=on_submit)
        self.mf.pack(fill="both", expand=True, padx=12, pady=12)

    def delete_event(self):
        self.id = FormEntry(
            self.container,
            direction="horizontal",
            name="member_id",
            label="Member ID",
            type="entry",
        )
        self.id.pack(fill="both", pady=12)

        ttk.Separator(self.container, orient="horizontal").pack(
            fill="x", padx=12, pady=12
        )

        self.name = FormEntry(
            self.container,
            direction="horizontal",
            name="member_name",
            label="Member Name",
            type="entry",
        )
        self.name.pack(fill="both", pady=12)

        def on_submit():
            try:
                id_value = self.id.__get__()
                name_value = self.name.__get__()

                db = DBConnection()
                db.execute(
                    """
                    DELETE FROM members
                    WHERE member_id = ? OR member_name = ?
                    """,
                    (id_value, name_value),
                )

                messagebox.showinfo(
                    title="Member Deletion",
                    message="Member deleted successfully!",
                    icon="info",
                )

            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(self, text="Submit", padding=(8, 4), command=on_submit).pack(
            pady=(10, 0)
        )

    def update_event(self):
        def on_submit():
            try:
                db = DBConnection()

                id = self.mf.id.__get__()
                name = self.mf.name.__get__()
                contact_no = self.mf.contact_no.__get__()
                age = self.mf.age.__get__()
                member_type = self.mf.member_type.__get__()
                member_status = self.mf.membership_status.__get__()

                if not id:
                    return messagebox.showerror("Error", "ID is required!")

                db.execute(
                    """
                    UPDATE members
                    SET 
                        member_name = ?,
                        contact_no = ?,
                        age = ?,
                        membership_type = ?
                        membership_status = ?
                    WHERE publisher_id = ?
                    """,
                    (
                        id,
                        name,
                        contact_no,
                        age,
                        member_type,
                        member_status,
                    ),
                )

                return messagebox.showinfo(
                    title="Members Update",
                    message="Members Updated Successfully!",
                    detail=f"""
                    ID: {id}\n
                    Name: {name}
                    """,
                    icon="info",
                )

            except Exception as e:
                return messagebox.showerror(title="Error", message=str(e))

        self.mf = MemberForm(self.container, command=on_submit)
        self.mf.pack(fill="both", expand=True, padx=12, pady=12)
