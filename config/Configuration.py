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

# Dashboard Settings

BOOK_DASHBOARD_QUERY = "SELECT COUNT(*) as total, SUM(CASE WHEN status='Available' THEN 1 ELSE 0 END), SUM(CASE WHEN status='Borrowed' THEN 1 ELSE 0 END), SUM(CASE WHEN status='Reserved' THEN 1 ELSE 0 END), SUM(CASE WHEN status='Unavailable' THEN 1 ELSE 0 END) FROM books"

AUTHOR_DASHBOARD_QUERY = "SELECT COUNT(*) as total FROM authors"

MEMBER_DASHBOARD_QUERY = "SELECT COUNT(*) as total, SUM(CASE WHEN membership_type='Staff' THEN 1 ELSE 0 END), SUM(CASE WHEN membership_type='Client' THEN 1 ELSE 0 END), SUM(CASE WHEN membership_status='Bronze' THEN 1 ELSE 0 END), SUM(CASE WHEN membership_status='Silver' THEN 1 ELSE 0 END) FROM members"

PUBLISHER_DASHBOARD_QUERY = "SELECT COUNT(*) as total FROM publishers"

# Repository Settings

##  Books
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

## Authors

AUTHOR_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS authors (author_id TEXT PRIMARY KEY, author_name TEXT, address TEXT, gov_reg_no TEXT, agreement_time DATE)"

AUTHOR_IMPORT_PATH = BASE_DIR / "database/author_data.csv"

AUTHOR_IMPORT_QUERY = "INSERT OR IGNORE INTO authors (author_id, author_name, address, gov_reg_no, agreement_time) VALUES (?, ?, ?, ?, ?)"

AUTHOR_EXPORT_PATH = BASE_DIR / "database/author_data.csv"

AUTHOR_EXPORT_QUERY = "SELECT * FROM books"

AUTHOR_GET_ONE_QUERY = "SELECT * FROM authors WHERE author_id = ?"

AUTHOR_GET_ALL_QUERY = "SELECT * FROM authors"

AUTHOR_ADD_QUERY = "INSERT INTO authors (author_id, author_name, address, gov_reg_no, agreement_time) VALUES (?, ?, ?, ?, ?)"

AUTHOR_UPDATE_QUERY = "UPDATE authors SET author_name = ?, address = ?, gov_reg_no = ?, agreement_time = ? WHERE author_id = ?"

AUTHOR_DELETE_QUERY = "DELETE FROM authors WHERE author_id = ?"

# Publisher

PUBLISHER_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS publishers ( publisher_id TEXT PRIMARY KEY, publisher_name TEXT, address TEXT, gov_reg_no TEXT, agreement_time TEXT )"

PUBLISHER_IMPORT_PATH = BASE_DIR / "database/publisher_data.csv"

PUBLISHER_IMPORT_QUERY = "INSERT OR IGNORE INTO publishers (publisher_id, publisher_name, address, gov_reg_no, agreement_time) VALUES (?, ?, ?, ?, ?)"

PUBLISHER_EXPORT_PATH = BASE_DIR / "database/publisher_data.csv"

PUBLISHER_EXPORT_QUERY = "SELECT * FROM publishers"

PUBLISHER_GET_ONE_QUERY = "SELECT * FROM publishers WHERE publisher_id = ?"

PUBLISHER_GET_ALL_QUERY = "SELECT * FROM publishers"

PUBLISHER_ADD_QUERY = "INSERT INTO publishers (publisher_id, publisher_name, address, gov_reg_no, agreement_time) VALUES (?, ?, ?, ?, ?)"

PUBLISHER_UPDATE_QUERY = "UPDATE publishers SET publisher_name = ?, address = ?, gov_reg_no = ?, agreement_time = ? WHERE publisher_id = ?"

PUBLISHER_DELETE_QUERY = "DELETE FROM publishers WHERE publisher_id = ?"

# Members

MEMBER_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS members ( member_id TEXT PRIMARY KEY, member_name TEXT, contact_no TEXT, age INTEGER, membership_type TEXT, membership_status TEXT )"

MEMBER_IMPORT_PATH = BASE_DIR / "database/member_data.csv"

MEMBER_IMPORT_QUERY = "INSERT OR IGNORE INTO members (member_id, member_name, contact_no, age, membership_type, membership_status) VALUES (?, ?, ?, ?, ?, ?)"

MEMBER_EXPORT_PATH = BASE_DIR / "database/member_data.csv"

MEMBER_EXPORT_QUERY = "SELECT * FROM members"

MEMBER_GET_ONE_QUERY = "SELECT * FROM members WHERE member_id = ?"

MEMBER_GET_ALL_QUERY = "SELECT * FROM members"

MEMBER_ADD_QUERY = "INSERT INTO members (member_id, member_name, contact_no, age, membership_type, membership_status) VALUES (?, ?, ?, ?, ?, ?)"

MEMBER_UPDATE_QUERY = "UPDATE members SET member_name = ?, contact_no = ?, age = ?, membership_type = ?, membership_status = ? WHERE member_id = ?"

MEMBER_DELETE_QUERY = "DELETE FROM members WHERE member_id = ?"
