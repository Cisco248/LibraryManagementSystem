from tkinter import ttk
from config.Configuration import (
    AUTHOR_LIST_COLUMN,
    AUTHOR_LIST_HEADING,
    BOOK_LIST_COLUMN,
    BOOK_LIST_HEADING,
    MEMBER_LIST_COLUMN,
    MEMBER_LIST_HEADING,
    PUBLISHER_LIST_COLUMN,
    PUBLISHER_LIST_HEADING,
)
from services.BookService import BookActionController
from services.AuthorService import AuthorActionController
from services.MemberService import MemberActionController
from services.PublisherService import PublisherActionController
from utils.Styles import ListStyle


class BookListView(ttk.Frame):

    def __init__(self, master: ttk.Widget, form):
        self.controller = BookActionController()
        self.form = form
        self.style = ListStyle(widget="TreeView", component="Heading")
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1)
        self.style.__map__()

        self.list_view = ttk.Treeview(
            self,
            columns=BOOK_LIST_COLUMN,
            show="headings",
            height=23,
        )

        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
        )

        headings = BOOK_LIST_HEADING
        if isinstance(headings, dict):
            headings = headings.items()

        for heading in headings:
            if isinstance(heading, (list, tuple)) and len(heading) == 2:
                column, text = heading
            else:
                column = heading
                text = heading
            self.list_view.heading(column, text=text)

        self.list_view.column("isbn", width=120, anchor="center")
        self.list_view.column("title", width=200, anchor="center")
        self.list_view.column("author", width=150, anchor="center")
        self.list_view.column("publisher", width=150, anchor="center")
        self.list_view.column("category", width=150, anchor="center")
        self.list_view.column("publication_year", width=80, anchor="center")
        self.list_view.column("book_type", width=100, anchor="center")
        self.list_view.column("status", width=100, anchor="center")
        self.list_view.column("file_format", width=80, anchor="center")
        self.list_view.column("price", width=100, anchor="center")
        self.list_view.column("ratings", width=100, anchor="center")

        self.list_view.bind("<<TreeviewSelect>>", self.__select__)

        self.list_view.grid(column=0, row=0, columnspan=2, sticky="nsew")
        self.scrollbar.grid(column=1, row=0, sticky="ns")

        self.__add__()

    def __select__(self, event):
        selected = self.list_view.selection()
        if not selected or not self.form:
            return

        item = self.list_view.item(selected[0])
        values = item["values"]

        data = {
            "isbn": values[0],
            "title": values[1],
            "author": values[2],
            "publisher": values[3],
            "category": values[4],
            "year": values[5],
            "book_type": values[6],
            "status": values[7],
            "file_format": values[8],
            "price": values[9],
            "ratings": values[10],
        }

        self.form.__set__(data)

    def __add__(self):
        books = self.controller.handle_get_all()
        if not isinstance(books, list):
            print("Error retrieving books:", books)
            return
        for book in books:
            book_row = (
                book[0],
                book[1],
                book[2],
                book[3],
                book[4],
                book[5],
                book[6],
                book[7],
                book[8],
                book[9],
                book[10],
            )
            self.list_view.insert("", "end", values=book_row)

    def __refresh__(self):
        for item in self.list_view.get_children():
            self.list_view.delete(item)

        self.__add__()


class MemberListView(ttk.Frame):
    def __init__(self):
        pass

    def __view__(self, master: ttk.Widget):
        super().__init__(master)
        self.pack(fill="both", expand=True, padx=12, pady=6)
        ListStyle(widget="TreeView", component="Heading").__map__()
        self.list_view = ttk.Treeview(self, columns=MEMBER_LIST_COLUMN, show="headings")

        headings = MEMBER_LIST_HEADING
        if isinstance(headings, dict):
            headings = headings.items()

        for heading in headings:
            if isinstance(heading, (list, tuple)) and len(heading) == 2:
                column, text = heading
            else:
                column = heading
                text = heading
            self.list_view.heading(column, text=text)

        self.list_view.column("member_id", width=120, anchor="center")
        self.list_view.column("member_name", width=200, anchor="center")
        self.list_view.column("contact_no", width=150, anchor="center")
        self.list_view.column("age", width=80, anchor="center")
        self.list_view.column("membership_type", width=150, anchor="center")
        self.list_view.column("membership_status", width=120, anchor="center")
        self.list_view.pack(fill="both", expand=True)

        self.__add__()

    def __add__(self):
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

    def __refresh__(self):
        for item in self.list_view.get_children():
            self.list_view.delete(item)

        self.__add__()


class AuthorListView(ttk.Frame):
    def __init__(self):
        pass

    def __view__(self, master: ttk.Widget):
        super().__init__(master)
        self.pack(fill="both", expand=True, padx=12, pady=6)
        ListStyle(widget="TreeView", component="Heading").__map__()
        self.list_view = ttk.Treeview(self, columns=AUTHOR_LIST_COLUMN, show="headings")

        headings = AUTHOR_LIST_HEADING
        if isinstance(headings, dict):
            headings = headings.items()

        for heading in headings:
            if isinstance(heading, (list, tuple)) and len(heading) == 2:
                column, text = heading
            else:
                column = heading
                text = heading
            self.list_view.heading(column, text=text)

        self.list_view.column("author_id", width=120, anchor="center")
        self.list_view.column("author_name", width=200, anchor="center")
        self.list_view.column("address", width=250, anchor="center")
        self.list_view.column("gov_reg_no", width=80, anchor="center")
        self.list_view.column("reg_date", width=120, anchor="center")

        self.list_view.pack(fill="both", expand=True)

        self.__add__()

    def __add__(self):
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

    def __refresh__(self):
        for item in self.list_view.get_children():
            self.list_view.delete(item)
        self.__add__()


class PublisherListView(ttk.Frame):
    def __init__(self):
        pass

    def __view__(self, master: ttk.Widget):
        super().__init__(master)
        self.pack(fill="both", expand=True, padx=12, pady=6)
        ListStyle(widget="TreeView", component="Heading").__map__()
        self.list_view = ttk.Treeview(
            self, columns=PUBLISHER_LIST_COLUMN, show="headings"
        )

        headings = PUBLISHER_LIST_HEADING
        if isinstance(headings, dict):
            headings = headings.items()

        for heading in headings:
            if isinstance(heading, (list, tuple)) and len(heading) == 2:
                column, text = heading
            else:
                column = heading
                text = heading
            self.list_view.heading(column, text=text)

        self.list_view.column("publisher_id", width=120, anchor="center")
        self.list_view.column("publisher_name", width=200, anchor="center")
        self.list_view.column("address", width=250, anchor="center")
        self.list_view.column("gov_reg_no", width=80, anchor="center")
        self.list_view.column("agreement_time", width=150, anchor="center")
        self.list_view.pack(fill="both", expand=True)

        self.__add__()

    def __add__(self):
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

    def __refresh__(self):
        for item in self.list_view.get_children():
            self.list_view.delete(item)
        self.__add__()
