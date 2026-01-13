from tkinter import ttk
from app.helpers.container_frame import custom_container_with_label


def details_component(
    parent: ttk.Widget, title: str, label_text: list, name_list: list[str]
) -> ttk.Entry:
    """
    Generates a read-only form with key-value pairs (Label : Entry).
    """

    # 1. Create container
    f = custom_container_with_label(parent, title)

    # 2. Grid configuration
    f.columnconfigure(1, weight=1)

    # 3. Create rows
    for i, label_text in enumerate(label_text):
        # Label
        lbl = ttk.Label(f, text=f"{label_text}:")
        lbl.grid(row=i, column=0, sticky="w", padx=5, pady=5)

        # Entry (lowercase name = Tkinter-safe)
        entry = ttk.Entry(f, width=40, state="readonly", name=name_list[i].lower())
        entry.grid(row=i, column=1, sticky="ew", padx=5, pady=5)

    return entry
