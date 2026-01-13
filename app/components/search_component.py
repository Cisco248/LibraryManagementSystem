import tkinter as tk
from tkinter import ttk
from app.helpers.container_frame import custom_container_with_label
from app.modules.search_module import handle_search


def search_component(
    parent: tk.Widget,
    title: str,
    button_text: str,
    label_text: str,
) -> ttk.LabelFrame:
    """
    Creates a responsive search bar component.

    Layout: [Label] [Input Field ------------------] [Button]

    Args:
        p (tk.Widget): The parent widget.
        t (str): Text for the container frame border.
        bt (str): Text to display on the action button.
        lt (str): Text to display before the input field.

    Returns:
        ttk.LabelFrame: The container widget (unplaced).
    """

    frame = custom_container_with_label(
        parent,
        title,
    )
    frame.columnconfigure(
        1,
        weight=1,
    )

    ttk.Label(
        frame,
        text=label_text,
    ).grid(
        row=0,
        column=0,
        padx=(10, 5),
        pady=10,
        sticky="w",
    )

    entry = ttk.Entry(frame)
    entry.grid(
        row=0,
        column=1,
        padx=5,
        pady=10,
        sticky="ew",
    )

    result_label = ttk.Label(
        frame,
        text="Find Book Entering ISBN",
    )
    result_label.grid(
        row=1,
        column=0,
        columnspan=3,
        padx=10,
        pady=(0, 10),
        sticky="w",
    )

    ttk.Button(
        frame,
        text=button_text,
        command=lambda: handle_search(
            source=entry,
            target=result_label,
            parent=frame,
        ),
    ).grid(
        row=0,
        column=2,
        padx=(5, 10),
        pady=10,
    )

    return frame
