from tkinter import ttk
import tkinter as tk
from app.services.book_management import PrintedBook

pb = PrintedBook()


class BookActionController:
    """
    Handles button click logic and UI updates.
    """

    def handle_add(self, target: ttk.Widget):
        """
        Creates and displays the details form.
        """

        book_data = {}

        for widget in target.winfo_children():
            if isinstance(widget, ttk.Entry):
                widget.config(state="normal")

                key = widget.winfo_name()
                value = widget.get()
                book_data[key] = value

                print(book_data)

        pb.add_book(book_data)

        print(book_data)

    def handle_clear(self, target: ttk.Widget):
        """
        Clears all entry boxes in a given form frame.
        """
        for widget in target.winfo_children():
            if isinstance(widget, (ttk.Entry, ttk.Entry)):
                current_state = widget["state"]
                widget.config(state="normal")
                widget.delete(0, tk.END)
                widget.config(state=current_state)

    def handle_delete(self, target: ttk.Widget):
        """
        Removes the component from the UI.
        """
        target.destroy()

    def handle_update(self, target: ttk.Widget):
        print("Update logic goes here...")

    def hide_container(self, target: ttk.Widget):
        """
        Removes the component from the UI.
        """
        target.grid_remove()


class PrintedBookActionController(BookActionController):

    def handle_status(self, t: str):
        r = pb.check_status(t)
        if isinstance(r, dict):
            return f"book is {r.get('Title', 'Unknown')}"
        return "book not found"

    def handle_update_status(self, t: str, ns: str):
        r = pb.update_status(t, ns)
        if isinstance(r, dict):
            return f"Book Status Update Successfully!"
        return f"Book Status Update Failed!"


class EBookActionController(BookActionController):

    def handle_e_book_add(self, target: ttk.Widget):
        return

    def handle_e_book_get(self, target: ttk.Widget):
        return

    def handle_download(self, target: ttk.Widget):
        return

    def handle_get_file_size(self, target: ttk.Widget):
        return
