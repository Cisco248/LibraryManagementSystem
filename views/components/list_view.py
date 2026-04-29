from tkinter import ttk
from services.book_service import BookActionController
from services.author_service import AuthorActionController
from services.member_service import MemberActionController
from services.publisher_service import PublisherActionController


class BookListView(ttk.Frame):
    def __init__(self, master: ttk.Widget):
        super().__init__(master)

        self.pack(fill="both", expand=True, padx=12, pady=6)

        self.list_view = ttk.Treeview(
            self,
            columns=[
                "isbn",
                "title",
                "author",
                "publisher",
                "publication_year",
                "book_type",
                "status",
                "file_format",
                "file_size",
            ],
            show="headings",
        )
        self.list_view.heading("isbn", text="ISBN")
        self.list_view.heading("title", text="Title")
        self.list_view.heading("author", text="Author")
        self.list_view.heading("publisher", text="Publisher")
        self.list_view.heading("publication_year", text="Year")
        self.list_view.heading("book_type", text="Type")
        self.list_view.heading("status", text="Status")
        self.list_view.heading("file_format", text="Format")
        self.list_view.heading("file_size", text="Size")

        self.list_view.column("isbn", width=120, anchor="center")
        self.list_view.column("title", width=200, anchor="center")
        self.list_view.column("author", width=150, anchor="center")
        self.list_view.column("publisher", width=150, anchor="center")
        self.list_view.column("publication_year", width=80, anchor="center")
        self.list_view.column("book_type", width=100, anchor="center")
        self.list_view.column("status", width=100, anchor="center")
        self.list_view.column("file_format", width=80, anchor="center")
        self.list_view.column("file_size", width=100, anchor="center")

        self.list_view.pack(fill="both", expand=True)

        self.add_sample_data()

    def add_sample_data(self):
        """Fetch real data from database via controller"""
        controller = BookActionController()
        books = controller.handle_get_all()

        if not isinstance(books, list):
            print("Error retrieving books:", books)
            return

        for book in books:
            book_row = (
                book.isbn,
                book.title,
                book.author,
                book.publisher,
                book.publication_year,
                book.book_type,
                book.status,
                book.file_format,
                book.file_size,
            )
            self.list_view.insert("", "end", values=book_row)


class BarrowBookListView(ttk.Frame):
    def __init__(self, master: ttk.Widget):
        super().__init__(master)

        self.pack(fill="both", expand=True, padx=12, pady=6)

        self.list_view = ttk.Treeview(
            self,
            columns=[
                "isbn",
                "title",
                "member",
                "status",
            ],
            show="headings",
        )
        self.list_view.heading("isbn", text="ISBN")
        self.list_view.heading("title", text="Title")
        self.list_view.heading("member", text="Member")
        self.list_view.heading("status", text="Status")

        self.list_view.column("isbn", width=120, anchor="center")
        self.list_view.column("title", width=200, anchor="center")
        self.list_view.column("member", width=200, anchor="center")
        self.list_view.column("status", width=100, anchor="center")

        self.list_view.pack(fill="both", expand=True)


class MemberListView(ttk.Frame):
    def __init__(self, master: ttk.Widget):
        super().__init__(master)

        self.pack(fill="both", expand=True, padx=12, pady=6)

        style = ttk.Style()

        style.configure(
            "Treeview",
            background="white",
            foreground="black",
            rowheight=25,
            fieldbackground="white",
        )

        style.map(
            "Treeview",
            background=[("selected", "#0078d7")],
            foreground=[("selected", "white")],
        )

        style.configure(
            "Treeview.Heading",
            background="#a8a8a8",
            foreground="black",
            relief="flat",
            font=("Poppins", 8, "bold"),
        )

        style.map("Treeview.Heading", background=[("active", "#e0e0e0")])

        self.list_view = ttk.Treeview(
            self,
            columns=[
                "member_id",
                "member_name",
                "contact_no",
                "age",
                "membership_type",
                "membership_status",
            ],
            show="headings",
        )

        self.list_view.heading("member_id", text="Member ID")
        self.list_view.heading("member_name", text="Name")
        self.list_view.heading("contact_no", text="Contact No")
        self.list_view.heading("age", text="Age")
        self.list_view.heading("membership_type", text="Membership Type")
        self.list_view.heading("membership_status", text="Status")

        self.list_view.column("member_id", width=120, anchor="center")
        self.list_view.column("member_name", width=200, anchor="center")
        self.list_view.column("contact_no", width=150, anchor="center")
        self.list_view.column("age", width=80, anchor="center")
        self.list_view.column("membership_type", width=150, anchor="center")
        self.list_view.column("membership_status", width=120, anchor="center")

        self.list_view.pack(fill="both", expand=True)

        self.add_sample_data()

    def add_sample_data(self):
        """Fetch real data from database via controller"""
        controller = MemberActionController()
        members = controller.handle_get_all()

        if not isinstance(members, list):
            print("Error retrieving members:", members)
            return

        for member in members:
            member_row = (
                member.member_id,
                member.member_name,
                member.contact_no,
                member.age,
                member.membership_type,
                member.membership_status,
            )
            self.list_view.insert("", "end", values=member_row)


class AuthorListView(ttk.Frame):
    def __init__(self, master: ttk.Widget):
        super().__init__(master)

        self.pack(fill="both", expand=True, padx=12, pady=6)

        style = ttk.Style()

        style.configure(
            "Treeview",
            background="white",
            foreground="black",
            rowheight=25,
            fieldbackground="white",
        )

        style.map(
            "Treeview",
            background=[("selected", "#0078d7")],
            foreground=[("selected", "white")],
        )

        style.configure(
            "Treeview.Heading",
            background="#a8a8a8",
            foreground="black",
            relief="flat",
            font=("Poppins", 8, "bold"),
        )

        style.map("Treeview.Heading", background=[("active", "#e0e0e0")])

        self.list_view = ttk.Treeview(
            self,
            columns=[
                "author_id",
                "author_name",
                "address",
                "gov_reg_no",
                "author_type",
                "author_status",
                "reg_date",
            ],
            show="headings",
        )

        self.list_view.heading("author_id", text="Author ID")
        self.list_view.heading("author_name", text="Name")
        self.list_view.heading("address", text="Address")
        self.list_view.heading("gov_reg_no", text="Gov Reg No")
        self.list_view.heading("author_type", text="Membership Type")
        self.list_view.heading("author_status", text="Status")
        self.list_view.heading("reg_date", text="Reg Date")

        self.list_view.column("author_id", width=120, anchor="center")
        self.list_view.column("author_name", width=200, anchor="center")
        self.list_view.column("address", width=250, anchor="center")
        self.list_view.column("gov_reg_no", width=80, anchor="center")
        self.list_view.column("author_type", width=150, anchor="center")
        self.list_view.column("author_status", width=120, anchor="center")
        self.list_view.column("reg_date", width=120, anchor="center")

        self.list_view.pack(fill="both", expand=True)

        self.add_sample_data()

    def add_sample_data(self):
        """Fetch real data from database via controller"""
        controller = AuthorActionController()
        authors = controller.handle_get_all()

        if not isinstance(authors, list):
            print("Error retrieving authors:", authors)
            return

        for author in authors:
            author_row = (
                author.author_id,
                author.author_name,
                author.address,
                author.gov_reg_no,
                author.agreement_time,
                "Regular",
                "Active",
                "N/A",
            )
            self.list_view.insert("", "end", values=author_row)


class PublisherListView(ttk.Frame):
    def __init__(self, master: ttk.Widget):
        super().__init__(master)

        self.pack(fill="both", expand=True, padx=12, pady=6)

        style = ttk.Style()

        style.configure(
            "Treeview",
            background="white",
            foreground="black",
            rowheight=25,
            fieldbackground="white",
        )

        style.map(
            "Treeview",
            background=[("selected", "#0078d7")],
            foreground=[("selected", "white")],
        )

        style.configure(
            "Treeview.Heading",
            background="#a8a8a8",
            foreground="black",
            relief="flat",
            font=("Poppins", 8, "bold"),
        )

        style.map("Treeview.Heading", background=[("active", "#e0e0e0")])

        self.list_view = ttk.Treeview(
            self,
            columns=[
                "publisher_id",
                "publisher_name",
                "address",
                "gov_reg_no",
                "agreement_time",
            ],
            show="headings",
        )

        self.list_view.heading("publisher_id", text="Publisher ID")
        self.list_view.heading("publisher_name", text="Name")
        self.list_view.heading("address", text="Address")
        self.list_view.heading("gov_reg_no", text="Gov Reg No")
        self.list_view.heading("agreement_time", text="Agreement Time")

        self.list_view.column("publisher_id", width=120, anchor="center")
        self.list_view.column("publisher_name", width=200, anchor="center")
        self.list_view.column("address", width=250, anchor="center")
        self.list_view.column("gov_reg_no", width=80, anchor="center")
        self.list_view.column("agreement_time", width=150, anchor="center")

        self.list_view.pack(fill="both", expand=True)

        self.add_sample_data()

    def add_sample_data(self):
        controller = PublisherActionController()
        publishers = controller.handle_get_all()

        if not isinstance(publishers, list):
            raise ValueError("Error retrieving publishers:", publishers)

        for publisher in publishers:
            publisher_row = (
                publisher.publisher_id,
                publisher.publisher_name,
                publisher.address,
                publisher.gov_reg_no,
                publisher.agreement_time,
            )
            self.list_view.insert("", "end", values=publisher_row)
