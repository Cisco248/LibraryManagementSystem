from tkinter import ttk


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

        self.list_view.pack(fill="both", expand=True)

        self.add_sample_data()

    def add_sample_data(self):
        """Add some sample books to demonstrate"""
        sample_books = [
            (
                "978-0-123456-78-9",
                "Python Programming",
                "John Doe",
                "Tech Books",
                "2023",
                "eBook",
                "Available",
                "PDF",
                "5.2 MB",
            ),
            (
                "978-0-987654-32-1",
                "Data Science Basics",
                "Jane Smith",
                "Data Press",
                "2022",
                "Hardcover",
                "Borrowed",
                "N/A",
                "N/A",
            ),
            (
                "978-1-111111-11-1",
                "Web Development",
                "Bob Johnson",
                "Web Publishers",
                "2024",
                "eBook",
                "Available",
                "EPUB",
                "3.8 MB",
            ),
            (
                "978-2-222222-22-2",
                "Machine Learning",
                "Alice Brown",
                "AI Books",
                "2023",
                "Paperback",
                "Available",
                "N/A",
                "N/A",
            ),
            (
                "978-3-333333-33-3",
                "Database Design",
                "Charlie Wilson",
                "Tech Press",
                "2021",
                "eBook",
                "Reserved",
                "PDF",
                "7.1 MB",
            ),
        ]

        for book in sample_books:
            self.list_view.insert("", "end", values=book)


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
        """Add some sample members to demonstrate"""
        sample_members = [
            ("M001", "John Doe", "+94 77 123 4567", "28", "Premium", "Active"),
            ("M002", "Jane Smith", "+94 71 234 5678", "35", "Standard", "Active"),
            ("M003", "Bob Johnson", "+94 76 345 6789", "42", "Premium", "Active"),
            ("M004", "Alice Brown", "+94 70 456 7890", "25", "Standard", "Inactive"),
            ("M005", "Charlie Wilson", "+94 75 567 8901", "31", "Premium", "Active"),
        ]

        for member in sample_members:
            self.list_view.insert("", "end", values=member)


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
        """Add some sample author to demonstrate"""
        sample_members = [
            (
                "M001",
                "John Doe",
                "+94 77 123 4567",
                "28",
                "Local",
                "Active",
                "2022-01-15",
            ),
            (
                "M002",
                "Jane Smith",
                "+94 71 234 5678",
                "35",
                "International",
                "Active",
                "2022-01-15",
            ),
            (
                "M003",
                "Bob Johnson",
                "+94 76 345 6789",
                "42",
                "Local",
                "Active",
                "2022-01-15",
            ),
            (
                "M004",
                "Alice Brown",
                "+94 70 456 7890",
                "25",
                "International",
                "Inactive",
                "2022-01-15",
            ),
            (
                "M005",
                "Charlie Wilson",
                "+94 75 567 8901",
                "31",
                "Local",
                "Active",
                "2022-01-15",
            ),
        ]

        for member in sample_members:
            self.list_view.insert("", "end", values=member)


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
                "publisher_type",
                "publisher_status",
                "reg_date",
            ],
            show="headings",
        )

        self.list_view.heading("publisher_id", text="Publisher ID")
        self.list_view.heading("publisher_name", text="Name")
        self.list_view.heading("address", text="Address")
        self.list_view.heading("gov_reg_no", text="Gov Reg No")
        self.list_view.heading("publisher_type", text="Membership Type")
        self.list_view.heading("publisher_status", text="Status")
        self.list_view.heading("reg_date", text="Reg Date")

        self.list_view.column("publisher_id", width=120, anchor="center")
        self.list_view.column("publisher_name", width=200, anchor="center")
        self.list_view.column("address", width=250, anchor="center")
        self.list_view.column("gov_reg_no", width=80, anchor="center")
        self.list_view.column("publisher_type", width=150, anchor="center")
        self.list_view.column("publisher_status", width=120, anchor="center")
        self.list_view.column("reg_date", width=120, anchor="center")

        self.list_view.pack(fill="both", expand=True)

        self.add_sample_data()

    def add_sample_data(self):
        """Add some sample Publisher to demonstrate"""
        sample_members = [
            (
                "M001",
                "John Doe",
                "+94 77 123 4567",
                "28",
                "Local",
                "Active",
                "2022-01-15",
            ),
            (
                "M002",
                "Jane Smith",
                "+94 71 234 5678",
                "35",
                "International",
                "Active",
                "2022-01-15",
            ),
            (
                "M003",
                "Bob Johnson",
                "+94 76 345 6789",
                "42",
                "Local",
                "Active",
                "2022-01-15",
            ),
            (
                "M004",
                "Alice Brown",
                "+94 70 456 7890",
                "25",
                "International",
                "Inactive",
                "2022-01-15",
            ),
            (
                "M005",
                "Charlie Wilson",
                "+94 75 567 8901",
                "31",
                "Local",
                "Active",
                "2022-01-15",
            ),
        ]

        for member in sample_members:
            self.list_view.insert("", "end", values=member)
