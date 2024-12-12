class BookManagement:
    def __init__(self, title=None, isbn=None, author_name=None, category='Unknown', status='Available', link='', file_size=''):
        self.title = title
        self.isbn = isbn
        self.author = author_name
        self.category = category
        self.status = status
        self.link = link
        self.file_size = file_size
        self.books = []

    def get_book_details(self):
        print("\n========== All Book Details ==========")
        if not self.books:
            print("Library is Empty.")
        else:
            for book in self.books:
                print(f"Title: {book['Title']}\nISBN: {book['ISBN']}\nAuthor: {book['Author']}\nCategory: {book['Category']}\nStatus: {book['Status']}\n")

    def add_book(self, title, isbn, author, category, status):
        print("\n========== Add Book ==========")
        if isbn in self.books:
                print(f"Book with ISBN: {book.isbn} already exists")
                return
        else:
            book = {
                "Title": title,
                "ISBN": isbn,
                "Author": author,
                "Category": category,
                "Status": status
            }
            self.books.append(book)
            print(f"Book '{title}' Added Successfully!")
            return
        
    def delete_book(self, title, isbn):
        print("\n========== Delete The Book ==========")
        for book in self.books:
            if title == book['Title']:
                self.books.remove(book)
                print(f"ISBN: {isbn}\nTitle: {title}\nSuccessfully Deleted")
                return
        print(f"Book is Not Found!")

    def update_book_details(self, isbn, new_title, new_author, new_category, new_status):
        print("\n========== Update Book ==========")
        for book in self.books:
            if book['ISBN'].lower() == isbn.lower():
                if new_title:
                    book['Title'] = new_title
                if new_author:
                    book['Author'] = new_author
                if new_category:
                    book['Category'] = new_category
                if new_status:
                    book['Status'] = new_status
                print(f"Book '{isbn}' updated successfully!")
                return
        print(f"Book with title '{isbn}' not found.")

    def find_book(self, isbn):
        print("\n========== Find the Book ==========")
        for book in self.books:
            if isbn == book['ISBN']:
                print(f"ISBN: {isbn}\nTitle: {book['Title']}\nAuthor: {book['Author']}\nCategory: {book['Category']}\nStatus: {book['Status']}\n>>>>> Book is Found")
                return
        print("Book is Not Found")

class PrintedBook(BookManagement):
    def __init__(self, title=None, isbn=None, author_name=None, category='Unknown', status='Available', link='', file_size=''):
        super().__init__(title, isbn, author_name, category, status, link, file_size)

    def check_status(self, title):
        print("\n========== Check Book Status ==========")
        for book in self.books:
            if book['Title'] == title:
                print(f"Title: {book['Title']}\nStatus: {book['Status']}")
                return
        print(f"Book '{title}' not found.\n")

    def update_status(self, title, next_status):
        print("\n========== Update Book Status ==========")
        for book in self.books:
            if book['Title'] == title:
                prev_status = book['Status']
                if prev_status != next_status:
                    book['Status'] = next_status
                    print(f"Title: {title}\nStatus Updated: {next_status}\n>>>>> Status Updated Successfully")
                else:
                    print(f"Title: {book['Title']}\nStatus: {next_status}\n>>>>> Already Existed")
                return
        print(f"Book is Not Found.")
        
class Ebook(BookManagement):
    def __init__(self, title=None, isbn=None, author_name=None, category='Unknown', status='Available', link='', file_size=''):
        super().__init__(title, isbn, author_name, category, status, link, file_size)
        self.link = link
        self.file_size = file_size
        self.books = []

    def add_ebook(self, isbn, title, author, category, link, file_size):
        print("\n========== Add E-Book ==========")
        if isbn in self.books:
            print(f"Book with ISBN {ebook.isbn} Already Exists!")
        else:
            ebook = {
                "Title": title,
                "ISBN": isbn,
                "Author": author,
                "Category": category,
                "Link": link,
                "Size": file_size
            }
            self.books.append(ebook)
            print(f"Book '{title}' Added Successfully!")

    def get_ebook_details(self):
        if not self.books:
            print("Library is Empty.")
        else:
            print("\n========== All E-Book Details ==========")
            for ebook in self.books:
                print(f"Title: {ebook['Title']}\nISBN: {ebook['ISBN']}\nAuthor: {ebook['Author']}\nCategory: {ebook['Category']}\nLink: {ebook['Link']}\nSize: {ebook['Size']}\n")

    def download(self, isbn):
        print("\n========== E-Book Download Link ==========")
        for ebook in self.books:
            if isbn in ebook['ISBN']:
                print(f"Title: {ebook['Title']}\nLink: {ebook['Link']}")
        return f"E-Book is Not Found"
            
    def get_file_size(self, isbn):
        print("\n========== E-Book Size ==========")
        for ebook in self.books:
            if isbn in ebook['ISBN']:
                print(f"Title: {ebook['Title']}\nFile Size: {ebook['Size']}")
        return f"E-Book with ISBN {isbn} is Not Found"