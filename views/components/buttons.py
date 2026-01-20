from tkinter import ttk
from typing import Callable, Optional


class ButtonToolBar(ttk.Frame):
    """
    A reusable toolbar containing CRUD action buttons.
    """

    def __init__(
        self,
        parent: ttk.Widget,
        on_add: Optional[Callable] = None,
        on_delete: Optional[Callable] = None,
        on_update: Optional[Callable] = None,
        on_clear: Optional[Callable] = None,
    ):
        """
        Args:
            parent: The parent widget.
            on_add: Function to call when "Add Book" is clicked.
            on_delete: Function to call when "Delete Book" is clicked.
            on_update: Function to call when "Update Book" is clicked.
            on_clear: Function to call when "Clear All" is clicked.
        """
        super().__init__(parent)

        for col in range(4):
            self.columnconfigure(col, weight=1)

        # self.style = ttk.Style()

        # self.style.theme_create("add_button", parent="self.button1")

        self.button1 = ttk.Button(
            self,
            text="Add Book",
            padding=(16, 4),
            command=on_add if on_add else lambda: None,
        )
        self.button1.grid(row=0, column=0, padx=4, pady=4)

        self.button2 = ttk.Button(
            self,
            text="Delete Book",
            padding=(16, 4),
            command=on_delete if on_delete else lambda: None,
        )
        self.button2.grid(row=0, column=1, padx=4, pady=4)

        self.button3 = ttk.Button(
            self,
            text="Update Book",
            padding=(16, 4),
            command=on_update if on_update else lambda: None,
        )
        self.button3.grid(row=0, column=2, padx=4, pady=4)

        self.button4 = ttk.Button(
            self,
            text="Clear All",
            padding=(16, 4),
            command=on_clear if on_clear else lambda: None,
        )
        self.button4.grid(row=0, column=3, padx=4, pady=4)
