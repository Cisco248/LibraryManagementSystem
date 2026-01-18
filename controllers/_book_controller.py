"""
Book Controller Module

This module contains controller classes for managing book operations in the
library management system, following the MVC architecture pattern.
"""

from ._basic_crud import BookActionController


class PrintedBookActionController(BookActionController):
    """
    Controller subclass specifically for managing printed books.

    This controller extends the base BookActionController with additional
    functionality specific to physical book management, such as checking
    availability status and updating book conditions.

    Examples:
        >>> controller = PrintedBookActionController()
        >>> status = controller.handle_update_status("978-0-123456-78-9", "Available")
    """

    # def handle_update_status(self, isbn: str, new_status: str) -> str:
    #     """
    #     Update the status of a printed book.

    #     Args:
    #         isbn (str): The ISBN of the book to update.
    #         new_status (str): The new status (e.g., "Available", "Checked Out",
    #                         "Lost", "Damaged").

    #     Returns:
    #         str: Success or failure message.

    #     Example:
    #         >>> result = controller.handle_update_status("978-0-123456-78-9", "Available")
    #         >>> print(result)
    #         'Book status updated successfully!'
    #     """
    #     try:
    #         res = self.repository.update_book(isbn, {"status": new_status})

    #         if isinstance(res, str):
    #             return "Book Status Update Failed!"
    #         else:
    #             messagebox.showinfo("Success", "Book Status Updated Successfully!")
    #             return "Book Status Updated Successfully!"

    #     except Exception as e:
    #         messagebox.showerror("Error", f"Failed to Update Status: {str(e)}")
    #         return f"Failed to Update Status: {str(e)}"


class EBookActionController(BookActionController):
    """
    Controller subclass specifically for managing e-books.

    This controller extends the base BookActionController with additional
    functionality specific to electronic book management, such as file
    downloads, format validation, and file size tracking.

    Examples:
        >>> controller = EBookActionController()
        >>> size = controller.handle_get_file_size("978-0-123456-78-9")
    """

    # def handle_get_file_size(self, isbn: str):
    #     """
    #     Get the file size of an e-book.

    #     Args:
    #         isbn (str): The ISBN of the e-book.

    #     Returns:
    #         Optional[str]: Formatted file size string (e.g., "5.2 MB"), None if not found.

    #     Example:
    #         >>> size = controller.handle_get_file_size("978-0-123456-78-9")
    #         >>> print(f"File size: {size}")
    #     """
    #     try:
    #         book = self.repository.get_book(isbn)

    #         if book and "file_size" in book:
    #             file_size = book["file_size"]
    #             return f"{file_size} MB"
    #         else:
    #             return "Size unknown"

    #     except Exception as e:
    #         messagebox.showerror("Error", f"Failed to get file size: {str(e)}")
    #         return None
