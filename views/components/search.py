import tkinter as tk
from tkinter import ttk
from typing import Callable


class SearchComponent(ttk.Labelframe):
    """
    A reusable search bar component inheriting from ttk.LabelFrame.

    This component encapsulates a label, an entry field, a button, and a
    feedback label.
    """

    def __init__(
        self,
        parent: ttk.Widget,
        title: str,
        button_text: str,
        lable_text: str,
        command: Callable[[str], None],
    ):
        super().__init__(parent, text=title)
        self.command = command
        self.pack(fill="x", padx=12, pady=12)

        self.columnconfigure(2, weight=1)

        self.lbl = ttk.Label(self, text=lable_text)
        self.lbl.grid(row=0, column=0, padx=4, pady=4)

        self.search_var = tk.StringVar(value="Enter the Value")
        self.entry = ttk.Entry(self, textvariable=self.search_var, width=30)
        self.entry.grid(row=0, column=1, padx=8, pady=4, sticky="ew")

        self.entry.bind("<Return>", lambda event: self._on_search())

        self.button = ttk.Button(self, text=button_text, command=self._on_search)
        self.button.grid(row=0, column=2, padx=8, pady=4)

        self.res_lbl = ttk.Label(self, text="", foreground="grey")
        self.res_lbl.grid(row=1, column=0, columnspan=3, padx=4, pady=4, sticky="ew")

    def _on_search(self):
        query = self.search_var.get()
        if self.command:
            self.command(query)
        else:
            print(f"Search triggered for: {query} (No command bound)")

    def set_feedback(self, message: str, is_error: bool = False):
        color = "red" if is_error else "green"
        self.res_lbl.config(text=message, foreground=color)
