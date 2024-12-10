class BookManagement:
    def __init__(self, title=None, isbn=None, author_name=None, category='Unknown', status='Available', link='', file_size=''):
        self.title = title
        self.isbn = isbn
        self.author = author_name
        self.category = category
        self.status = status
        self.link = link
        self.file_size = file_size
        self.books = {}

    def get_book_details(self):
        if not self.books:
            print("Library is Empty.")
        else:
            print("\n========== All Book Details ==========")
            for index, (isbn, details) in enumerate(self.books.items(), start=1):
                title = details.get('Title', 'N/A')
                author = details.get('Author', 'N/A')
                isbn = details.get('ISBN', 'N/A')
                category = details.get('Category', 'Unknown')
                status = details.get('Status', "0MB")
                print(f"\nTitle: {title}\nISBN: {isbn}\nAuthor: {author}\nCategory: {category}\nStatus: {status}")

    def add_book(self, title, isbn, author, category, status):
        print("\n========== Add Book ==========")
        if isbn in self.books:
            print(f"Book with ISBN '{isbn}' already exists!")
        else:
            self.books[isbn] = {
                "Title": title,
                "ISBN": isbn,
                "Author": author,
                "Category": category,
                "Status": status
            }
            print(f"Book '{title}' Added Successfully!")
            return
        
    def delete_book(self, title, isbn):
        print("\n========== Delete The Book ==========")
        if isbn in self.books:
            print(f"ISBN: {isbn}\nTitle: {title}\nSuccessfully Deleted")
            del self.books[isbn]
        else:
            print(f"Book is Not Found!")

    def update_book_details(self, isbn, title, author, category, status):
        print("\n========== Update Book ==========")
        if isbn not in self.books:
            print(f"Book is Not Found")
            return
        book = self.books[isbn]
        if title:
            book["Title"] = title
        if author:
            book["Author"] = author
        if category:
            book["Category"] = category
        if status:
            book["Status"] = status
        print(f"ISBN: {isbn}\nTitle: {title}\nAuthor: {author}\nCategory: {category}\nStatus: {status}\nUpdated Successfully!")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print(f"Found Book:\n{book.get_book_details()}")
                return book
        print(f"Book with ID {book_id} not found in the library.")
        return None

class PrintedBook(BookManagement):
    def check_status(self, title):
        print("\n========== Check Book Status ==========")
        print(f"Title: {title}\nStatus: {'Available' if self.status else 'Unavailable'}\n")

    def update_status(self, title, next_status):
        print("========== Update Book Status ==========")
        prev_status = self.status
        if prev_status != next_status:
            self.status = next_status
            print (f"Title: {title}\nStatus Updated: {prev_status} to {self.status} successfully.")
            return
        else:
            print(f"{title} is already {prev_status}.")
            return
PrintedBook()
        
class Ebook(BookManagement):
    def __init__(self, title=None, isbn=None, author_name=None, category='Unknown', status='Available', link='', file_size=''):
        super().__init__(title, isbn, author_name, category, status, link, file_size)
        self.link = link
        self.file_size = file_size
        self.books = {}

    def add_ebook(self, isbn, title, author, category, link, file_size):
        print("\n========== Add E-Book ==========")
        if isbn in self.books:
            print(f"Book with ISBN '{isbn}' already exists!")
        else:
            self.books[isbn] = {
                "Title": title,
                "ISBN": isbn,
                "Author": author,
                "Category": category,
                "Link": link,
                "Size": file_size
            }
            print(f"Title: {title}\nISBN: {isbn}\nAuthor: {author}\nCategory: {category}\nLink: {link}\nSize: {file_size}\nAdded Successfully!")

    def get_ebook_details(self):
        if not self.books:
            print("Library is Empty.")
        else:
            print("\n========== All E-Book Details ==========")
            for index, (isbn, details) in enumerate(self.books.items(), start=1):
                title = details.get('Title', 'N/A')
                author = details.get('Author', 'N/A')
                isbn = details.get('ISBN', 'N/A')
                category = details.get('Category', 'Unknown')
                link = details.get('Link', 'N/A')
                size = details.get('Size', "0MB")
                print(f"\nTitle: {title}\nISBN: {isbn}\nAuthor: {author}\nCategory: {category}\nLink: {link}\n(Size: {size})")

    def download(self, isbn):
        print("\n========== E-Book Download Link ==========")
        if isbn in self.books:
            print(f"Title: {self.books[isbn]['Title']}\nLink: {self.books[isbn]['Link']}")
        else:
            print(f"E-Book with ISBN {isbn} is Not Found")
            

    def get_file_size(self, isbn):
        """Get the file size of the e-book."""
        print("\n========== E-Book Size ==========")
        if isbn in self.books:
            print(f"Title: {self.books[isbn]['Title']}\nFile Size: {self.books[isbn]['Size']}")
        else:
            print(f"E-Book with ISBN {isbn} is Not Found")