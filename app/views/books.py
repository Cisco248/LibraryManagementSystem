from app.components import search_component, details_component, button_toolbar
from tkinter import ttk
from app.modules.button_click_module import BookActionController
from app.modules.search_module import handle_search


controller = BookActionController()


def e_books_gui(container):

    search_component(
        container,
        title="Search Book",
        button_text="Search",
        label_text="ISBN: ",
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
    )

    button_toolbar(
        container,
        bd={
            "Add": lambda: controller.handle_add(target=book_form),
            "Update": lambda: controller.handle_update,
            "Delete": controller.handle_delete,
            "Clear": controller.handle_clear,
        },
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10,
    )

    book_form = details_component(
        container,
        title="Book Details",
        label_text=[
            "ISBN",
            "Title",
            "Author",
            "Publisher",
            "Status",
        ],
        name_list=[
            "isbn",
            "title",
            "author",
            "publisher",
            "status",
        ],
    )
    book_form.grid(
        row=2,
        column=0,
        padx=10,
        pady=10,
    )


def printed_books_gui(container):

    search_component(
        container,
        title="Search Book",
        button_text="Search",
        label_text="ISBN: ",
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
    )

    button_toolbar(
        container,
        bd={
            "Add": lambda: controller.handle_add(target=book_form),
            "Update": controller.handle_update,
            "Delete": controller.handle_update,
            "Clear": controller.handle_clear,
        },
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10,
    )

    book_form = details_component(
        parent=container,
        title="Book Details",
        label_text=[
            "ISBN",
            "Title",
            "Author",
            "Publisher",
            "Status",
        ],
        name_list=[
            "isbn",
            "title",
            "author",
            "publisher",
            "status",
        ],
    )
    book_form.grid(
        row=2,
        column=0,
        padx=10,
        pady=10,
    )


def book_gui(c):

    book_tab = ttk.Notebook(c)
    book_tab.pack(pady=10, expand=True, fill="both")

    pb = ttk.Frame(book_tab)
    book_tab.add(pb, text="Printed Books")
    printed_books_gui(pb)

    eb = ttk.Frame(book_tab)
    book_tab.add(eb, text="E Books")
    e_books_gui(eb)
