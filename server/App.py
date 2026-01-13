"""
Module: app

This module acts as the main entry point for the application.
It integrates functionalities from the `BookManagement`,
`AuthorManagement`, and `MemberManagement` modules to form
a cohesive library management system.
"""

# from logic.services.book_management import PrintedBook, Ebook
# from logic.services.author_management import HandleAuthor, HandleLicense
# from logic.services.member_management import Member


def main():
    """
    Manages main app calling the all the class with parameters.
    """
    # Initialize objects
    pbk = PrintedBook()
    ebk = Ebook()
    ha = HandleAuthor()
    hl = HandleLicense()
    mm = Member()

    # Printed Book Operations

    pbk.delete_book("111111")
    pbk.get_book_details()

    pbk.update_book_details(
        "333333",
        {
            "Title": "Music Production",
            "Author": "Mark",
            "Category": "Music",
            "Status": "Available",
        },
    )
    pbk.get_book_details()

    pbk.check_status("Music Production")

    pbk.update_status("Music Production", "Unavailable")
    pbk.get_book_details()

    pbk.find_book("555555")

    # Ebook Operations
    ebk.add_ebook(
        {
            "ISBN": "456123789",
            "Title": "Machine Learning Basics",
            "Author": "Alice Johnson",
            "Category": "Technology",
            "Link": "https://example.com/ml_basics",
            "Size": "6MB",
        }
    )
    ebk.add_ebook(
        {
            "ISBN": "123456789",
            "Title": "Python Basics",
            "Author": "John Doe",
            "Category": "Programming",
            "Link": "http://example.com",
            "Size": "20MB",
        }
    )
    ebk.add_ebook(
        {
            "ISBN": "987654321",
            "Title": "Guitar Lesson",
            "Author": "Jane Doe",
            "Category": "Music",
            "Link": "http://example.com",
            "Size": "5MB",
        }
    )
    ebk.get_ebook_details()
    ebk.download("456123789")
    ebk.get_file_size("123456789")

    # Author Operations
    ha.add_author(
        {
            "author_id": "A001",
            "author_name": "Mark Anderson",
            "address": "Main Street, High Level.",
            "gov_reg_no": "G123456789",
            "agreement_time": "1 Year",
        }
    )
    ha.add_author(
        {
            "author_id": "A002",
            "author_name": "Henry Cavill",
            "address": "School Road, Romania.",
            "gov_reg_no": "G234567891",
            "agreement_time": "1.5 Years",
        }
    )

    ha.add_author(
        {
            "author_id": "A003",
            "author_name": "Anton Jones",
            "address": "Main Street, Peace Road.",
            "gov_reg_no": "G345678912",
            "agreement_time": "3 Years",
        }
    )

    ha.add_author(
        {
            "author_id": "A004",
            "author_name": "John Doe",
            "address": "12/A, High Level.",
            "gov_reg_no": "G456789123",
            "agreement_time": "2 Years",
        }
    )

    ha.add_author(
        {
            "author_id": "A005",
            "author_name": "Hillary Clinton",
            "address": "350A, Flower Road.",
            "gov_reg_no": "G567891234",
            "agreement_time": "6 Months",
        }
    )
    ha.list_authors()

    ha.delete_author("A001")
    ha.list_authors()

    ha.edit_author(
        "A002",
        {
            "author_name": "Henry William",
            "address": "School Road, Romania.",
            "gov_reg_no": "G234567891",
            "agreement_time": "1 Year",
        },
    )
    ha.list_authors()

    # License Operations
    hl.add_license({"license_no": "L0001", "license_period": "5 Years"})
    hl.add_license({"license_no": "L0023", "license_period": "4 Years"})
    hl.add_license({"license_no": "L0005", "license_period": "2 Years"})
    hl.list_licenses()

    hl.update_license("L0001", {"license_period": "3 Years"})
    hl.list_licenses()

    # Member Operations


if __name__ == "__main__":
    main()
