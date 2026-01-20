"""
Library Management System - Main Application

This is the entry point for the Library Management System GUI application.
Uses tkinter (ttk) for the user interface and implements MVC architecture.
"""

from tkinter import Tk, ttk
from config.settings import APP_TITLE
from utils import AppHeader, AppFooter
from views import (
    BookView,
    MemberView,
    AuthorView,
    PublisherView,
)


class LibraryManagementApp:
    """Main application class for Library Management System."""

    def __init__(self, root: Tk):
        self.root = root
        self.root.title(APP_TITLE)

        self.root.resizable(width=False, height=False)
        self.root.update_idletasks()
        self.root.wm_minsize(height=800, width=1000)

        AppHeader(self.root)

        Root = self.ContentFrame(self.root)

        self.NoteBook(Root)

        BookView(self.notebook)
        MemberView(self.notebook)
        AuthorView(self.notebook)
        PublisherView(self.notebook)

        AppFooter(Root)

    def NoteBook(self, master: ttk.Frame):
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill="both", expand=True)
        return self.notebook

    def ContentFrame(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill="both", expand=True, padx=12, pady=12)
        return self.frame


def main():
    root = Tk()
    LibraryManagementApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
