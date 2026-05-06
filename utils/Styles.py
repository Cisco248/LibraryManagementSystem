from tkinter import ttk


class ListStyle:
    def __init__(self, widget: str, component: str) -> None:
        self.widget = widget
        self.component = component
        self.style = ttk.Style()

        self.style.configure(
            self.widget,
            background="white",
            foreground="black",
            rowheight=24,
            fieldbackground="white",
        )

        self.style.configure(
            f"{self.widget}.{self.component}",
            background="#a8a8a8",
            foreground="black",
            relief="flat",
            font=("Poppins", 8, "bold"),
        )

    def __map__(self):

        self.style.map(
            self.widget,
            background=[("selected", "#0078d7")],
            foreground=[("selected", "white")],
        )

        self.style.map(
            f"{self.widget}.{self.component}", background=[("active", "#e0e0e0")]
        )
