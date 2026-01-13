class BookManagement:
    """
    Module: BookManagement

    This module handles book-related operations, such as searching for books,
    displaying book details, and managing printed and e-books.

    Manages books by providing functionality to search, display, and update books.
    """

    def __init__(self):
        """
        Initializes an instance of the BookManagement class with an empty book list.
        """
        self.books = []

    def get_book_details(self) -> str | list[str]:
        """
        Displays details of all books in the library.

        Returns:
            list: A list of book dictionaries or an empty list if no books exist.
        """
        print("\n========== All Book Details ==========")
        if not self.books:
            return "Library is Empty."
        for book in self.books:
            print(
                f"Title: {book['Title']}\nISBN: {book['ISBN']}\nAuthor: {book['Author']}\n"
                f"Category: {book['Category']}\nStatus: {book['Status']}\n"
            )
        return self.books

    def add_book(self, book_data: dict[str, str]) -> str:
        """
        Adds a book to the library.

        Args:
            book_data (dict): A dictionary containing book details.

        Returns:
            str: Success or error message.
        """
        print("\n========== Add Book ==========")
        if (book["isbn"] == book_data["isbn"] for book in self.books):
            return f"Error: Book with ISBN '{book_data['isbn']}' already exists."
        self.books.append(book_data)
        return f"Book '{book_data['title']}' added successfully!"

    def delete_book(self, isbn: str) -> str:
        """
        Deletes a book from the library.

        Args:
            isbn (str): The ISBN of the book to delete.

        Returns:
            str: Success or error message.
        """
        print("\n========== Delete Book ==========")
        for book in self.books:
            if book["ISBN"] == isbn:
                self.books.remove(book)
                return f"Book with ISBN '{isbn}' deleted successfully."
        return f"Error: Book with ISBN '{isbn}' not found."

    def update_book_details(self, isbn: str, updated_data: dict[str, str]) -> str:
        """
        Updates details of a specific book.

        Args:
            isbn (str): The ISBN of the book to update.
            updated_data (dict): A dictionary containing updated book details.

        Returns:
            str: Success or error message.
        """
        print("\n========== Update Book ==========")
        for book in self.books:
            if book["ISBN"] == isbn:
                book.update(
                    {key: value for key, value in updated_data.items() if value}
                )
                return f"Book with ISBN '{isbn}' updated successfully."
        return f"Error: Book with ISBN '{isbn}' not found."

    def find_book(self, isbn: str) -> dict | str:
        """
        Finds a book by ISBN.

        Args:
            isbn (str): The ISBN of the book to find.

        Returns:
            dict | None: Book details if found, or None if not found.
        """
        print("\n========== Find Book ==========")
        for book in self.books:
            if book["ISBN"] == isbn:
                print(
                    f"Title: {book['Title']}",
                    f"ISBN: {book['ISBN']}",
                    f"Author: {book['Author']}",
                    f"Category: {book['Category']}",
                    f"Status: {book['Status']}\n",
                )
                return book
        return f"Error: Book with ISBN '{isbn}' not found."


class PrintedBook(BookManagement):
    """
    Manages printed books with additional features to check and update status.
    """

    def check_status(self, t: str) -> str:
        """
        Checks the availability status of a printed book.

        Args:
            t (str): The title of the book.

        Returns:
            str: Status of the book or an error message if the book is not found.
        """
        print("\n========== Check Book Status ==========")
        for book in self.books:
            if book["Title"] == t:
                return f"Title: {book['Title']}\nStatus: {book['Status']}"
        return f"Error: Book with title '{t}' not found."

    def update_status(self, title: str, next_status: str) -> str:
        """
        Updates the status of a printed book.

        Args:
            title (str): The title of the book.
            next_status (str): The new status of the book.

        Returns:
            str: Success message or an error message if the book is not found.
        """
        print("\n========== Update Book Status ==========")
        for book in self.books:
            if book["Title"] == title:
                if book["Status"] != next_status:
                    book["Status"] = next_status
                    return f"Title: {title}\nStatus updated to: {next_status}"
                return f"Error: Status of '{title}' is already '{next_status}'."
        return f"Error: Book with title '{title}' not found."


class Ebook(BookManagement):
    """
    Manages e-books with additional features to handle download links and file sizes.
    """

    def add_ebook(self, data: dict[str, str]) -> str:
        """
        Adds an e-book to the library.

        Args:
            data (dict): A dictionary containing e-book details.

        Returns:
            str: Success or error message.
        """
        print("\n========== Add E-Book ==========")
        if any(ebook["ISBN"] == data["ISBN"] for ebook in self.books):
            return f"Error: E-Book with ISBN '{data['ISBN']}' already exists."
        self.books.append(data)
        return f"E-Book '{data['Title']}' added successfully!"

    def get_ebook_details(self) -> str | list[str]:
        """
        Displays details of all e-books.

        Returns:
            list: A list of e-book details or an empty list if no e-books exist.
        """
        print("\n========== All E-Book Details ==========")
        if not self.books:
            return "Library is Empty."

        for ebook in self.books:
            print(
                f"Title: {ebook['Title']}\n"
                f"ISBN: {ebook['ISBN']}\n"
                f"Author: {ebook['Author']}\n"
                f"Category: {ebook['Category']}\n"
                f"Link: {ebook['Link']}\n"
                f"Size: {ebook['Size']}\n"
            )
        return self.books

    def download(self, isbn: str) -> str:
        """
        Provides the download link for an e-book.

        Args:
            isbn (str): The ISBN of the e-book.

        Returns:
            str: Download link or an error message if not found.
        """
        print("\n========== E-Book Download Link ==========")
        for ebook in self.books:
            if ebook["ISBN"] == isbn:
                return f"Title: {ebook['Title']}\nDownload Link: {ebook['Link']}"
        return f"Error: E-Book with ISBN '{isbn}' not found."

    def get_file_size(self, isbn: str) -> str:
        """
        Retrieves the file size of an e-book.

        Args:
            isbn (str): The ISBN of the e-book.

        Returns:
            str: File size or an error message if not found.
        """
        print("\n========== E-Book Size ==========")
        for ebook in self.books:
            if ebook["ISBN"] == isbn:
                return f"Title: {ebook['Title']}\nFile Size: {ebook['Size']}"
        return f"Error: E-Book with ISBN '{isbn}' not found."
