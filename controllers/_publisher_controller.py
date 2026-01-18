"""
Publisher Controller Module

Controller classes for managing publisher operations in the GUI.
"""

from tkinter import messagebox, ttk
import tkinter as tk
from services._publisher_service import PublisherService


class PublisherActionController:
    """Controller for handling publisher-related actions in the GUI."""

    def __init__(self):
        """Initialize the PublisherActionController."""
        self.service = PublisherService()

    def handle_add(self, data: dict) -> bool:
        """Add a new publisher."""
        try:
            self.service.add_publisher(data)
            messagebox.showinfo("Success", "Publisher added successfully!")
            return True
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add publisher: {str(e)}")
            return False

    def handle_clear(self, target: ttk.Widget) -> None:
        """Clear all Entry widgets in the given container."""
        for widget in target.winfo_children():
            if isinstance(widget, ttk.Entry):
                current_state = widget["state"]
                widget.config(state="normal")
                widget.delete(0, tk.END)
                widget.config(state=current_state)

    def handle_update(self, publisher_id: str, updates: dict) -> bool:
        """Update a publisher's information."""
        try:
            if not publisher_id:
                messagebox.showerror("Error", "Publisher ID is required for updating.")
                return False

            self.service.update_publisher(publisher_id, updates)
            messagebox.showinfo("Success", "Publisher updated successfully!")
            return True
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update publisher: {str(e)}")
            return False

    def handle_delete(self, publisher_id: str) -> bool:
        """Delete a publisher."""
        try:
            if not publisher_id:
                messagebox.showerror(
                    "Error", "Please provide a Publisher ID to delete."
                )
                return False

            confirm = messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete publisher with ID: {publisher_id}?",
            )

            if not confirm:
                return False

            self.service.delete_publisher(publisher_id)
            messagebox.showinfo("Success", "Publisher deleted successfully!")
            return True
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete publisher: {str(e)}")
            return False

    def get_all_publishers(self) -> list:
        """Get all publishers."""
        try:
            return self.service.get_all_publishers()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve publishers: {str(e)}")
            return []

    def search_publishers(self, **criteria) -> list:
        """Search for publishers by criteria."""
        try:
            return self.service.search_publishers(**criteria)
        except Exception as e:
            messagebox.showerror("Error", f"Search failed: {str(e)}")
            return []

    def hide_container(self, target: ttk.Widget) -> None:
        """Hide the container widget."""
        target.grid_remove()

    def show_container(self, target: ttk.Widget, **grid_options) -> None:
        """Show the container widget."""
        target.grid(**grid_options)
