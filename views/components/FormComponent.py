from tkinter import ttk
import tkinter as tk

from ..widgets import FormEntry


class BookForm(tk.LabelFrame):

    def __init__(self, parent, command):
        super().__init__(parent, text="Add Book to Library", padx=12, pady=12)

        self.isbn = FormEntry(
            self, direction="horizontal", name="isbn", label="ISBN", type="entry"
        )
        self.isbn.pack(fill="x", pady=(10, 0))

        self.title = FormEntry(
            self, direction="horizontal", name="title", label="Title", type="entry"
        )
        self.title.pack(fill="x", pady=(10, 0))

        self.author = FormEntry(
            self, direction="horizontal", name="author", label="Author", type="entry"
        )
        self.author.pack(fill="x", pady=(10, 0))

        self.publisher = FormEntry(
            self,
            direction="horizontal",
            name="publisher",
            label="Publisher",
            type="entry",
        )
        self.publisher.pack(fill="x", pady=(10, 0))

        self.year = FormEntry(
            self, direction="horizontal", name="year", label="Year", type="entry"
        )
        self.year.pack(fill="x", pady=(10, 0))

        self.book_type = FormEntry(
            self,
            direction="horizontal",
            name="book_type",
            label="Book Type",
            type="selector",
            values=["Printed", "Digital"],
        )
        self.book_type.pack(fill="x", pady=(10, 0))

        self.status = FormEntry(
            self,
            direction="horizontal",
            name="status",
            label="Status",
            type="selector",
            values=["Available", "Unavailable", "Borrowed", "Reserved"],
        )
        self.status.pack(fill="x", pady=(10, 0))

        self.file_format = FormEntry(
            self,
            direction="horizontal",
            name="file_format",
            label="File Format",
            type="selector",
            values=["HARDCOPY", "PDF", "EPUB", "MOBI"],
        )
        self.file_format.pack(fill="x", pady=(10, 0))

        self.file_size = FormEntry(
            self,
            direction="horizontal",
            name="file_size",
            label="File Size",
            type="entry",
        )
        self.file_size.pack(fill="x", pady=(10, 0))

        submit_btn = ttk.Button(self, text="Submit", padding=(8, 4), command=command)
        submit_btn.pack(pady=(10, 0))

    def __get__(self):
        return {
            "isbn": self.isbn.__get__(),
            "title": self.title.__get__(),
            "author": self.author.__get__(),
            "publisher": self.publisher.__get__(),
            "year": self.year.__get__(),
            "book_type": self.book_type.__get__(),
            "status": self.status.__get__(),
            "file_format": self.file_format.__get__(),
            "file_size": self.file_size.__get__(),
        }


class AuthorForm(tk.LabelFrame):

    def __init__(self, parent, command):
        super().__init__(parent, text="Add Author to Library", padx=12, pady=12)

        self.id = FormEntry(
            self,
            direction="horizontal",
            name="author_id",
            label="Author ID",
            type="entry",
        )
        self.id.pack(fill="x", pady=(10, 0))

        self.name = FormEntry(
            self,
            direction="horizontal",
            name="author_name",
            label="Author Name",
            type="entry",
        )
        self.name.pack(fill="x", pady=(10, 0))

        self.address = FormEntry(
            self,
            direction="horizontal",
            name="address",
            label="Author Address",
            type="entry",
        )
        self.address.pack(fill="x", pady=(10, 0))

        self.gov_reg_no = FormEntry(
            self,
            direction="horizontal",
            name="gov_reg_no",
            label="Government Registration Number",
            type="entry",
        )
        self.gov_reg_no.pack(fill="x", pady=(10, 0))

        self.agree_time = FormEntry(
            self,
            direction="horizontal",
            name="agreement_time",
            label="Agreement Time",
            type="entry",
        )
        self.agree_time.pack(fill="x", pady=(10, 0))

        submit_btn = ttk.Button(self, text="Submit", padding=(8, 4), command=command)
        submit_btn.pack(pady=(10, 0))

    def __get__(self):
        return {
            "author_id": self.id.__get__(),
            "author_name": self.name.__get__(),
            "author_address": self.address.__get__(),
            "gov_reg_no": self.gov_reg_no.__get__(),
            "agreement_time": self.agree_time.__get__(),
        }


class PublisherForm(tk.LabelFrame):

    def __init__(self, parent, command):
        super().__init__(parent, text="Add Publisher to Library", padx=12, pady=12)

        self.id = FormEntry(
            self,
            direction="horizontal",
            name="publisher_id",
            label="Publisher ID",
            type="entry",
        )
        self.id.pack(fill="x", pady=(10, 0))

        self.name = FormEntry(
            self,
            direction="horizontal",
            name="publisher_name",
            label="Publisher Name",
            type="entry",
        )
        self.name.pack(fill="x", pady=(10, 0))

        self.address = FormEntry(
            self,
            direction="horizontal",
            name="address",
            label="Publisher Address",
            type="entry",
        )
        self.address.pack(fill="x", pady=(10, 0))

        self.gov_reg_no = FormEntry(
            self,
            direction="horizontal",
            name="gov_reg_no",
            label="Government Registration Number",
            type="entry",
        )
        self.gov_reg_no.pack(fill="x", pady=(10, 0))

        self.agree_time = FormEntry(
            self,
            direction="horizontal",
            name="agreement_time",
            label="Agreement Time",
            type="entry",
        )
        self.agree_time.pack(fill="x", pady=(10, 0))

        submit_btn = ttk.Button(self, text="Submit", padding=(8, 4), command=command)
        submit_btn.pack(pady=(10, 0))

    def __get__(self):
        return {
            "publisher_id": self.id.__get__(),
            "publisher_name": self.name.__get__(),
            "publisher_address": self.address.__get__(),
            "gov_reg_no": self.gov_reg_no.__get__(),
            "agreement_time": self.agree_time.__get__(),
        }


class MemberForm(tk.LabelFrame):

    def __init__(self, parent, command):
        super().__init__(parent, text="Add Member to Library", padx=12, pady=12)

        self.id = FormEntry(
            self,
            direction="horizontal",
            name="member_id",
            label="Member ID",
            type="entry",
        )
        self.id.pack(fill="x", pady=(10, 0))

        self.name = FormEntry(
            self,
            direction="horizontal",
            name="member_name",
            label="Member Name",
            type="entry",
        )
        self.name.pack(fill="x", pady=(10, 0))

        self.contact_no = FormEntry(
            self,
            direction="horizontal",
            name="contact_no",
            label="Contact Number",
            type="entry",
        )
        self.contact_no.pack(fill="x", pady=(10, 0))

        self.age = FormEntry(
            self,
            direction="horizontal",
            name="age",
            label="Member Age",
            type="entry",
        )
        self.age.pack(fill="x", pady=(10, 0))

        self.member_type = FormEntry(
            self,
            direction="horizontal",
            name="membership_type",
            label="Membership Type",
            type="selector",
            values=["Staff", "Client"],
        )
        self.member_type.pack(fill="x", pady=(10, 0))

        self.membership_status = FormEntry(
            self,
            direction="horizontal",
            name="membership_status",
            label="Membership Status",
            type="selector",
            values=["None", "Bronze", "Silver", "Gold", "Platinum"],
        )
        self.membership_status.pack(fill="x", pady=(10, 0))

        submit_btn = ttk.Button(self, text="Submit", padding=(8, 4), command=command)
        submit_btn.pack(pady=(10, 0))

    def __get__(self):
        return {
            "member_id": self.id.__get__(),
            "member_name": self.name.__get__(),
            "contact_no": self.contact_no.__get__(),
            "age": self.age.__get__(),
            "membership_type": self.member_type.__get__(),
            "membership_status": self.membership_status.__get__(),
        }
