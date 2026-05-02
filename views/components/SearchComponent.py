import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from utils.DBConnection import DBConnection


class SearchComponent(ttk.Labelframe):
    def __init__(
        self,
        parent: ttk.Widget,
        title: str,
        button_text: str,
        lable_text: str,
        table: str,
        parameter1: str,
        parameter2: str,
    ):
        super().__init__(parent, text=title)
        self.pack(fill="both", padx=12, pady=12)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, weight=1)

        self.lbl = ttk.Label(self, text=lable_text)
        self.lbl.grid(row=0, column=0, padx=4, pady=4)

        self.search_var = tk.StringVar(value="Enter the Value")
        self.entry = ttk.Entry(self, textvariable=self.search_var, width=60)
        self.entry.grid(row=0, column=1, padx=8, pady=4, sticky="ew")

        self.entry.bind(
            "<Return>",
            lambda event: self.__get_search__(table, parameter1, parameter2),
        )

        self.button = ttk.Button(
            self,
            text=button_text,
            command=lambda: self.__get_search__(table, parameter1, parameter2),
        )
        self.button.grid(row=0, column=2, padx=8, pady=4)

        self.res_lbl = ttk.Label(self, text="", foreground="grey")
        self.res_lbl.grid(row=1, column=0, columnspan=3, padx=4, pady=4, sticky="ew")

    def __get_search__(self, table: str, parameter1: str, parameter2: str):
        try:
            self.db = DBConnection()
            query = self.search_var.get()
            if not query:
                return messagebox.showwarning(
                    "Warning", "Search query cannot be empty!"
                )

            res = self.db.execute(
                f"SELECT * FROM {table} WHERE {parameter1} LIKE ? OR {parameter2} LIKE ?",
                (f"%{query}%", f"%{query}%"),
                fetch=True,
            )
            return self.__set_search__(f"Result: {res[0]} ")

        except:
            return messagebox.showerror(
                "Error", f"Search triggered for: {query} (No command bound)"
            )

    def __set_search__(self, message: str, is_error: bool = False):
        color = "red" if is_error else "green"
        self.res_lbl.config(text=message, foreground=color)
