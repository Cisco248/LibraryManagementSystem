"""Simple reusable form field widget"""

from tkinter import ttk
import tkinter as tk


class DetailRow(ttk.Frame):

    def __init__(self, parent, field_name, label_text, field_type="entry"):
        super().__init__(parent)

        self.field_name = field_name
        self.field_type = field_type

        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.label = ttk.Label(self, text=label_text)
        self.label.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        self.value_var = tk.StringVar()

        if field_type == "entry":
            self.input = ttk.Entry(self, textvariable=self.value_var, width=40)
        else:
            self.input = ttk.Combobox(
                self, textvariable=self.value_var, width=40, state="readonly"
            )

        self.input.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

    def get_value(self):
        return self.value_var.get()

    def set_value(self, value):
        self.value_var.set(str(value) if value else "")

    def clear(self):
        self.value_var.set("")

    def set_options(self, options):
        if self.field_type == "selector":
            self.input["values"] = options

    # def enable(self):
    #     state = "readonly" if self.field_type == "selector" else "normal"
    #     self.input.config(state=state)

    # def disable(self):
    #     self.input.config(state="disabled")
