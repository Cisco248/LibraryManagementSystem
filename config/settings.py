"""
Configuration Settings Module

This module contains all configuration settings for the Library Management System.
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database configuration
DATABASE_DIR = os.path.join(BASE_DIR, "database")
BOOKS_CSV = os.path.join(DATABASE_DIR, "book_data.csv")
MEMBERS_CSV = os.path.join(DATABASE_DIR, "member_data.csv")
AUTHORS_CSV = os.path.join(DATABASE_DIR, "author_data.csv")
PUBLISHERS_CSV = os.path.join(DATABASE_DIR, "publisher_data.csv")

# Ensure database directory exists
os.makedirs(DATABASE_DIR, exist_ok=True)

# Application settings
APP_TITLE = "Library Management System"
APP_WIDTH = 600
APP_HEIGHT = 600
APP_RESIZABLE = False

# UI Settings
THEME = "clam"
PADDING = 10
BUTTON_WIDTH = 12
ENTRY_WIDTH = 30

# CSV Field Names
BOOK_FIELDS = [
    "isbn",
    "title",
    "author",
    "publisher",
    "publication_year",
    "quantity",
    "book_type",
    "status",
    "file_format",
    "file_size",
]

MEMBER_FIELDS = [
    "member_id",
    "name",
    "email",
    "phone",
    "membership_date",
    "status",
]

AUTHOR_FIELDS = [
    "author_id",
    "name",
    "biography",
    "country",
    "birth_year",
]

PUBLISHER_FIELDS = [
    "publisher_id",
    "name",
    "country",
    "email",
    "phone",
]
