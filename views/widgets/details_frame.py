from tkinter import ttk


def create_detail_row(p: ttk.Widget, lt: str, r: int, n: str) -> ttk.Entry:
    """
    Creates a single row with a Label and a Read-Only Entry.

    Args:
        parent (tk.Widget): The container frame.
        label_text (str): The text for the label (e.g., "Name").
        row_index (int): The grid row number to place this widget on.

    Returns:
        ttk.Entry: The created entry widget (useful if you need to set text later).
    """

    # 1. Create and Place Label (Column 0)
    lbl = ttk.Label(p, text=f"{lt}:")
    lbl.grid(row=r, column=0, sticky="w", padx=5, pady=5)

    # 2. Create and Place Entry (Column 1)
    entry = ttk.Entry(p, width=40, state="readonly", name=n)
    entry.grid(row=r, column=1, sticky="ew", padx=5, pady=5)

    return entry
