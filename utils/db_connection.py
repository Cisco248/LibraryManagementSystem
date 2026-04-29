import sqlite3
from tkinter import messagebox
from typing import Any


class DBConnection:
    def __init__(self):
        self.conn = None
        self.cursor = None

        try:
            self.conn = sqlite3.connect("database/library_connection.sqlite")
            self.cursor = self.conn.cursor()

        except sqlite3.Error as e:
            raise RuntimeError("Error", f"{str(e)}")

    def execute(self, query: str, params: tuple = (), fetch: bool = False) -> Any:
        if not self.conn or not self.cursor:
            return messagebox.showerror("Error", "Database not initialized")

        try:
            self.cursor.execute(query, params)
            self.conn.commit()

            if fetch:
                return self.cursor.fetchall()

        except sqlite3.Error as err:
            self.conn.rollback()
            return messagebox.showerror("Error", f"{str(err)}")

    def close(self) -> None:
        if self.cursor and self.conn:
            self.cursor.close()
            self.conn.close()
