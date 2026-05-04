from tkinter import ttk
from typing import Callable, Optional

from config.Configuration import COLUMN_TITLES
from utils.BarcodeScanner import BarCodeScanner


class ButtonToolBar(ttk.LabelFrame):
    def __init__(self, title: str, parent: ttk.Widget, **kwargs):
        super().__init__(parent, text=title, padding=(0, 8))
        self.kwargs = kwargs
        self.scanner = BarCodeScanner("books.csv", column_titles=COLUMN_TITLES)

        for i in range(7):
            self.columnconfigure(i, weight=1)
        self.rowconfigure(0, weight=1)

        self.__widget__()
        self.__layout__()

    def __widget__(self):

        self.button1 = ScanButton(
            self,
            "Scan Now!",
            self.scanner.start_scanner,
        )

        self.button2 = ttk.Button(
            self,
            text="Add Book",
            padding=(16, 4),
            command=self.kwargs.get("add_func", ""),
        )

        self.button3 = ttk.Button(
            self,
            text="Delete Book",
            padding=(16, 4),
            command=self.kwargs.get("del_func", ""),
        )

        self.button4 = ttk.Button(
            self,
            text="Update Book",
            padding=(16, 4),
            command=self.kwargs.get("update_func", ""),
        )

        self.button5 = ttk.Button(
            self,
            text="Clear All",
            padding=(16, 4),
            command=self.kwargs.get("clear_func", ""),
        )

        self.button6 = ttk.Button(
            self,
            text="Import Data",
            padding=(16, 4),
            command=self.kwargs.get("import_func", ""),
        )

        self.button7 = ttk.Button(
            self,
            text="Export Data",
            padding=(16, 4),
            command=self.kwargs.get("export_func", ""),
        )

    def __layout__(self):
        self.button1.grid(row=0, column=0, padx=4, pady=4)
        self.button2.grid(row=0, column=1, padx=4, pady=4)
        self.button3.grid(row=0, column=2, padx=4, pady=4)
        self.button4.grid(row=0, column=3, padx=4, pady=4)
        self.button5.grid(row=0, column=4, padx=4, pady=4)
        self.button6.grid(row=0, column=5, padx=4, pady=4)
        self.button7.grid(row=0, column=6, padx=4, pady=4)


class MiniButtonBar(ttk.Frame):

    def __init__(
        self,
        parent,
        button_1_name,
        button_2_name,
        barrow: Optional[Callable] = None,
        return_back: Optional[Callable] = None,
    ):
        super().__init__(parent)
        self.pack(fill="x", padx=12, pady=6)

        for col in range(2):
            self.columnconfigure(col, weight=1)

        self.button1 = ttk.Button(
            self,
            text=button_1_name,
            padding=(16, 4),
            command=barrow if barrow else lambda: None,
        )
        self.button1.grid(row=0, column=0, padx=4, pady=4)

        self.button2 = ttk.Button(
            self,
            text=button_2_name,
            padding=(16, 4),
            command=return_back if return_back else lambda: None,
        )
        self.button2.grid(row=0, column=1, padx=4, pady=4)


class ScanButton(ttk.Frame):

    def __init__(
        self,
        parent,
        button_name,
        func_name: Optional[Callable],
    ):
        super().__init__(parent)

        self.columnconfigure(1, weight=1)

        self.button1 = ttk.Button(
            self,
            text=button_name,
            padding=(16, 4),
            command=func_name if func_name else lambda: None,
        )
        self.button1.grid(row=0, column=0, padx=4, pady=4)
