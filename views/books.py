"""
Book View Module

This module contains the BookView class and related functions for managing
the book management interface in the library management system.
"""

from tkinter import ttk
from repository._book_repository import BookRepository
from controllers._book_controller import BookActionController
from .components import search_component, details_component, button_toolbar

book_action = BookActionController(BookRepository())


class BookView:
    """
    Manages the user interface for book operations.

    This class handles the creation and layout of GUI components for both
    printed books and e-books, including search functionality, action buttons,
    and detailed form inputs.

    Attributes:
        controller: The controller instance that handles business logic.
    """

    def __init__(self) -> None:
        """
        Initialize the BookView.
        """
        pass

    def create_ebooks_tab(self, parent: ttk.Frame) -> None:
        """
        Create and configure the e-books tab interface.

        This method sets up the complete UI for managing electronic books, including:
        - Search functionality by ISBN
        - Action buttons (Add, Update, Delete, Clear)
        - Detailed form for e-book information

        Args:
            parent_container (ttk.Frame): The parent frame to contain all components.

        Returns:
            None
        """

        search_component(
            parent,
            title="Search Book",
            button_text="Search",
            label_text="ISBN: ",
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        book_form = details_component(
            parent,
            title="Book Details",
            labels=[
                "ISBN",
                "Title",
                "Author",
                "Publisher",
                "Status",
            ],
            name_list=[
                "isbn",
                "title",
                "author",
                "publisher",
                "status",
            ],
        )
        book_form.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
        )

        button_toolbar(
            parent,
            text=[
                "Add",
                "Update",
                "Delete",
                "Clear",
            ],
            func=[],
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
        )

    def create_printed_books_tab(self, parent: ttk.Frame) -> None:
        """
        Create and configure the printed books tab interface.

        This method sets up the complete UI for managing printed books, including:
        - Search functionality by ISBN
        - Action buttons (Add, Update, Delete, Clear)
        - Detailed form for book information

        Args:
            parent_container (ttk.Frame): The parent frame to contain all components.

        Returns:
            None
        """
        search_component(
            parent,
            title="Search Book",
            button_text="Search",
            label_text="ISBN: ",
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        button_toolbar(
            parent,
            text=[
                "Add",
                "Update",
                "Delete",
                "Clear",
            ],
            func=[],
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
        )

        book_form = details_component(
            parent=parent,
            title="Book Details",
            labels=[
                "ISBN",
                "Title",
                "Author",
                "Publisher",
                "Status",
            ],
            name_list=[
                "isbn",
                "title",
                "author",
                "publisher",
                "status",
            ],
        )
        book_form.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
        )


def create_book_interface(container: ttk.Frame, controller=None) -> ttk.Notebook:
    """
    Create the complete book management interface with tabbed navigation.

    This function creates a notebook widget containing separate tabs for
    printed books and e-books, each with their own management interface.

    Args:
        parent_container (ttk.Frame): The parent container to hold the notebook.
        controller: Optional controller instance for handling business logic.

    Returns:
        ttk.Notebook: The notebook widget containing both book management tabs.

    Example:
        >>> root = tk.Tk()
        >>> main_frame = ttk.Frame(root)
        >>> book_notebook = create_book_interface(main_frame, my_controller)
        >>> book_notebook.pack(fill="both", expand=True)
    """

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
