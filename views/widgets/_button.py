from tkinter import ttk


class Button:

    def __init__(self, frame, function) -> None:
        self.frame = frame
        self.function = function

    def _add_button(self, frame, function):
        btn = ttk.Button(
            frame,
            text="Add",
            command=function,
        )

        btn.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=5,
            pady=5,
        )

    def _update_button(
        self,
        frame,
        function,
        col=1,
        row=1,
    ):
        btn = ttk.Button(
            frame,
            text="Add",
            command=function,
        )

        btn.grid(
            row=row,
            column=col,
            sticky="ew",
            padx=5,
            pady=5,
        )
