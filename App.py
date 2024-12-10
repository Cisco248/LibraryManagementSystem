from Models.BookManagement import BookManagement, PrintedBook, Ebook
from Models.AuthorManagement import HandleAuthor, HandleLicense
from Models.MemberManagement import Member, Employee

# class Library:
#     def __init__(self, library_id, library_name, address):
#         self.library_id = library_id
#         self.library_name = library_name
#         self.address = address
#         self.books = []
#         



#     def add_book(self, book):
#         # Check for duplicate book
#         for existing_book in self.books:
#             if existing_book.book_id == book.book_id:
#                 print(f"Book with ID {book.book_id} already exists")
#                 return

#         # Add the book
#         self.books.append(book)
#         print(f"Book '{book.title}' (ID: {book.book_id}) has been successfully")

#     def remove_book(self, book_id):
#         for book in self.books:
#             if book.book_id == book_id:
#                 self.books.remove(book)
#                 print(f"Book with ID {book_id} has been removed")
#                 return
#         print(f"Book with ID {book_id} not found in the library.")

if __name__ == "__main__":
    bk = BookManagement()
    pbk = PrintedBook()
    ebk = Ebook()
    ha = HandleAuthor()
    hl = HandleLicense()

    # bk.add_book("Guitar lesson 1", "111111", "Mark", "Music", "Available")
    # bk.add_book("Python Basics", "222222", "John Doe", "Programming", "Available")
    # bk.add_book("Cooking 101", "333333", "Jane Smith", "Cooking", "Unavailable")
    # bk.add_book("Astronomy Guide", "444444", "Dr. Star", "Science", "Available")
    # bk.add_book("History of Art", "555555", "Leonardo", "Art", "Available")
    # bk.get_book_details()

    # bk.delete_book("Guitar lesson 1", "111111")
    # bk.get_book_details()

    # bk.update_book_details("333333", "Music Production", "Mark", "Music", "Available")
    # bk.get_book_details()

    # pbk.check_status("Guitar lesson 1")

    # pbk.update_status("Guitar lesson 1", "Unavailable")

    # pbk.find_book("101")

    # ebk.add_ebook("456123789", "Machine Learning Basics", "Alice Johnson", "Technology", "https://example.com/ml_basics", "6MB")
    # ebk.add_ebook("123456789", "Python Basics", "John Doe", "Programming", "http://example.com", "20MB")
    # ebk.add_ebook("987654321", "Guitar Lesson", "Jane Doe", "Music", "http://example.com", "5MB")
    # ebk.get_ebook_details()
    # ebk.download("456123789")
    # ebk.get_file_size("987654321")

    # ha.add_author("A001", "Maark Anderson", "Main Street,High level.", "G123456789", "1 - Year")
    # ha.add_author("A002", "Henry Cavill", "School Road,Romania.", "G234567891", "1 1/2 - Year")
    # ha.add_author("A003", "Anton Jones", "Main Street,Peace Road.", "G345678912", "3 - Year")
    # ha.add_author("A004", "John Doe", "12/A,High level.", "G456789123", "2 - Year")
    # ha.add_author("A005", "Hillary Klinton", "350A,Flower Road.", "G567891234", "1/2 -Year")
    # ha.get_authors()

    # ha.delete_author("A001")
    # ha.get_authors()

    # ha.edit_author("A002", "Henry William", "School Road,Romania.", "G234567891", "1 - Year")
    # ha.get_authors()

    # hl.add_license("L0001", "5 - Years")
    # hl.add_license("L0023", "4 - Years")
    # hl.add_license("L0005", "2 - Years")
    # hl.get_license()

    print("\n")
    member = Member()

    member = Member("201", "Alice", "alice@example.com", 25, "Standard", "Active")
    member.register_member(member)

    stm = Employee

    stm.update_member_status(Employee, "M001", "Suspended")
    

    print("\n=== Member Operations ===")
    member.update_contact_info("alice_new@example.com")
    book_4 = BookManagement("101", "Python Programming", "123456789", "John Doe", "Programming")
    member.borrow_book(book_4)
    member.return_book(book_4)