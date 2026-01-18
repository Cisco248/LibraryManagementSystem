from tkinter import ttk


class AppButton:
    def __init__(
        self,
        parent: ttk.Widget,
        text: str,
        row: int,
        column: int,
        colspan: int = 1,
    ):
        self.button = ttk.Button(
            parent,
            text=text,
        )

        self.button.grid(
            row=row,
            column=column,
            columnspan=colspan,
            sticky="ew",
            padx=5,
            pady=5,
        )
