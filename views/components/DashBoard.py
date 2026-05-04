import tkinter as tk
from tkinter import ttk
from utils.DBConnection import DBConnection
from views.widgets.StatCard import StatCard


class Dashboard(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)

        # Layout
        for i in range(5):
            self.columnconfigure(i, weight=1)

        # Cards
        self.total = StatCard(self, "Total Books")
        self.available = StatCard(self, "Available")
        self.borrowed = StatCard(self, "Borrowed")
        self.reserved = StatCard(self, "Reserved")
        self.unavailable = StatCard(self, "Unavailable")

        self.total.grid(row=0, column=0, sticky="nsew", padx=5)
        self.available.grid(row=0, column=1, sticky="nsew", padx=5)
        self.borrowed.grid(row=0, column=2, sticky="nsew", padx=5)
        self.reserved.grid(row=0, column=3, sticky="nsew", padx=5)
        self.unavailable.grid(row=0, column=4, sticky="nsew", padx=5)

        self.refresh()

    def refresh(self):
        db = DBConnection()

        result = db.execute(
            """
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN status='Available' THEN 1 ELSE 0 END),
                SUM(CASE WHEN status='Borrowed' THEN 1 ELSE 0 END),
                SUM(CASE WHEN status='Reserved' THEN 1 ELSE 0 END),
                SUM(CASE WHEN status='Unavailable' THEN 1 ELSE 0 END)
            FROM books
            """,
            fetch=True,
        )

        row = result[0]

        self.total.update(row[0] or 0)
        self.available.update(row[1] or 0)
        self.borrowed.update(row[2] or 0)
        self.reserved.update(row[3] or 0)
        self.unavailable.update(row[4] or 0)
