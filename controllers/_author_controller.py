"""
Author Controller Module

Controller classes for managing author operations in the GUI.
"""

from tkinter import messagebox, ttk
import tkinter as tk
from services._author_service import AuthorService


class AuthorActionController:
    """Controller for handling author-related actions in the GUI."""

    def __init__(self):
        """Initialize the AuthorActionController."""
        self.service = AuthorService()

    def handle_add(self, data: dict) -> bool:
        """Add a new author."""
        try:
            self.service.add_author(data)
            messagebox.showinfo("Success", "Author added successfully!")
            return True
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add author: {str(e)}")
            return False

    def handle_clear(self, target: ttk.Widget) -> None:
        """Clear all Entry widgets in the given container."""
        for widget in target.winfo_children():
            if isinstance(widget, ttk.Entry):
                current_state = widget["state"]
                widget.config(state="normal")
                widget.delete(0, tk.END)
                widget.config(state=current_state)

    def handle_update(self, author_id: str, updates: dict) -> bool:
        """Update an author's information."""
        try:
            if not author_id:
                messagebox.showerror("Error", "Author ID is required for updating.")
                return False

            self.service.update_author(author_id, updates)
            messagebox.showinfo("Success", "Author updated successfully!")
            return True
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update author: {str(e)}")
            return False

    def handle_delete(self, author_id: str) -> bool:
        """Delete an author."""
        try:
            if not author_id:
                messagebox.showerror("Error", "Please provide an Author ID to delete.")
                return False

            confirm = messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete author with ID: {author_id}?",
            )

            if not confirm:
                return False

            self.service.delete_author(author_id)
            messagebox.showinfo("Success", "Author deleted successfully!")
            return True
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete author: {str(e)}")
            return False

    def get_all_authors(self) -> list:
        """Get all authors."""
        try:
            return self.service.get_all_authors()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve authors: {str(e)}")
            return []

    def search_authors(self, **criteria) -> list:
        """Search for authors by criteria."""
        try:
            return self.service.search_authors(**criteria)
        except Exception as e:
            messagebox.showerror("Error", f"Search failed: {str(e)}")
            return []

    def hide_container(self, target: ttk.Widget) -> None:
        """Hide the container widget."""
        target.grid_remove()

    def show_container(self, target: ttk.Widget, **grid_options) -> None:
        """Show the container widget."""
        target.grid(**grid_options)
