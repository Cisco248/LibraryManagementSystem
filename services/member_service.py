from tkinter import messagebox, ttk
import tkinter as tk
from models._member_model import MemberModel
from repository._member_repo import MemberRepository


class MemberActionController:

    def __init__(self):
        self.repository = MemberRepository()

    def handle_get_one(self, **criteria):
        try:
            return self.repository.search(**criteria)
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_get_all(self):
        try:
            return self.repository.get_all()
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_add(self, data: MemberModel) -> str:
        try:
            res = self.repository.add(data)
            return messagebox.showinfo("Member Added", f"{res}")
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_update(self, member_id: str, updates: dict) -> str:
        try:
            if not member_id:
                return messagebox.showwarning(
                    "Warning", "Member ID is required for updating."
                )
            res = self.repository.update(member_id, updates)
            return messagebox.showinfo("Member Updated", f"{res}")
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_delete(self, member_id: str) -> str:
        try:
            if not member_id:
                return messagebox.showerror(
                    "Error", "Please provide a Member ID to delete."
                )

            confirm = messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete member with ID: {member_id}?",
            )

            if not confirm:
                return messagebox.showwarning("Cancelled", "Member deletion cancelled.")

            res = self.repository.delete(member_id)
            return messagebox.showinfo("Member Deleted", f"{res}")
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")
