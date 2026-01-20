import tkinter as tk
from tkinter import ttk
from typing import Any, Callable, Optional, Type


class ExternalWindow(tk.Toplevel):
    """
    A generic modal popup window.
    """

    def __init__(
        self,
        parent,
        title: str,
        content_class: Type[tk.Widget],
        command: Optional[Callable[[tk.Widget], None]] = None,
        **kwargs: Any,
    ):
        super().__init__(parent)

        self.title(title)
        self.transient(parent)
        self.grab_set()
        self.focus_set()

        self.content = content_class(self, **kwargs)
        self.content.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.button = ttk.Button(
            self,
            text="Submit",
            padding=(8, 4),
            command=self.command,
        )

        self.button.pack()
