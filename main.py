"""
Library Management System - Main Application

This is the entry point for the Library Management System GUI application.
Uses tkinter (ttk) for the user interface and implements MVC architecture.
"""

from tkinter import Tk, ttk
from config.settings import APP_TITLE, APP_WIDTH, APP_HEIGHT
from views import books, members, authors, publishers


class LibraryManagementApp:
    """Main application class for Library Management System."""

    def __init__(self, root: Tk):
        """
        Initialize the Library Management Application.

        Args:
            root (Tk): The root window object.
        """
        self.root = root
        self.setup_window()
        self.create_ui()

    def setup_window(self) -> None:
        """Configure the main window properties."""
        self.root.title(APP_TITLE)
        self.root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.root.resizable(width=False, height=False)

        # Center window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_ui(self) -> None:
        """Create the user interface with tabs."""
        # Create main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create notebook (tabbed interface)
        self.tabs = ttk.Notebook(main_frame)
        self.tabs.pack(fill="both", expand=True)

        # Create tab frames
        self._create_books_tab()
        self._create_members_tab()
        self._create_authors_tab()
        self._create_publishers_tab()

    def _create_books_tab(self) -> None:
        """Create the Books management tab."""
        books_frame = ttk.Frame(self.tabs)
        self.tabs.add(books_frame, text="Books")
        books.create_book_interface(books_frame)

    def _create_members_tab(self) -> None:
        """Create the Members management tab."""
        members_frame = ttk.Frame(self.tabs)
        self.tabs.add(members_frame, text="Members")
        members.member_management_gui(members_frame)

    def _create_authors_tab(self) -> None:
        """Create the Authors management tab."""
        authors_frame = ttk.Frame(self.tabs)
        self.tabs.add(authors_frame, text="Authors")
        authors.author_management_gui(authors_frame)

    def _create_publishers_tab(self) -> None:
        """Create the Publishers management tab."""
        publishers_frame = ttk.Frame(self.tabs)
        self.tabs.add(publishers_frame, text="Publishers")
        publishers.publisher_management_gui(publishers_frame)


def main():
    """Main entry point for the application."""
    root = Tk()
    app = LibraryManagementApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
