"""Book form component"""

from tkinter import ttk
import tkinter as tk
from ..widgets import DetailRow


class BookForm(tk.LabelFrame):

    def __init__(self, command):
        super().__init__(self)

