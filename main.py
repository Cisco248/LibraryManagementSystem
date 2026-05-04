from tkinter import Tk, ttk

from config.Configuration import APP_TITLE
from views.components import AppHeader
from views import BookView, AuthorView, PublisherView, MemberView
from views.components import AppFooter


class MainAppRunner:
    def __init__(self, title: str, size: tuple):
        self.root = Tk()
        self.root.title(title)

        self.root.resizable(False, False)
        self.root.state("zoomed")
        self.root.wm_minsize(size[0], size[1])

        AppHeader(self.root)

        Root = self.ContentFrame(self.root)
        second_root = self.NoteBook(Root)

        BookView(second_root)
        AuthorView(second_root)
        PublisherView(second_root)
        MemberView(second_root)

        AppFooter(self.root)
        self.root.mainloop()

    def NoteBook(self, master: ttk.Frame):
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill="both", expand=True)
        return self.notebook

    def ContentFrame(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill="both", expand=True, padx=12, pady=12)
        return self.frame


if __name__ == "__main__":
    MainAppRunner(title=APP_TITLE, size=(800, 1000))
