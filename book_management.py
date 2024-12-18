"""
Module: BookManagement

This module handles book-related operations, such as searching for books,
displaying book details, and managing printed and e-books.
"""

class BookManagement:
    """
    Manages books by providing functionality to search, display, and update books.
    """
    def __init__(self):
        """
        Initializes an instance of the BookManagement class with an empty book list.
        """
        self.books = []

    def get_book_details(self):
        """
        Displays details of all books in the library.

        Returns:
            list: A list of book dictionaries or an empty list if no books exist.
        """
        print("\n========== All Book Details ==========")
        if not self.books:
            print("Library is Empty.")
            return []
        for book in self.books:
            print(f"Title: {book['Title']}\nISBN: {book['ISBN']}\nAuthor: {book['Author']}\n"
                  f"Category: {book['Category']}\nStatus: {book['Status']}\n")
        return self.books

    def add_book(self, book_data):
        """
        Adds a book to the library.

        Args:
            book_data (dict): A dictionary containing book details.

        Returns:
            str: Success or error message.
        """
        print("\n========== Add Book ==========")
        if any(book['ISBN'] == book_data['ISBN'] for book in self.books):
            return f"Error: Book with ISBN '{book_data['ISBN']}' already exists."
        self.books.append(book_data)
        print(f"Book '{book_data['Title']}' added successfully!")

    def delete_book(self, isbn):
        """
        Deletes a book from the library.

        Args:
            isbn (str): The ISBN of the book to delete.

        Returns:
            str: Success or error message.
        """
        print("\n========== Delete Book ==========")
        for book in self.books:
            if book['ISBN'] == isbn:
                self.books.remove(book)
                print(f"Book with ISBN '{isbn}' deleted successfully.")
        return(f"Error: Book with ISBN '{isbn}' not found.")

    def update_book_details(self, isbn, updated_data):
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
            if book['ISBN'] == isbn:
                book.update({key: value for key, value in updated_data.items() if value})
                print(f"Book with ISBN '{isbn}' updated successfully.")
        return(f"Error: Book with ISBN '{isbn}' not found.")

    def find_book(self, isbn):
        """
        Finds a book by ISBN.

        Args:
            isbn (str): The ISBN of the book to find.

        Returns:
            dict: Book details if found, or None if not found.
        """
        print("\n========== Find Book ==========")
        for book in self.books:
            if book['ISBN'] == isbn:
                print(f"Title: {book['Title']}\nISBN: {book['ISBN']}\nAuthor: {book['Author']}\n"
                      f"Category: {book['Category']}\nStatus: {book['Status']}\n")
                return book
        print(f"Error: Book with ISBN '{isbn}' not found.")
        return None


class PrintedBook(BookManagement):
    """
    Manages printed books with additional features to check and update status.
    """

    def check_status(self, title):
        """
        Checks the availability status of a printed book.

        Args:
            title (str): The title of the book.

        Returns:
            str: Status of the book or an error message if the book is not found.
        """
        print("\n========== Check Book Status ==========")
        for book in self.books:
            if book['Title'] == title:
                print(f"Title: {book['Title']}\nStatus: {book['Status']}")
                return
        print(f"Error: Book with title '{title}' not found.")

    def update_status(self, title, next_status):
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
            if book['Title'] == title:
                if book['Status'] != next_status:
                    book['Status'] = next_status
                    print(f"Title: {title}\nStatus updated to: {next_status}")
                    return
                print(f"Error: Status of '{title}' is already '{next_status}'.")
                return
        print(f"Error: Book with title '{title}' not found.")
        return


class Ebook(BookManagement):
    """
    Manages e-books with additional features to handle download links and file sizes.
    """

    def add_ebook(self, ebook_data):
        """
        Adds an e-book to the library.

        Args:
            ebook_data (dict): A dictionary containing e-book details.

        Returns:
            str: Success or error message.
        """
        print("\n========== Add E-Book ==========")
        if any(ebook['ISBN'] == ebook_data['ISBN'] for ebook in self.books):
            return f"Error: E-Book with ISBN '{ebook_data['ISBN']}' already exists."
        self.books.append(ebook_data)
        print(f"E-Book '{ebook_data['Title']}' added successfully!")

    def get_ebook_details(self):
        """
        Displays details of all e-books.

        Returns:
            list: A list of e-book details or an empty list if no e-books exist.
        """
        print("\n========== All E-Book Details ==========")
        if not self.books:
            print("Library is Empty.")
            return []
        for ebook in self.books:
            print(f"Title: {ebook['Title']}\nISBN: {ebook['ISBN']}\nAuthor: {ebook['Author']}\n"
                  f"Category: {ebook['Category']}\nLink: {ebook['Link']}\nSize: {ebook['Size']}\n")
        return self.books

    def download(self, isbn):
        """
        Provides the download link for an e-book.

        Args:
            isbn (str): The ISBN of the e-book.

        Returns:
            str: Download link or an error message if not found.
        """
        print("\n========== E-Book Download Link ==========")
        for ebook in self.books:
            if ebook['ISBN'] == isbn:
                print(f"Title: {ebook['Title']}\nDownload Link: {ebook['Link']}")
                return
        print(f"Error: E-Book with ISBN '{isbn}' not found.")
        return

    def get_file_size(self, isbn):
        """
        Retrieves the file size of an e-book.

        Args:
            isbn (str): The ISBN of the e-book.

        Returns:
            str: File size or an error message if not found.
        """
        print("\n========== E-Book Size ==========")
        for ebook in self.books:
            if ebook['ISBN'] == isbn:
                print(f"Title: {ebook['Title']}\nFile Size: {ebook['Size']}")
                return
        print(f"Error: E-Book with ISBN '{isbn}' not found.")
        return
