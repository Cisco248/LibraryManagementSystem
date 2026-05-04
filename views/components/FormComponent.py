from tkinter import ttk
import tkinter as tk

from models.BookModel import BookModel, BookType, BookStatus, FileFormat

from ..widgets import FormEntry


class BookForm(ttk.LabelFrame):

    def __init__(self, parent, title: str):
        super().__init__(parent, text=title, padding=(0, 8))
        for y in range(4):
            self.columnconfigure(y, weight=1)

        for x in range(3):
            self.rowconfigure(x)

        self.__widget__()
        self.__layout__()

    def __widget__(self):
        self.isbn = FormEntry(
            self,
            direction="vertical",
            name="isbn",
            label="ISBN*",
            type="entry",
            placeholder="E.g: 911-1234-567890",
        )

        self.title = FormEntry(
            self,
            direction="vertical",
            name="title",
            label="Title*",
            type="entry",
            placeholder="E.g: Python-Project-Book",
        )

        self.author = FormEntry(
            self,
            direction="vertical",
            name="author",
            label="Author*",
            type="entry",
            placeholder="E.g: A B John Doe",
        )

        self.publisher = FormEntry(
            self,
            direction="vertical",
            name="publisher",
            label="Publisher*",
            type="entry",
            placeholder="E.g: C D John Carter",
        )

        self.category = FormEntry(
            self,
            direction="vertical",
            name="category",
            label="Category*",
            type="selector",
            values=[
                "Fantasy",
                "Romance",
                "Horror",
                "Adventure",
                "Historical",
                "Biography",
                "Autobiography",
                "Self-Help",
                "Health & Fitness",
                "Business",
                "Economics",
                "Technology",
                "Programming",
                "Science",
                "Mathematics",
                "Education",
                "Religion",
                "Philosophy",
                "Psychology",
                "Politics",
                "Travel",
                "Cooking",
                "Food",
                "Art",
                "Music",
                "Sports",
                "Children Books",
                "Young Adult",
                "Comics",
            ],
            placeholder="E.g: IT and Computing",
        )

        self.year = FormEntry(
            self,
            direction="vertical",
            name="year",
            label="Year*",
            type="entry",
            placeholder="E.g: 2020",
        )

        self.book_type = FormEntry(
            self,
            direction="vertical",
            name="book_type",
            label="Type*",
            type="selector",
            values=["Printed", "Digital"],
            placeholder="E.g: Printed",
        )

        self.status = FormEntry(
            self,
            direction="vertical",
            name="status",
            label="Status*",
            type="selector",
            values=["Available", "Unavailable", "Borrowed", "Reserved"],
            placeholder="E.g: Available",
        )

        self.file_format = FormEntry(
            self,
            direction="vertical",
            name="file_format",
            label="File Format",
            type="selector",
            values=["HARDCOPY", "PDF", "EPUB", "MOBI"],
            placeholder="E.g: Hard Copy",
        )

        self.price = FormEntry(
            self,
            direction="vertical",
            name="price",
            label="Price*",
            type="entry",
            placeholder="E.g: LKR 1000",
        )

        self.ratings = FormEntry(
            self,
            direction="vertical",
            name="ratings",
            label="Ratings",
            type="selector",
            values=[
                "⭐",
                "⭐⭐",
                "⭐⭐⭐",
                "⭐⭐⭐⭐",
                "⭐⭐⭐⭐⭐",
            ],
            placeholder="E.g: 4.5",
        )

    def __layout__(self):
        self.isbn.grid(column=0, row=0, padx=4, sticky="ew")
        self.title.grid(column=1, row=0, padx=4, sticky="ew")
        self.author.grid(column=2, row=0, padx=4, sticky="ew")
        self.publisher.grid(column=3, row=0, padx=4, sticky="ew")

        self.category.grid(column=0, row=1, padx=4, sticky="ew")
        self.year.grid(column=1, row=1, padx=4, sticky="ew")
        self.book_type.grid(column=2, row=1, padx=4, sticky="ew")
        self.status.grid(column=3, row=1, padx=4, sticky="ew")

        self.file_format.grid(column=0, row=2, padx=4, sticky="ew")
        self.price.grid(column=1, row=2, padx=4, sticky="ew")
        self.ratings.grid(column=2, row=2, padx=4, sticky="ew")

    def __get__(self):
        return BookModel(
            isbn=self.isbn.__get__(),
            title=self.title.__get__(),
            author=self.author.__get__(),
            publisher=self.publisher.__get__(),
            category=self.category.__get__(),
            publication_year=self.year.__get__(),
            book_type=BookType(self.book_type.__get__()),
            status=BookStatus(self.status.__get__()),
            file_format=FileFormat(self.file_format.__get__()),
            price=self.price.__get__(),
            ratings=self.ratings.__get__(),
        )

    def __set__(self, data: dict):
        self.isbn.__set__(data.get("isbn", ""))
        self.title.__set__(data.get("title", ""))
        self.author.__set__(data.get("author", ""))
        self.publisher.__set__(data.get("publisher", ""))
        self.category.__set__(data.get("category", ""))
        self.year.__set__(data.get("year", ""))
        self.book_type.__set__(data.get("book_type", ""))
        self.status.__set__(data.get("status", ""))
        self.file_format.__set__(data.get("file_format", ""))
        self.price.__set__(data.get("price", ""))
        self.ratings.__set__(data.get("ratings", ""))

    def __clear__(self):
        for field in [
            self.isbn,
            self.title,
            self.author,
            self.publisher,
            self.category,
            self.year,
            self.book_type,
            self.status,
            self.file_format,
            self.price,
            self.ratings,
        ]:
            field.__clear__()


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
