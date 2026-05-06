from tkinter import messagebox
from models.PublisherModel import PublisherModel
from repository.PublisherRepository import PublisherRepository


class PublisherActionController:
    def __init__(self):
        self.repository = PublisherRepository()

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

    def handle_get_all(self):
        try:
            return self.repository.get_all()
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_get_one(self, id):
        try:
            return self.repository.get_one(id)
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_add(self, data: PublisherModel) -> str:
        try:
            res = self.repository.add(data)
            return messagebox.showinfo("Publisher Added", f"{res}")
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_update(self, data: PublisherModel) -> str:
        try:
            if not data.publisher_id:
                return messagebox.showwarning(
                    "Warning", "Publisher ID is required for updating."
                )
            res = self.repository.update(data)
            return messagebox.showinfo("Publisher Updated", f"{res}")
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")

    def handle_delete(self, id: str) -> str:
        try:
            if not id:
                return messagebox.showwarning(
                    "Warning", "Please provide a Publisher ID to delete."
                )

            confirm = messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete publisher with ID: {id}?",
            )

            if not confirm:
                return messagebox.showinfo("Cancelled", "Publisher deletion cancelled.")

            res = self.repository.delete(id)
            return messagebox.showinfo("Publisher Deleted", f"{res}")
        except Exception as e:
            return messagebox.showerror("Error", f"{str(e)}")
