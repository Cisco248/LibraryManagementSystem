from tkinter import ttk
import tkinter as tk
from typing import Any, Dict


class DetailRow(ttk.Frame):
    """
    A single row representing one data field (Label + Read-only Entry).
    """

    def __init__(self, parent: ttk.Widget, label: str, field_name: str):
        super().__init__(parent)

        self.columnconfigure(1, weight=1)

        self.value_var = tk.StringVar(value=label)
        self.entry = ttk.Entry(
            self,
            width=40,
            state="readonly",
            name=field_name,
            textvariable=self.value_var,
        )
        self.entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

    def _get_value(self):
        return self.entry.get()

    def _set_value(self, name, value):
        self.name = name
        self.value = value
        return self.entry.setvar(self.name, self.value)


class BookDetailsForm(ttk.LabelFrame):
    """
    A container displaying the full list of book details.
    """

    def __init__(self, parent: ttk.Widget, title: str = "Book Details"):
        super().__init__(parent, text=title)
        self.columnconfigure(0, weight=1)

        # Configuration: Label Text mapped to Internal Name
        # Using a list of tuples guarantees order
        self.field_config = [
            ("ISBN:", "isbn"),
            ("Title:", "title"),
            ("Author:", "author"),
            ("Publisher:", "publisher"),
            ("Year:", "publication_year"),
            ("Type:", "book_type"),
            ("Status:", "status"),
            ("File Format:", "file_format"),
            ("File Size:", "file_size"),
        ]

        self.rows: Dict[str, DetailRow] = {}

        # Dynamically generate rows based on config
        for idx, (label_text, field_name) in enumerate(self.field_config):
            row = DetailRow(self, label_text, field_name)
            row.grid(row=idx, column=0, sticky="ew", pady=2, padx=5)

            # Store reference to access it later by name
            self.rows[field_name] = row

    def load_data(self, data: Dict[str, Any]):
        """
        Populate the form with a dictionary of data.
        Keys in 'data' must match the internal names (isbn, title, etc).
        """
        for key, value in data.items():
            if key in self.rows:
                self.rows[key]._set_value(value=value, name=key)
            else:
                print(f"Warning: Data key '{key}' has no corresponding field.")

    def clear_form(self):
        """Clear all fields."""
        for row in self.rows.values():
            row._set_value(value="", name=row.keys)


# def details_component(
#     parent: ttk.Widget, title: str, labels: list[str], name_list: list[str]
# ) -> ttk.Entry:
#     """
#     Generate a read-only form inside a labeled container with multiple key-value pairs.

#     Each key-value pair consists of a Label (key) and a read-only Entry (value).

#     Args:
#         parent (ttk.Widget): The parent widget where the form will be placed.
#         title (str): Title for the container frame.
#         labels (list[str]): List of labels (keys) to display on the left side.
#         name_list (list[str]): List of names/identifiers for each Entry widget.
#                                Must be the same length as `labels`.

#     Returns:
#         ttk.Frame: The container frame holding all labels and read-only entries.

#     Example:
#         >>> labels = ["ISBN", "Title", "Author"]
#         >>> names = ["isbn", "title", "author"]
#         >>> frame = details_component(root, "Book Details", labels, names)
#         >>> frame.grid(row=0, column=0, sticky="ew")
#     """

#     if len(labels) != len(name_list):
#         raise ValueError("labels and name_list must have the same length")

#     # Create a labeled container
#     container = custom_container_with_label(parent, title)
#     container.columnconfigure(1, weight=1)

#     # Store references to Entry widgets in a dictionary (optional)
#     entries = {}

#     for i, label_text in enumerate(labels):
#         # Create the label
#         lbl = ttk.Label(container, text=f"{label_text}:")
#         lbl.grid(row=i, column=0, sticky="w", padx=5, pady=5)

#         # Create a read-only entry
#         entry = ttk.Entry(
#             container, width=40, state="readonly", name=name_list[i].lower()
#         )
#         entry.grid(row=i, column=1, sticky="ew", padx=5, pady=5)

#         # Save entry reference
#         entries[name_list[i]] = entry

#     # Optionally, you could return the dictionary of entries if you need to update values
#     # return entries

#     return entry
