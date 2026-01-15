from tkinter import ttk
from views.widgets import custom_container_with_label


def details_component(
    parent: ttk.Widget,
    title: str,
    labels: list[str],
    name_list: list[str],
) -> ttk.Entry:
    """
    Generate a read-only form inside a labeled container with multiple key-value pairs.

    Each key-value pair consists of a Label (key) and a read-only Entry (value).

    Args:
        parent (ttk.Widget): The parent widget where the form will be placed.
        title (str): Title for the container frame.
        labels (list[str]): List of labels (keys) to display on the left side.
        name_list (list[str]): List of names/identifiers for each Entry widget.
                               Must be the same length as `labels`.

    Returns:
        ttk.Frame: The container frame holding all labels and read-only entries.

    Example:
        >>> labels = ["ISBN", "Title", "Author"]
        >>> names = ["isbn", "title", "author"]
        >>> frame = details_component(root, "Book Details", labels, names)
        >>> frame.grid(row=0, column=0, sticky="ew")
    """

    if len(labels) != len(name_list):
        raise ValueError("labels and name_list must have the same length")

    # Create a labeled container
    container = custom_container_with_label(parent, title)
    container.columnconfigure(1, weight=1)

    # Store references to Entry widgets in a dictionary (optional)
    entries = {}

    for i, label_text in enumerate(labels):
        # Create the label
        lbl = ttk.Label(container, text=f"{label_text}:")
        lbl.grid(row=i, column=0, sticky="w", padx=5, pady=5)

        # Create a read-only entry
        entry = ttk.Entry(
            container, width=40, state="readonly", name=name_list[i].lower()
        )
        entry.grid(row=i, column=1, sticky="ew", padx=5, pady=5)

        # Save entry reference
        entries[name_list[i]] = entry

    # Optionally, you could return the dictionary of entries if you need to update values
    # return entries

    return entry
