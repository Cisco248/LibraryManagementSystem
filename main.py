"""
Library Management System - Main Application

This is the entry point for the Library Management System GUI application.
Uses tkinter (ttk) for the user interface and implements MVC architecture.
"""

from tkinter import Tk, ttk

from config.configure import APP_TITLE
from utils import app_header, app_footer
from views import BookView, AuthorView, PublisherView, MemberView


class MainAppRunner:
    def __init__(self):
        self.root = Tk()
        self.root.title(APP_TITLE)

        self.root.resizable(False, False)
        self.root.update_idletasks()
        self.root.wm_minsize(800, 1000)

        app_header.AppHeader(self.root)

        Root = self.ContentFrame(self.root)
        self.NoteBook(Root)
        
        BookView(self.notebook)
        AuthorView(self.notebook)
        PublisherView(self.notebook)
        MemberView(self.notebook)

        app_footer.AppFooter(self.root)

    def NoteBook(self, master: ttk.Frame):
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill="both", expand=True)
        return self.notebook

    def ContentFrame(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill="both", expand=True, padx=12, pady=12)
        return self.frame


def main():
    app = MainAppRunner()
    app.root.mainloop()


if __name__ == "__main__":
    main()
