"""
Member Controller Module

Controller classes for managing member operations in the GUI.
"""

from tkinter import messagebox, ttk
import tkinter as tk
from services._member_service import MemberService


class MemberActionController:
    """Controller for handling member-related actions in the GUI."""

    def __init__(self):
        """Initialize the MemberActionController."""
        self.service = MemberService()

    def handle_add(self, data: dict) -> bool:
        """Add a new member."""
        try:
            self.service.add_member(data)
            messagebox.showinfo("Success", "Member added successfully!")
            return True
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add member: {str(e)}")
            return False

    def handle_clear(self, target: ttk.Widget) -> None:
        """Clear all Entry widgets in the given container."""
        for widget in target.winfo_children():
            if isinstance(widget, ttk.Entry):
                current_state = widget["state"]
                widget.config(state="normal")
                widget.delete(0, tk.END)
                widget.config(state=current_state)

    def handle_update(self, member_id: str, updates: dict) -> bool:
        """Update a member's information."""
        try:
            if not member_id:
                messagebox.showerror("Error", "Member ID is required for updating.")
                return False

            self.service.update_member(member_id, updates)
            messagebox.showinfo("Success", "Member updated successfully!")
            return True
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update member: {str(e)}")
            return False

    def handle_delete(self, member_id: str) -> bool:
        """Delete a member."""
        try:
            if not member_id:
                messagebox.showerror("Error", "Please provide a Member ID to delete.")
                return False

            confirm = messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete member with ID: {member_id}?",
            )

            if not confirm:
                return False

            self.service.delete_member(member_id)
            messagebox.showinfo("Success", "Member deleted successfully!")
            return True
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete member: {str(e)}")
            return False

    def get_all_members(self) -> list:
        """Get all members."""
        try:
            return self.service.get_all_members()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve members: {str(e)}")
            return []

    def search_members(self, **criteria) -> list:
        """Search for members by criteria."""
        try:
            return self.service.search_members(**criteria)
        except Exception as e:
            messagebox.showerror("Error", f"Search failed: {str(e)}")
            return []

    def hide_container(self, target: ttk.Widget) -> None:
        """Hide the container widget."""
        target.grid_remove()

    def show_container(self, target: ttk.Widget, **grid_options) -> None:
        """Show the container widget."""
        target.grid(**grid_options)
