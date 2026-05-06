import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from typing import Any

from services.AuthorService import AuthorActionController
from services.BookService import BookActionController
from services.MemberService import MemberActionController
from services.PublisherService import PublisherActionController


class BookSearchComponent(ttk.Labelframe):

    def __init__(
        self,
        parent: ttk.Widget,
        title: str,
        button_text: str,
        label_text: str,
        service: BookActionController,
    ):
        super().__init__(parent, text=title)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, weight=1)

        self.service = service
        self.label_text = label_text
        self.button_text = button_text
        self.service = service

        self.__widget__()
        self.__layout__()
        self.__function__()

    def __widget__(self):
        self.lbl = ttk.Label(self, text=self.label_text)
        self.search_var = tk.StringVar(value="Enter the Value")
        self.entry = ttk.Entry(self, textvariable=self.search_var, width=60)
        self.button = ttk.Button(
            self, text=self.button_text, command=self.__get_search__
        )
        self.res_lbl = ttk.Label(self, text="", foreground="grey")

    def __layout__(self):
        self.lbl.grid(row=0, column=0, padx=4, pady=4)
        self.entry.grid(row=0, column=1, padx=8, pady=4, sticky="ew")
        self.button.grid(row=0, column=2, padx=8, pady=4)
        self.res_lbl.grid(row=1, column=0, columnspan=3, padx=4, pady=4, sticky="ew")

    def __function__(self):
        self.entry.bind("<Return>", lambda event: self.__get_search__())

    def __get_search__(self):
        try:
            if not self.search_var.get():
                return messagebox.showwarning("warning", f"Value is Missing!")

            res = self.service.handle_get_one(value=self.search_var.get())
            return self.__set_search__(f"Result: {res} ")

        except:
            return messagebox.showerror(
                "Error",
                f"Search triggered for: {self.search_var.get()} (No command bound)",
            )

    def __set_search__(self, message: Any):
        return self.res_lbl.config(text=message)


class AuthorSearchComponent(ttk.Labelframe):

    def __init__(
        self,
        parent: ttk.Widget,
        title: str,
        button_text: str,
        label_text: str,
        service: AuthorActionController,
    ):
        super().__init__(parent, text=title)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, weight=1)

        self.service = service
        self.label_text = label_text
        self.button_text = button_text
        self.service = service

        self.__widget__()
        self.__layout__()
        self.__function__()

    def __widget__(self):
        self.lbl = ttk.Label(self, text=self.label_text)
        self.search_var = tk.StringVar(value="Enter the Value")
        self.entry = ttk.Entry(self, textvariable=self.search_var, width=60)
        self.button = ttk.Button(
            self, text=self.button_text, command=self.__get_search__
        )
        self.res_lbl = ttk.Label(self, text="", foreground="grey")

    def __layout__(self):
        self.lbl.grid(row=0, column=0, padx=4, pady=4)
        self.entry.grid(row=0, column=1, padx=8, pady=4, sticky="ew")
        self.button.grid(row=0, column=2, padx=8, pady=4)
        self.res_lbl.grid(row=1, column=0, columnspan=3, padx=4, pady=4, sticky="ew")

    def __function__(self):
        self.entry.bind("<Return>", lambda event: self.__get_search__())

    def __get_search__(self):
        try:
            if not self.search_var.get():
                return messagebox.showwarning("warning", f"Value is Missing!")

            res = self.service.handle_get_one(author_id=self.search_var.get())
            return self.__set_search__(f"Result: {res} ")

        except:
            return messagebox.showerror(
                "Error",
                f"Search triggered for: {self.search_var.get()} (No command bound)",
            )

    def __set_search__(self, message: Any):
        return self.res_lbl.config(text=message)


class MemberSearchComponent(ttk.Labelframe):
    def __init__(
        self,
        parent: ttk.Widget,
        title: str,
        button_text: str,
        label_text: str,
        service: MemberActionController,
    ):
        super().__init__(parent, text=title)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, weight=1)

        self.service = service
        self.label_text = label_text
        self.button_text = button_text
        self.service = service

        self.__widget__()
        self.__layout__()
        self.__function__()

    def __widget__(self):
        self.lbl = ttk.Label(self, text=self.label_text)
        self.search_var = tk.StringVar(value="Enter the Value")
        self.entry = ttk.Entry(self, textvariable=self.search_var, width=60)
        self.button = ttk.Button(
            self, text=self.button_text, command=self.__get_search__
        )
        self.res_lbl = ttk.Label(self, text="", foreground="grey")

    def __layout__(self):
        self.lbl.grid(row=0, column=0, padx=4, pady=4)
        self.entry.grid(row=0, column=1, padx=8, pady=4, sticky="ew")
        self.button.grid(row=0, column=2, padx=8, pady=4)
        self.res_lbl.grid(row=1, column=0, columnspan=3, padx=4, pady=4, sticky="ew")

    def __function__(self):
        self.entry.bind("<Return>", lambda event: self.__get_search__())

    def __get_search__(self):
        try:
            if not self.search_var.get():
                return messagebox.showwarning("warning", f"Value is Missing!")

            res = self.service.handle_get_one(id=self.search_var.get())
            return self.__set_search__(f"Result: {res} ")

        except:
            return messagebox.showerror(
                "Error",
                f"Search triggered for: {self.search_var.get()} (No command bound)",
            )

    def __set_search__(self, message: Any):
        return self.res_lbl.config(text=message)


class PublisherSearchComponent(ttk.Labelframe):
    def __init__(
        self,
        parent: ttk.Widget,
        title: str,
        button_text: str,
        label_text: str,
        service: PublisherActionController,
    ):
        super().__init__(parent, text=title)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, weight=1)

        self.service = service
        self.label_text = label_text
        self.button_text = button_text
        self.service = service

        self.__widget__()
        self.__layout__()
        self.__function__()

    def __widget__(self):
        self.lbl = ttk.Label(self, text=self.label_text)
        self.search_var = tk.StringVar(value="Enter the Value")
        self.entry = ttk.Entry(self, textvariable=self.search_var, width=60)
        self.button = ttk.Button(
            self, text=self.button_text, command=self.__get_search__
        )
        self.res_lbl = ttk.Label(self, text="", foreground="grey")

    def __layout__(self):
        self.lbl.grid(row=0, column=0, padx=4, pady=4)
        self.entry.grid(row=0, column=1, padx=8, pady=4, sticky="ew")
        self.button.grid(row=0, column=2, padx=8, pady=4)
        self.res_lbl.grid(row=1, column=0, columnspan=3, padx=4, pady=4, sticky="ew")

    def __function__(self):
        self.entry.bind("<Return>", lambda event: self.__get_search__())

    def __get_search__(self):
        try:
            if not self.search_var.get():
                return messagebox.showwarning("warning", f"Value is Missing!")

            res = self.service.handle_get_one(id=self.search_var.get())
            return self.__set_search__(f"Result: {res} ")

        except:
            return messagebox.showerror(
                "Error",
                f"Search triggered for: {self.search_var.get()} (No command bound)",
            )

    def __set_search__(self, message: Any):
        return self.res_lbl.config(text=message)
