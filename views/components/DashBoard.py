from tkinter import ttk
from typing import Tuple
from utils.DBConnection import DBConnection
from views.widgets.StatCard import StatCard


class Dashboard(ttk.Frame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, padding=10)
        self.db = DBConnection()
        self.kwargs = kwargs

        for i in range(5):
            self.columnconfigure(i, weight=1)

        self.values = [self.kwargs.get(f"value_{i}", "") for i in range(1, 6)]

        self.cards = []
        for i, value in enumerate(self.values):
            card = StatCard(self, value)
            card.grid(row=0, column=i, sticky="nsew", padx=4)
            self.cards.append(card)

        self.refresh()

    def refresh(self):
        self.result: Tuple = self.db.execute(self.kwargs.get("query", ""), fetch=True)
        if not self.result:
            return

        row = self.result[0]

        for i, card in enumerate(self.cards):
            value = row[i] if i < len(row) else 0
            card.update(value or 0)
