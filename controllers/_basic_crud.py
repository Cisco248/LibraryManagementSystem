from abc import ABC
import tkinter as tk
from tkinter import messagebox, ttk


class BookActionController(ABC):

    def __init__(self):
        self.books = []
        # self.repository = repository

    def handle_add(self, data: dict):
        """
        Add a book to the repository.

        This method creates a BookModel instance from the provided data
        and persists it using the repository.

        Args:
            data (dict): Dictionary containing book information.

        Returns:
            Optional[BookModel]: The added book if successful, None otherwise.

        Raises:
            ValueError: If the collected data is invalid for BookModel creation.

        Example:
            >>> controller = BookActionController()
            >>> result = controller.handle_add({'isbn': '978-0-123456-78-9', 'title': 'Python 101'})
        """
        try:
            book = {
                "ISBN": data["isbn"],
                "Title": data["title"],
                "Author": data["author"],
                "Publisher": data["publisher"],
                "Publication Year": data["publication_year"],
                "Book Type": data["book_type"],
                "Status": data["status"],
                "File Format": data["file_format"],
                "File Size": data["file_size"],
            }
            return f"{book['Title']} Added Successfully!"

        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            return None
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add book: {str(e)}")
            return None

    def handle_update(self, isbn: str):
        """
        Update book data from form entries.

        Collects data from the form and updates the book record in the repository.

        Args:
            target (ttk.Widget): The container of book entries to update.

        Returns:
            Optional[Dict[str, Any]]: Updated book data if successful, None otherwise.

        Example:
            >>> updated_book = controller.handle_update(book_form_frame)
            >>> if updated_book:
            ...     print(f"Updated: {updated_book['title']}")
        """
        try:
            # for widget in target.winfo_children():
            #     if isinstance(widget, ttk.Entry):
            #         original_state = widget["state"]
            #         widget.config(state="normal")

            #         key = widget.winfo_name()
            #         value = widget.get().strip()

            #         widget.config(state=original_state)

            if not isbn:
                return ValueError("ISBN is required for updating a book.")

            for book in self.books:
                if book["isbn"] == isbn:
                    print(f"Book with ISBN {isbn} updated successfully.")
                    return f"Book with ISBN {isbn} updated successfully."
                print(f"Book with ISBN: {isbn} Not Found.")
                # return messagebox.showerror(
                #     "Error", "ISBN is required for updating a book."
                # )

            # # Convert numeric fields
            # if "quantity" in book_data:
            #     book_data["quantity"] = int(book_data["quantity"])
            # if "publication_year" in book_data:
            #     book_data["publication_year"] = int(book_data["publication_year"])

            # # Update in repository
            # result = self.repository.update_book(isbn, book_data)

            # if isinstance(result, str):  # Error message
            #     messagebox.showerror("Error", result)
            #     return None
            # else:
            #     messagebox.showinfo(
            #         "Success", f"Book with ISBN '{isbn}' updated successfully!"
            #     )
            #     return result

        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            print(e)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update book: {str(e)}")
            print(e)

    def hide_container(self, target: ttk.Widget) -> None:
        """
        Hide the container widget without destroying it.

        This method removes the widget from the grid layout manager,
        making it invisible but preserving its state for later retrieval.

        Args:
            target (ttk.Widget): The widget to hide from the layout.

        Example:
            >>> controller.hide_container(details_frame)
        """
        target.grid_remove()

    def show_container(self, target: ttk.Widget, **grid_options) -> None:
        """
        Show a previously hidden container widget.

        Args:
            target (ttk.Widget): The widget to show in the layout.
            **grid_options: Grid layout options (row, column, padx, pady, etc.).

        Example:
            >>> controller.show_container(details_frame, row=2, column=0, padx=10)
        """
        target.grid(**grid_options)
