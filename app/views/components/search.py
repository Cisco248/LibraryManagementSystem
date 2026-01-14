import tkinter as tk
from tkinter import ttk
from ..widgets.container import custom_container_with_label
from controllers import handle_search


def search_component(
    parent: tk.Widget,
    title: str,
    button_text: str,
    label_text: str,
) -> ttk.LabelFrame:
    """
    Create a reusable search bar component for Tkinter GUIs.

    The layout is as follows:
        [Label] [Entry ------------------] [Button]
        [Result Label (span across columns)]

    Args:
        parent (tk.Widget): The parent widget where this component will be placed.
        title (str): The title for the container LabelFrame.
        button_text (str): Text to display on the search/action button.
        label_text (str): Text to display next to the input field.

    Returns:
        ttk.LabelFrame: A LabelFrame containing the search entry, button, and result label.
                        It is returned unplaced, so the caller can grid/pack/place it.

    Example:
        >>> frame = search_component(root, "Book Search", "Search", "ISBN:")
        >>> frame.grid(row=0, column=0, sticky="ew")
    """

    frame = custom_container_with_label(parent, title)

    frame.columnconfigure(1, weight=1)

    ttk.Label(frame, text=label_text).grid(
        row=0, column=0, padx=(10, 5), pady=10, sticky="w"
    )

    entry = ttk.Entry(frame)
    entry.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

    result_label = ttk.Label(frame, text="Find Book Entering ISBN")
    result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 10), sticky="w")

    ttk.Button(
        frame,
        text=button_text,
        command=lambda: handle_search(
            source=entry,
            target=result_label,
            parent=frame,
        ),
    ).grid(row=0, column=2, padx=(5, 10), pady=10)

    return frame
