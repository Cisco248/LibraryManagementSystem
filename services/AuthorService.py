from tkinter import messagebox
from models.AuthorModel import AuthorModel
from repository.AuthorRepository import AuthorRepository
from services._service_class import Controller


class AuthorActionController(Controller):

    def __init__(self):
        self.repository = AuthorRepository()

    def handle_get_one(self, author_id: str) -> AuthorModel | str:
        try:
            return self.repository.get_one(author_id)
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_get_all(self) -> list | str:
        try:
            return self.repository.get_all()
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_add(self, data: AuthorModel) -> str:
        try:
            res = self.repository.add(data)
            return messagebox.showinfo("Author Added", f"{res}")
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_update(self, author_id: str, updates: dict) -> str:
        try:
            if not author_id:
                return messagebox.showwarning(
                    "Warning", "Author ID is required for updating."
                )
            res = self.repository.update(author_id, updates)
            return messagebox.showinfo("Author Updated", f"{res}")
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_delete(self, author_id: str):
        try:
            if not author_id:
                return messagebox.showwarning(
                    "Warning", "Please provide an Author ID to delete."
                )
            confirm = messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete author with ID: {author_id}?",
            )

            if not confirm:
                return messagebox.showwarning("Warning", "Discard deletion.")

            res = self.repository.delete(author_id)
            return messagebox.showinfo("Author Deleted", f"{res}")
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")
