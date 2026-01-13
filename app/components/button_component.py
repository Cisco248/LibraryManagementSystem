from tkinter import ttk
from app.helpers.container_frame import custom_container_without_label


def button_toolbar(p: ttk.Widget, bd: dict) -> ttk.Frame:
    """
    Args:
        button_data (dict): A map of "Label" -> Function.
                            Ex: {"Add": self.add, "Delete": self.delete}
    """
    frame = custom_container_without_label(p)

    for i, (text, func) in enumerate(bd.items()):
        frame.columnconfigure(i, weight=1)

        # We assign the specific function 'func' to this button
        btn = ttk.Button(frame, text=text, command=func)

        btn.grid(row=0, column=i, sticky="ew", padx=5, pady=5)

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
