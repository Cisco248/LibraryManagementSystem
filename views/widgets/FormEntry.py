from tkinter import ttk
import tkinter as tk


class FormEntry(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)

        self.kwargs = kwargs
        self.value_var = tk.StringVar()
        self.input = None

        if self.kwargs.get("direction", "") == "horizontal":
            self.columnconfigure(0, weight=1)

            self.label = ttk.Label(self, text=self.kwargs.get("label", "example"))
            self.label.grid(row=0, column=0, sticky="w", padx=8)

            if self.kwargs.get("type", "") == "entry":
                self.input = ttk.Entry(
                    self,
                    textvariable=self.value_var,
                    width=40,
                )
            else:
                self.input = ttk.Combobox(
                    self,
                    values=self.kwargs.get("values", []),
                    textvariable=self.value_var,
                    width=40,
                    state="readonly",
                )

            self.input.grid(row=1, column=0, sticky="ew", padx=4, pady=4)

        else:
            self.columnconfigure(1, weight=1)

            self.label = ttk.Label(self, text=self.kwargs.get("label", "example"))
            self.label.grid(row=0, column=0, sticky="w", padx=4, pady=4)

            if self.kwargs.get("type", "") == "entry":
                self.input = ttk.Entry(
                    self,
                    textvariable=self.value_var,
                    width=40,
                )
            else:
                self.input = ttk.Combobox(
                    self,
                    values=self.kwargs.get("values", []),
                    textvariable=self.value_var,
                    width=40,
                    state="readonly",
                )

            self.input.grid(row=0, column=1, sticky="ew", padx=4, pady=4)

    def __get__(self):
        return self.value_var.get()

    def __set__(self, value):
        self.value_var.set("" if value is None else str(value))

    def __clear__(self):
        self.value_var.set("")
