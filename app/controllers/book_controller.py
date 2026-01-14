"""
Book Controller Module

This module contains controller classes for managing book operations in the
library management system, following the MVC architecture pattern.
"""

from tkinter import messagebox, ttk
import tkinter as tk
from models.book_model import BookModel
from repository.book_repo import BookRepository


class BookActionController:
    """
    Base controller class for handling book-related actions in a GUI.

    This class provides generic methods for adding, clearing, deleting,
    updating, and managing book detail forms in a Tkinter interface.
    It acts as a bridge between the view (UI) and the model (data/business logic).

    Attributes:
        repository: The repository instance for data persistence operations.
        view: The view instance containing UI components.

    Examples:
        >>> from repositories.book_repository import BookRepository
        >>> repository = BookRepository()
        >>> controller = BookActionController(repository)
    """

    def __init__(self, repository: BookRepository) -> None:
        """
        Initialize the BookActionController.

        Args:
            repository: Repository instance for data operations.
        """
        self.repository = repository

    def handle_add(self, target: ttk.Widget):
        """
        Collect data from entry widgets in a container and add a book.

        This method iterates through all Entry widgets in the target container,
        collects their values, creates a BookModel instance, and persists it
        using the repository.

        Args:
            target (ttk.Widget): The parent container holding the Entry widgets.

        Raises:
            ValueError: If the collected data is invalid for BookModel creation.

        Behavior:
            - Iterates through all child Entry widgets in the target.
            - Enables editing temporarily to read their values.
            - Collects values into a dictionary.
            - Creates a BookModel instance.
            - Calls repository.add_book() to persist the data.
            - Shows success or error message to the user.

        Example:
            >>> controller = BookActionController(repository)
            >>> result = controller.handle_add(book_form_frame)
        """
        try:
            book_data = {}

            for widget in target.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.config(state="normal")
                    key = widget.winfo_name()
                    value = widget.get()
                    if value:
                        book_data[key] = value

            if not book_data:
                messagebox.showerror("Error: No Data to Add. Fill the Fields")
                return None

            book_model = BookModel(**book_data)
            res = self.repository.add_book(data=book_model)

            if isinstance(res, str):
                messagebox.showerror("Error: ", res)
                return None
            else:
                messagebox.showinfo(
                    "Success", f"Book {book_model.title} Added Successfully!"
                )
                self.handle_clear(target)
                return res

        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            return None
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add book: {str(e)}")
            return None

    def handle_clear(self, target: ttk.Widget) -> None:
        """
        Clear all Entry widgets inside the given container.

        This method resets all form fields to their default empty state,
        preserving the original enabled/disabled state of each widget.

        Args:
            target (ttk.Widget): The parent frame containing Entry widgets.

        Behavior:
            - Temporarily sets each Entry to 'normal' to allow editing.
            - Deletes all text inside the Entry.
            - Restores the original Entry state.

        Example:
            >>> controller.handle_clear(book_form_frame)
        """
        for widget in target.winfo_children():
            if isinstance(widget, ttk.Entry):
                current_state = widget["state"]
                widget.config(state="normal")
                widget.delete(0, tk.END)
                widget.config(state=current_state)

    def handle_delete(self, isbn: str) -> bool:
        """
        Delete a book from the repository by ISBN.

        Args:
            isbn (str): The ISBN of the book to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.

        Example:
            >>> success = controller.handle_delete("978-0-123456-78-9")
            >>> if success:
            ...     print("Book deleted successfully")
        """
        try:
            if not isbn:
                messagebox.showerror("Error", "Please provide an ISBN to delete.")
                return False

            # Confirm deletion
            confirm = messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete the book with ISBN: {isbn}?",
            )

            if not confirm:
                return False

            result = self.repository.delete_book()

            if isinstance(result, str) and "Error" not in result:
                messagebox.showinfo("Success", result)
                return True
            else:
                messagebox.showerror(
                    "Error", result if isinstance(result, str) else "Deletion failed"
                )
                return False

        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete book: {str(e)}")
            return False

    def handle_update(self, target: ttk.Widget):
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
            book_data = {}

            # Collect data from form
            for widget in target.winfo_children():
                if isinstance(widget, ttk.Entry):
                    original_state = widget["state"]
                    widget.config(state="normal")

                    key = widget.winfo_name()
                    value = widget.get().strip()

                    widget.config(state=original_state)

                    if value:
                        book_data[key] = value

            # ISBN is required for update
            if "isbn" not in book_data:
                messagebox.showerror("Error", "ISBN is required for updating a book.")
                return None

            isbn = book_data.pop("isbn")  # Remove ISBN from update data

            # Convert numeric fields
            if "quantity" in book_data:
                book_data["quantity"] = int(book_data["quantity"])
            if "publication_year" in book_data:
                book_data["publication_year"] = int(book_data["publication_year"])

            # Update in repository
            result = self.repository.update_book(isbn, book_data)

            if isinstance(result, str):  # Error message
                messagebox.showerror("Error", result)
                return None
            else:
                messagebox.showinfo(
                    "Success", f"Book with ISBN '{isbn}' updated successfully!"
                )
                return result

        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            return None
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update book: {str(e)}")
            return None

    def handle_search(self, search_term: str) -> list:
        """
        Search for books matching the search term.

        Args:
            search_term (str): The search term (ISBN, title, or author).

        Returns:
            list: List of matching books.

        Example:
            >>> results = controller.handle_search("Python")
            >>> for book in results:
            ...     print(book['title'])
        """
        try:
            if not search_term:
                return self.repository.get_all_books()

            # Search by multiple criteria
            results = self.repository.search_book(
                isbn=search_term, title=search_term, author=search_term
            )

            return results

        except Exception as e:
            messagebox.showerror("Error", f"Search failed: {str(e)}")
            return []

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


class PrintedBookActionController(BookActionController):
    """
    Controller subclass specifically for managing printed books.

    This controller extends the base BookActionController with additional
    functionality specific to physical book management, such as checking
    availability status and updating book conditions.

    Examples:
        >>> controller = PrintedBookActionController(repository, view)
        >>> status = controller.handle_check_status("978-0-123456-78-9")
    """

    def handle_status(self, isbn: str) -> str:
        """
        Check the availability status of a printed book by ISBN.

        Args:
            isbn (str): The ISBN number of the book to check.

        Returns:
            str: A message indicating the book status or not found.

        Example:
            >>> controller.handle_check_status("978-0-123456-78-9")
            'Book is Available'
        """
        try:
            book = self.repository.get_book(isbn)

            if book:
                status = book.get("status", "unknown")
                return f"Book is {status}."

            else:
                return f"Book with ISBN {isbn} not Found"

        except Exception as e:
            return f"Error Checking Status: {str(e)}"

    def handle_update_status(self, isbn: str, new_status: str) -> str:
        """
        Update the status of a printed book.

        Args:
            isbn (str): The ISBN of the book to update.
            new_status (str): The new status (e.g., "Available", "Checked Out",
                            "Lost", "Damaged").

        Returns:
            str: Success or failure message.

        Example:
            >>> result = controller.handle_update_status("978-0-123456-78-9", "Available")
            >>> print(result)
            'Book status updated successfully!'
        """
        try:
            res = self.repository.update_book(isbn, {"status": new_status})

            if isinstance(res, str):
                return f"Book Status Update Failed!"
            else:
                messagebox.showinfo("Success", "Book Status Update Successfully!")
                return "Book Status Update Successfully!"

        except Exception as e:
            messagebox.showerror("Error", f"Failed to Update Status: {str(e)}")
            return f"Failed to Update Status: {str(e)}"


class EBookActionController(BookActionController):
    """
    Controller subclass specifically for managing e-books.

    This controller extends the base BookActionController with additional
    functionality specific to electronic book management, such as file
    downloads, format validation, and file size tracking.

    Examples:
        >>> controller = EBookActionController(repository, view)
        >>> controller.handle_download("978-0-123456-78-9")
    """

    def handle_add_ebook(self, target: ttk.Widget):
        """
        Add an e-book with additional electronic-specific validation.

        Args:
            target (ttk.Widget): The parent container holding the Entry widgets.

        Returns:
            Optional[BookModel]: The added BookModel instance if successful.

        Example:
            >>> result = controller.handle_add_ebook(ebook_form_frame)
        """
        try:
            pass
        except Exception as e:
            pass

    def handle_e_book_get(self, isbn: str):
        """
        Retrieve e-book data by ISBN.

        Args:
            isbn (str): The ISBN of the e-book to retrieve.

        Returns:
            Optional[Dict[str, Any]]: E-book data if found, None otherwise.

        Example:
            >>> ebook = controller.handle_get_ebook("978-0-123456-78-9")
            >>> if ebook:
            ...     print(f"Format: {ebook.get('file_format')}")
        """
        try:
            pass
        except:
            pass

    def handle_download(self, isbn: str, download_path: str):
        """
        Handle downloading an e-book file.

        Args:
            isbn (str): The ISBN of the e-book to download.
            download_path (str, optional): The path where the file should be saved.

        Returns:
            bool: True if download was successful, False otherwise.

        Example:
            >>> success = controller.handle_download("978-0-123456-78-9", "/downloads/")
            >>> if success:
            ...     print("Download complete!")
        """
        try:
            pass
        except:
            pass

    def handle_get_file_size(self, isbn: str):
        """
        Get the file size of an e-book.

        Args:
            isbn (str): The ISBN of the e-book.

        Returns:
            Optional[str]: Formatted file size string (e.g., "5.2 MB"), None if not found.

        Example:
            >>> size = controller.handle_get_file_size("978-0-123456-78-9")
            >>> print(f"File size: {size}")
        """
        try:
            pass
            # book = self.repository.get_book(isbn)

            # if book and "file_size" in book:
            #     file_size = book["file_size"]
            #     return f"{file_size} MB"
            # else:
            #     return "Size unknown"

        except Exception as e:
            pass
            # messagebox.showerror("Error", f"Failed to get file size: {str(e)}")
            # return None
