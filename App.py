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

def main():
    # Initialize objects
    pbk = PrintedBook()
    ebk = Ebook()
    ha = HandleAuthor()
    hl = HandleLicense()
    mm = Member()
    # emp = Employee()

    # Printed Book Operations
    pbk.add_book({
        "Title": "Guitar Lesson 1",
        "ISBN": "111111",
        "Author": "Mark",
        "Category": "Music",
        "Status": "Available"
    })
    pbk.add_book({
        "Title": "Python Basics",
        "ISBN": "222222",
        "Author": "John Doe",
        "Category": "Programming",
        "Status": "Available"
    })
    pbk.add_book({
        "Title": "Cooking 101",
        "ISBN": "333333",
        "Author": "Jane Smith",
        "Category": "Cooking",
        "Status": "Unavailable"
    })
    pbk.add_book({
        "Title": "Astronomy Guide",
        "ISBN": "444444",
        "Author": "Dr. Star",
        "Category": "Science",
        "Status": "Available"
    })
    pbk.add_book({
        "Title": "History of Art",
        "ISBN": "555555",
        "Author": "Leonardo",
        "Category": "Art",
        "Status": "Available"
    })
    pbk.get_book_details()

    pbk.delete_book("111111")
    pbk.get_book_details()

    pbk.update_book_details("333333",{"Title": "Music Production",
                                      "Author": "Mark",
                                      "Category": "Music",
                                      "Status": "Available"})
    pbk.get_book_details()

    pbk.check_status("Music Production")

    pbk.update_status("Music Production", "Unavailable")
    pbk.get_book_details()

    pbk.find_book("555555")

    # Ebook Operations
    ebk.add_ebook({
        "ISBN": "456123789",
        "Title": "Machine Learning Basics",
        "Author": "Alice Johnson",
        "Category": "Technology",
        "Link": "https://example.com/ml_basics",
        "Size": "6MB"
        })
    ebk.add_ebook({
        "ISBN": "123456789",
        "Title": "Python Basics",
        "Author": "John Doe",
        "Category": "Programming",
        "Link": "http://example.com",
        "Size": "20MB"
        })
    ebk.add_ebook({
        "ISBN": "987654321",
        "Title": "Guitar Lesson",
        "Author": "Jane Doe",
        "Category": "Music",
        "Link": "http://example.com",
        "Size": "5MB"})
    ebk.get_ebook_details()
    ebk.download("456123789")
    ebk.get_file_size("123456789")

    # Author Operations
    ha.add_author({
        "author_id": "A001",
        "author_name": "Mark Anderson",
        "address": "Main Street, High Level.",
        "gov_reg_no": "G123456789",
        "agreement_time": "1 Year"
        })
    ha.add_author({
    "author_id": "A002",
    "author_name": "Henry Cavill",
    "address": "School Road, Romania.",
    "gov_reg_no": "G234567891",
    "agreement_time": "1.5 Years"
    })

    ha.add_author({
        "author_id": "A003",
        "author_name": "Anton Jones",
        "address": "Main Street, Peace Road.",
        "gov_reg_no": "G345678912",
        "agreement_time": "3 Years"
    })

    ha.add_author({
        "author_id": "A004",
        "author_name": "John Doe",
        "address": "12/A, High Level.",
        "gov_reg_no": "G456789123",
        "agreement_time": "2 Years"
    })

    ha.add_author({
        "author_id": "A005",
        "author_name": "Hillary Clinton",
        "address": "350A, Flower Road.",
        "gov_reg_no": "G567891234",
        "agreement_time": "6 Months"
    })
    ha.list_authors()

    ha.delete_author("A001")
    ha.list_authors()

    ha.edit_author("A002", {
        "author_name": "Henry William",
        "address": "School Road, Romania.",
        "gov_reg_no": "G234567891",
        "agreement_time": "1 Year"})
    ha.list_authors()

    # License Operations
    hl.add_license({
        "license_no": "L0001",
        "license_period": "5 Years"
        })
    hl.add_license({
        "license_no": "L0023",
        "license_period": "4 Years"
        })
    hl.add_license({
        "license_no": "L0005",
        "license_period": "2 Years"})
    hl.list_licenses()

    hl.update_license("L0001", {
        "license_period": "3 Years"
        })
    hl.list_licenses()

    # Member Operations
    mm.register_member("S001", "Andrew Collison", "+94123456789", 23, "Staff", None)
    mm.register_member("S002", "Anton Newtown", "+94234567891", 20, "Client", "Silver")
    mm.register_member("S003", "Mark Antony", "+94345678912", 25, "Staff", None)
    mm.register_member("S004", "Henry Wright", "+94456789123", 18, "Client", "Silver")
    mm.get_member_details()

if __name__ == "__main__":
    main()
