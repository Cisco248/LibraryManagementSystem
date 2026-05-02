from tkinter import ttk
from config.Configuration import APP_FOOTER_TEXT_1, APP_FOOTER_TEXT_2


class AppFooter(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="both", padx=12)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.text1 = ttk.Label(
            self,
            text=APP_FOOTER_TEXT_1,
            font=("Poppins", 10),
            justify="left",
        )
        self.text1.grid(column=0, row=0, columnspan=1, sticky="ew")

        self.text2 = ttk.Label(
            self,
            text=APP_FOOTER_TEXT_2,
            font=("Poppins", 8),
            justify="center",
            anchor="e",
        )
        self.text2.grid(column=1, row=0, columnspan=1, sticky="ew")
