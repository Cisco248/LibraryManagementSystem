from tkinter import messagebox
from models.MemberModel import MemberModel
from repository.MemberRepository import MemberRepository


class MemberActionController:
    def __init__(self):
        self.repository = MemberRepository()

    def handle_import(self):
        try:
            self.repository.import_data()
        except Exception as e:
            return messagebox.showerror("error", message=f"{str(e)}")

    def handle_export(self):
        try:
            self.repository.export_data()
        except Exception as e:
            return messagebox.showerror("error", message=f"{str(e)}")

    def handle_get_one(self, id):
        try:
            return self.repository.get_one(id)
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

    def handle_update(self, data: MemberModel) -> str:
        try:
            if not data.member_id:
                return messagebox.showwarning(
                    "Warning", "Member ID is required for updating."
                )
            res = self.repository.update(data)
            return messagebox.showinfo("Member Updated", f"{res}")
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_delete(self, id: str) -> str:
        try:
            if not id:
                return messagebox.showerror(
                    "Error", "Please provide a Member ID to delete."
                )
            confirm = messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete member with ID: {id}?",
            )
            if not confirm:
                return messagebox.showwarning("Cancelled", "Member deletion cancelled.")

            res = self.repository.delete(id)
            return messagebox.showinfo("Member Deleted", f"{res}")
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")
