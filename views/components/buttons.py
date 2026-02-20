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

        super().__init__(parent)
        self.pack(fill="x", padx=12, pady=6)

        for col in range(4):
            self.columnconfigure(col, weight=1)

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
