class SearchLogic:

    def __init__(self, isbn, widget):
        self.isbn = isbn
        self.widget = widget

        print(f"Searching database for ISBN: {self.isbn}")
        if len(isbn) < 5:
            self.widget.set_feedback("Invalid ISBN format", is_error=True)
        else:
            self.widget.set_feedback(f"Book found: 'Python Mastery'", is_error=False)
