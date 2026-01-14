import tkinter as tk
from tkinter import ttk


def custom_container_with_label(p: tk.Widget, t: str) -> ttk.LabelFrame:
    """
    Creates a labeled frame container.

    Args:
        parent (tk.Widget): The parent widget.
        title (str): The text to display on the frame border.

    Returns:
        ttk.LabelFrame: The unplaced frame widget.
    """
    frame = ttk.LabelFrame(p, text=t, padding=(10, 10))
    return frame


def custom_container_without_label(p: tk.Widget) -> ttk.Frame:
    """
    Creates a labeled frame container.

    Args:
        parent (tk.Widget): The parent widget.

    Returns:
        ttk.Frame: The unplaced frame widget.
    """
    frame = ttk.Frame(p, padding=(10, 10))
    return frame
