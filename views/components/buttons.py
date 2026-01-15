from tkinter import ttk
from views.widgets import custom_container_without_label
from views.widgets import Button


def button_toolbar(parent: ttk.Widget) -> ttk.Frame:
    """
    Create a horizontal toolbar of buttons inside a frame.

    Each button is created from a dictionary mapping button labels to their respective functions.

    Args:
        parent (ttk.Widget): The parent widget where the toolbar will be placed.
        button_data (dict): A dictionary mapping button text (str) to functions (callable).
                            Example: {"Add": self.add, "Delete": self.delete}

    Returns:
        ttk.Frame: A frame containing the buttons arranged horizontally.

    Example:
        >>> buttons = {"Add": add_book, "Delete": delete_book, "Update": update_book}
        >>> toolbar = button_toolbar(root, buttons)
        >>> toolbar.grid(row=0, column=0, sticky="ew")
    """

    frame = custom_container_without_label(parent)
    frame.columnconfigure(
        1,
        weight=1,
    )

    Button._add_button(self=dsa, frame=frame, function=(adds))

    return frame


# --- Usage Example ---
# Assuming you have your controller class from before
# controller = Button_Click_Module()

# buttons_map = {
#    "Add": controller.click_add_button,
#    "Update": controller.click_update_button,
#    "Delete": controller.click_delete_button
# }
# toolbar = button_toolbar_connected(root, buttons_map)
# toolbar.pack(fill="x")
