from pathlib import Path

from models.BookModel import BookModel

BASE_DIR = Path(__file__).resolve().parent.parent

# Application settings
APP_TITLE = "Library Management System"
APP_RESIZABLE = False

APP_HEADER_TITLE = "LibraSys"

APP_FOOTER_TEXT_1 = "© 2026 Library Management System | Developed by Lahiru Dilshan"
APP_FOOTER_TEXT_2 = "Powered by Python & Tkinter | Version 2.0"

# Window Component Settings
COLUMN_TITLES = ["ISBN", "Title", "Author", "Publisher", "Published", "Scanned At"]

# UI Settings
THEME = "clam"
PADDING = 10
BUTTON_WIDTH = 12
ENTRY_WIDTH = 30

# List View Settings
BOOK_LIST_COLUMN = [
    "isbn",
    "title",
    "author",
    "publisher",
    "category",
    "publication_year",
    "book_type",
    "status",
    "file_format",
    "price",
    "ratings",
]

BOOK_LIST_HEADING = {
    "isbn": "ISBN",
    "title": "Title",
    "author": "Author",
    "publisher": "Publisher",
    "category": "Category",
    "publication_year": "Year",
    "book_type": "Type",
    "status": "Status",
    "file_format": "Format",
    "price": "Price",
    "ratings": "Ratings",
}


MEMBER_LIST_COLUMN = [
    "member_id",
    "member_name",
    "contact_no",
    "age",
    "membership_type",
    "membership_status",
]

MEMBER_LIST_HEADING = {
    "member_id": "ID",
    "member_name": "Name",
    "contact_no": "Contact No",
    "age": "Age",
    "membership_type": "Type",
    "membership_status": "Status",
}

AUTHOR_LIST_COLUMN = [
    "author_id",
    "author_name",
    "address",
    "gov_reg_no",
    "reg_date",
]

AUTHOR_LIST_HEADING = {
    "author_id": "ID",
    "author_name": "Name",
    "address": "Address",
    "gov_reg_no": "Government Reg No",
    "reg_date": "Registration Date",
}

PUBLISHER_LIST_COLUMN = [
    "publisher_id",
    "publisher_name",
    "address",
    "gov_reg_no",
    "agreement_time",
]

PUBLISHER_LIST_HEADING = {
    "publisher_id": "ID",
    "publisher_name": "Name",
    "address": "Address",
    "gov_reg_no": "Government Reg No",
    "agreement_time": "Agreement Period",
}

# Repository Settings


BOOK_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS books (isbn TEXT PRIMARY KEY, title TEXT, author TEXT, publisher TEXT, category TEXT, publication_year INTEGER, book_type TEXT, status TEXT, file_format TEXT, price TEXT, ratings TEXT)"""

BOOK_IMPORT_PATH = BASE_DIR / "database/book_data.csv"

BOOK_IMPORT_QUERY = """INSERT OR IGNORE INTO books (isbn, title, author, publisher, category, publication_year, book_type, status, file_format, price, ratings) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

BOOK_EXPORT_PATH = BASE_DIR / "database/book_data.csv"

BOOK_EXPORT_QUERY = "SELECT * FROM books"

BOOK_GET_ONE_QUERY = "SELECT * FROM books WHERE isbn = ?"

BOOK_GET_ALL_QUERY = "SELECT * FROM books"

BOOK_ADD_QUERY = """INSERT INTO books (isbn, title, author, publisher, category, publication_year, book_type, status, file_format, price, ratings) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

BOOK_UPDATE_QUERY = """UPDATE books SET itle = ?, author = ?, publisher = ?, category = ?, publication_year = ?, book_type = ?, status = ?, file_format = ?, price = ?, ratings = ? WHERE isbn = ?"""

BOOK_DELETE_QUERY = "DELETE FROM books WHERE isbn = ?"
