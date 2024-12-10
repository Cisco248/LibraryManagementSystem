# from library import Library
# from member import Member
# from employee import Employee
# from BookManagement import BookManagement

# # Example test case
# if __name__ == "__main__":
#     library = Library("1", "City Library", "123 Main St")
    
#     book = BookManagement("101", "Python Programming", "123456789", "John Doe", "Programming")
#     book_2 = BookManagement("102", "Data Science Essentials", "987654321", "Jane Smith", "Data Science")

#     print("\n=== Book Operations ===")
#     print(book.get_book_details())
#     book.check_availability()
#     book.update_availability(False)

#     print("\n=== Library Operations ===")
#     library.add_book(book)
#     library.add_book(book_2)
  
#     library.remove_book("102")
    
#     # Create a member

    
#     # # Create a Loan instance
#     # loan = Loan("L001", "2024-12-01", "2024-12-07")
#     # # Example usage of loan methods
#     # print("\n=== Loan Operations ===")
#     # # Check if the book is overdue
#     # loan.check_due_date()        
#     # # Mark the book as returned
#     # loan.complete_return("2024-12-10")
#     # # Calculate fine
#     # loan.calc_fine()           
#     # # Extend Loan by days
#     # loan.extend_loan(5)

#     # Create a PrintedBook
#     book_3 = PrintedBook("102", "Data Science Essentials", "987654321", "Jane Smith", "Data Science", 10, "Aisle 3, Shelf B", "Good")
#     # Example usage of PrintedBook methods
#     print("\n=== Printed Book Operations ===")
#     # View location of the book
#     book_3.view_location()
#     # Update the location of the book
#     book_3.update_location("Aisle 5, Shelf D")
#     # Check the quantity of the book
#     book_3.check_quantity()
#     # Update the quantity of the book
#     book_3.update_quantity(8)
#     # Update the condition of the book
#     book_3.update_condition("Excellent")

#     # Create an Ebook
#     ebook = Ebook("201", "Machine Learning Basics", "456123789", "Alice Johnson", "Technology", "https://example.com/ml_basics", "5MB")
#     # Example usage of Ebook methods
#     print("\n=== Ebook Operations ===")
#     # Get the downloadable link of the ebook
#     ebook.download()
#     # Get the file size of the ebook
#     ebook.get_file_size()

#     # # Create an Patron
#     # patron = Patron("201", "Alice", "alice@example.com", 25, "Standard", "Active", 3, 500)
#     # print("\n=== patron Operations ===")
#     # # Patron reserves a book
#     # patron.reserve_book(library, "102")

#     # Create an Employee
#     employee = Employee("E001", "John", "john@example.com", 35, "Staff", "Active", "EMP001", "Librarian", 50000)
#     # Example usage of Employee methods
#     print("\n=== Employee Operations ===")
#     # Update a member's status

#     # Add a book to the library inventory
#     # Create Book 3 instance
#     book_3 = Book("103", "Machine Learning Basics", "192837465", "Mark Johnson", "Machine Learning")
#     employee.manage_inventory(library, book_3, "add")
#     # Issue a fine to a member
#     employee.issue_fines(member, 10)
#     # Remove a book from the library inventory
#     employee.manage_inventory(library, book_3, "remove")

  