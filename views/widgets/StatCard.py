from tkinter import ttk


class StatCard(ttk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, padding=10, relief="groove", border=2.0)

        self.columnconfigure(0, weight=1)

        self.title = ttk.Label(self, text=title, font=("Segoe UI", 10))
        self.title.grid(row=0, column=0)

        self.value = ttk.Label(self, text="0", font=("Segoe UI", 18, "bold"))
        self.value.grid(row=1, column=0)

    def update(self, value):
        self.value.config(text=str(value))
