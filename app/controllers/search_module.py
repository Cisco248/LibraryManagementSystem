from tkinter import Entry, ttk
from app.services.book_management import PrintedBook
from app.helpers.container_frame import custom_container_without_label

pb = PrintedBook()


def handle_search(
    source: ttk.Entry,
    target: ttk.Label,
    parent: ttk.LabelFrame,
):
    """
    Reads ISBN from source Entry, searches the book,
    and displays the result in target Label and a new frame.
    """
    val = source.get().strip()

    if not val:
        target.config(text="Enter ISBN here")
        return

    book = pb.find_book(val)

    target.config(text=str(book))

    # Create a new frame inside parent to show book details
    frame = custom_container_without_label(parent)
    frame.grid(row=2, column=0, sticky="ew", pady=5, padx=5)
    frame.columnconfigure(0, weight=1)

    # Show book title in a read-only entry
    entry = ttk.Entry(frame, width=50, state="readonly")
    entry.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    # Insert text into read-only entry
    # title = book.get("Title", "Unknown Title")

    # entry.insert(0, book)

    # f"Title: {book}",
    # f"ISBN: {book['ISBN']}",
    # f"Author: {book['Author']}",
    # f"Category: {book['Category']}",
    # f"Status: {book['Status']}\n",
