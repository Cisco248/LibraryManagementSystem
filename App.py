"""
Module: app

This module acts as the main entry point for the application.
It integrates functionalities from the `BookManagement`,
`AuthorManagement`, and `MemberManagement` modules to form
a cohesive library management system.
"""
from book_management import PrintedBook, Ebook
from author_management import HandleAuthor, HandleLicense
from member_management import Member, Employee

if __name__ == "__main__":
    pbk = PrintedBook()
    ebk = Ebook()
    ha = HandleAuthor()
    hl = HandleLicense()
    mm = Member()
    emp = Employee()

    pbk.add_book("Guitar lesson 1", "111111", "Mark", "Music", "Available")
    pbk.add_book("Python Basics", "222222", "John Doe", "Programming", "Available")
    pbk.add_book("Cooking 101", "333333", "Jane Smith", "Cooking", "Unavailable")
    pbk.add_book("Astronomy Guide", "444444", "Dr. Star", "Science", "Available")
    pbk.add_book("History of Art", "555555", "Leonardo", "Art", "Available")
    pbk.get_book_details()

    pbk.delete_book("Guitar lesson 1", "111111")
    pbk.get_book_details()

    pbk.update_book_details("333333", "Music Production", "Mark", "Music", "Available")
    pbk.get_book_details()

    pbk.check_status("Cooking 101")

    pbk.update_status("Guitar lesson 1", "Unavailable")
    pbk.get_book_details()


    pbk.find_book("555555")

    ebk.add_ebook("456123789", "Machine Learning Basics", "Alice Johnson", "Technology", "https://example.com/ml_basics", "6MB")
    ebk.add_ebook("123456789", "Python Basics", "John Doe", "Programming", "http://example.com", "20MB")
    ebk.add_ebook("987654321", "Guitar Lesson", "Jane Doe", "Music", "http://example.com", "5MB")
    ebk.get_ebook_details()
    ebk.download("456123789")
    ebk.get_file_size("123456789")

    ha.add_author("A001", "Maark Anderson", "Main Street,High level.", "G123456789", "1 - Year")
    ha.add_author("A002", "Henry Cavill", "School Road,Romania.", "G234567891", "1 1/2 - Year")
    ha.add_author("A003", "Anton Jones", "Main Street,Peace Road.", "G345678912", "3 - Year")
    ha.add_author("A004", "John Doe", "12/A,High level.", "G456789123", "2 - Year")
    ha.add_author("A005", "Hillary Klinton", "350A,Flower Road.", "G567891234", "1/2 -Year")
    ha.get_authors()

    ha.delete_author("A001")
    ha.get_authors()

    ha.edit_author("A002", "Henry William", "School Road,Romania.", "G234567891", "1 - Year")
    ha.get_authors()

    hl.add_license("L0001", "5 - Years")
    hl.add_license("L0023", "4 - Years")
    hl.add_license("L0005", "2 - Years")
    hl.get_license()

    hl.update_license("L0001", "3 - Years")
    hl.get_license()


    mm.register_member("S001", "Andrew Collison", "+94123456789", 23, "Staff", "")
    mm.register_member("S002", "Anton Newtown", "+94234567891", 20, "Client", "Silver")
    mm.register_member("S003", "Mark Antony", "+94345678912", 25, "Staff", "")
    mm.register_member("S004", "Henry Wright", "+94456789123", 18, "Client", "Silver")
    mm.get_member_details()