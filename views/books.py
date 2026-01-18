"""
Book View Module

This module contains the BookView class and related functions for managing
the book management interface in the library management system.
"""

from tkinter import ttk
from .components import BookDetailsForm, SearchComponent


class BookView:
    """
    Manages the user interface for book operations.

    This class handles the creation and layout of GUI components for both
    printed books and e-books, including search functionality, action buttons,
    and detailed form inputs.
    """

    def __init__(self) -> None:
        pass

    def create_ebooks_tab(self, parent: ttk.Frame) -> None:

        def _on_search(isbn):
            print(f"Searching database for ISBN: {isbn}")
            if len(isbn) < 5:
                search_widget.set_feedback("Invalid ISBN format", is_error=True)
            else:
                search_widget.set_feedback(
                    f"Book found: 'Python Mastery'", is_error=False
                )

        search_widget = SearchComponent(
            parent,
            title="Find Book",
            button_text="Find",
            lable_text="ISBN: ",
            command=_on_search,
        )
        search_widget.pack(fill="x", padx=12, pady=12)

        list_view = BookDetailsForm(parent=parent, title="Book Details")
        list_view.pack(fill="x", padx=12, pady=12)

    def create_printed_books_tab(self, parent: ttk.Frame):

        def _on_search(isbn):
            print(f"Searching database for ISBN: {isbn}")
            if len(isbn) < 5:
                search_widget.set_feedback("Invalid ISBN format", is_error=True)
            else:
                search_widget.set_feedback(
                    f"Book found: 'Python Mastery'", is_error=False
                )

        search_widget = SearchComponent(
            parent,
            title="Find Book",
            button_text="Find",
            lable_text="ISBN: ",
            command=_on_search,
        )
        search_widget.pack(fill="x", padx=12, pady=12)

        list_view = BookDetailsForm(parent=parent, title="Book Details")
        list_view.pack(fill="x", padx=12, pady=12)


def create_book_interface(container: ttk.Frame, controller=None) -> ttk.Notebook:

    notebook = ttk.Notebook(container)
    notebook.pack(pady=10, expand=True, fill="both")

    book_view = BookView()

    printed_book_frame = ttk.Frame(notebook)
    notebook.add(printed_book_frame, text="Printed Books")
    book_view.create_printed_books_tab(printed_book_frame)

    ebooks_frame = ttk.Frame(notebook)
    notebook.add(ebooks_frame, text="E Books")
    book_view.create_ebooks_tab(ebooks_frame)

    return notebook
