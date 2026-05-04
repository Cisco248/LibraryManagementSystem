import sys
from pathlib import Path
from tkinter import messagebox
from typing import List
from models.BookModel import BookModel
from repository.BookRepository import BookRepository

sys.path.append(str(Path(__file__).resolve().parent.parent))


class BookActionController:

    def __init__(self):
        self.repository = BookRepository()

    def handle_import(self):
        try:
            res = self.repository.import_data()
            return messagebox.showinfo(title="Import Data", message=res)
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_export(self):
        try:
            res = self.repository.export_data()
            return messagebox.showinfo(title="Export Data", message=res)
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_get_one(self, value: str):
        try:
            return self.repository.get_one(value)
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_get_all(self):
        try:
            return self.repository.get_all()
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_add(self, data: BookModel):
        try:
            res = self.repository.add(data)
            return messagebox.showinfo(title="Add Data", message=res)
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_update(self, data: BookModel):
        try:
            res = self.repository.update(data)
            return messagebox.showinfo("Updated Data", res)
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_delete(self, value: str):
        try:
            res = self.repository.delete(value)
            return messagebox.showinfo("Delete Data", res)
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")
