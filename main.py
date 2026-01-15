from tkinter import Tk, ttk
from views import books, members, authors, publishers


def main():

    root = Tk()
    root.title("Library Management System")
    root.resizable(width=False, height=False)

    tabs = ttk.Notebook(root)
    tabs.pack(pady=10, expand=True, fill="both")

    book = ttk.Frame(tabs)
    tabs.add(book, text="Books")
    books.create_book_interface(book)

    member = ttk.Frame(tabs)
    tabs.add(member, text="Members")
    members.member_management_gui(member)

    author = ttk.Frame(tabs)
    tabs.add(author, text="Authors")
    authors.author_management_gui(author)

    pub = ttk.Frame(tabs)
    tabs.add(pub, text="Publishers")
    publishers.publisher_management_gui(pub)

    root.mainloop()


if __name__ == "__main__":

    main()
