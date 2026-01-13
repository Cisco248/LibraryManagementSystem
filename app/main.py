from tkinter import Tk, ttk

from app.views import (
    book_gui,
    member_management_gui,
    author_management_gui,
    publisher_management_gui,
)


def main():
    root = Tk()
    root.title("Library Management System")
    root.resizable(width=False, height=False)

    tabs = ttk.Notebook(root)
    tabs.pack(pady=10, expand=True, fill="both")

    book = ttk.Frame(tabs)
    tabs.add(book, text="Books")
    book_gui(book)

    member = ttk.Frame(tabs)
    tabs.add(member, text="Members")
    member_management_gui(member)

    author = ttk.Frame(tabs)
    tabs.add(author, text="Authors")
    author_management_gui(author)

    pub = ttk.Frame(tabs)
    tabs.add(pub, text="Publishers")
    publisher_management_gui(pub)

    root.mainloop()


if __name__ == "__main__":
    main()
