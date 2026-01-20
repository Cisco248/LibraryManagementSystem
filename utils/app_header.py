from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class AppHeader(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, style="Master.TFrame")
        self.style = ttk.Style()
        self.style.configure("Master.TFrame", background="#FFFFFF")
        self.pack(fill="both", anchor="center", side="top")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        image = Image.open("assets/logos/logo.jpg")
        image = image.resize((64, 64))
        self.logo_img = ImageTk.PhotoImage(image)

        self.style.configure("Header.TLabel", background="#FFFFFF")
        self.logo = ttk.Label(
            self,
            image=self.logo_img,
            style="Header.TLabel",
            anchor="center",
        )
        self.logo.grid(row=0, column=0, padx=8, columnspan=1, sticky="e")

        self.style.configure("HeaderTitle.TLabel", background="#FFFFFF")
        self.title = ttk.Label(
            self,
            text="Smart Library Management System",
            font=("Poppins", 22, "bold"),
            style="HeaderTitle.TLabel",
        )
        self.title.grid(row=0, column=1, sticky="w")
