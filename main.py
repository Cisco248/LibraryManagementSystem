from tkinter import Tk, ttk

from config.Configuration import APP_TITLE
from views.components import AppHeader
from views import BookView, AuthorView, PublisherView, MemberView
from views.components import AppFooter


class MainAppRunner:
    def __init__(self):
        self.root = Tk()
        self.root.title(APP_TITLE)

        self.root.resizable(False, False)
        self.root.update_idletasks()
        self.root.wm_minsize(800, 1000)

        AppHeader.AppHeader(self.root)

        Root = self.ContentFrame(self.root)
        second_root = self.NoteBook(Root)

        BookView(second_root).update_idletasks()
        AuthorView(second_root).update_idletasks()
        PublisherView(second_root).update_idletasks()
        MemberView(second_root).update_idletasks()

        AppFooter.AppFooter(self.root)

    def NoteBook(self, master: ttk.Frame):
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill="both", expand=True)
        return self.notebook

    def ContentFrame(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill="both", expand=True, padx=12, pady=12)
        return self.frame


def main():
    app = MainAppRunner()
    app.root.mainloop()


if __name__ == "__main__":
    main()
