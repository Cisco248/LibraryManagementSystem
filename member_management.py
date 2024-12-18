class Member:
    """
    Handles member-related operations like adding, updating, and managing member records.
    """

    def __init__(self, books=None):
        """
        Initialize the Member class with a list of books.

        Args:
            books (list, optional): A list of books managed by the system. Defaults to None.
        """
        self.members = []
        self.books = books if books is not None else []

    def register_member(self, member_id, member_name, contact_no, age, membership_type, membership_status):
        """
        Register a new member to the library.

        Args:
            member_id (str): The unique ID of the member.
            member_name (str): The name of the member.
            contact_no (str): The contact number of the member.
            age (int): The age of the member.
            membership_type (str): The type of membership.
            membership_status (str): The status of the membership.
        """
        print("\n========== Add Member ==========")
        if any(member['Member ID'] == member_id for member in self.members):
            print(f"Member with ID '{member_id}' already exists!")
            return
        member = {
            "Member ID": member_id,
            "Member Name": member_name,
            "Contact No": contact_no,
            "Age": age,
            "Membership Type": membership_type,
            "Membership Status": membership_status,
            "Borrowed Books": []
        }
        self.members.append(member)
        print(f"Member '{member_id}' added successfully!")

    def update_member(self, member_id, new_member_name=None, new_contact_no=None, new_age=None, new_member_type=None, new_membership_status=None):
        """
        Update details of an existing member.

        Args:
            member_id (str): The ID of the member to update.
            new_member_name (str, optional): The new name of the member.
            new_contact_no (str, optional): The new contact number of the member.
            new_age (int, optional): The new age of the member.
            new_member_type (str, optional): The new membership type.
            new_membership_status (str, optional): The new membership status.
        """
        print("\n========== Update Member ==========")
        member = next((m for m in self.members if m['Member ID'] == member_id), None)
        if not member:
            print(f"Member with ID '{member_id}' not found.")
            return

        if new_member_name:
            member['Member Name'] = new_member_name
        if new_contact_no:
            member['Contact No'] = new_contact_no
        if new_age:
            member['Age'] = new_age
        if new_member_type:
            member['Membership Type'] = new_member_type
        if new_membership_status:
            member['Membership Status'] = new_membership_status

        print(f"Member ID: {member_id} updated successfully.")

    def delete_member(self, member_id):
        """
        Delete an existing member.

        Args:
            member_id (str): The ID of the member to delete.
        """
        print("\n========== Delete Member ==========")
        member = next((m for m in self.members if m['Member ID'] == member_id), None)
        if not member:
            print(f"Member with ID '{member_id}' not found.")
            return
        self.members.remove(member)
        print(f"Member with ID '{member_id}' successfully deleted.")

    def get_member_details(self):
        """
        Print details of all members.

        Returns:
            None
        """
        print("\n========== All Member Details ==========")
        if not self.members:
            print("No members found.")
        else:
            for member in self.members:
                borrowed_books = ', '.join([book['Title'] for book in member['Borrowed Books']]) or 'None'
                print(f"Member ID: {member['Member ID']}\n"
                      f"Member Name: {member['Member Name']}\n"
                      f"Contact No: {member['Contact No']}\n"
                      f"Age: {member['Age']}\n"
                      f"Membership Type: {member['Membership Type']}\n"
                      f"Membership Status: {member['Membership Status']}\n"
                      f"Borrowed Books: {borrowed_books}\n")

    def borrow_book(self, member_id, isbn):
        """
        Allow a member to borrow a book.

        Args:
            member_id (str): The ID of the member borrowing the book.
            isbn (str): The ISBN of the book to borrow.
        """
        print("\n========== Borrow Book ==========")
        member = next((m for m in self.members if m['Member ID'] == member_id), None)
        book = next((b for b in self.books if b['ISBN'] == isbn), None)
        if not member:
            print(f"Member with ID '{member_id}' not found.")
            return
        if not book:
            print(f"Book with ISBN '{isbn}' not found.")
            return
        if book.get('Status') == 'Borrowed':
            print(f"Book '{book['Title']}' is already borrowed.")
            return
        member['Borrowed Books'].append(book)
        book['Status'] = 'Borrowed'
        print(f"Book '{book['Title']}' successfully borrowed by member '{member['Member Name']}'.")

    def return_book(self, member_id, isbn):
        """
        Allow a member to return a borrowed book.

        Args:
            member_id (str): The ID of the member returning the book.
            isbn (str): The ISBN of the book to return.
        """
        print("\n========== Return Book ==========")
        member = next((m for m in self.members if m['Member ID'] == member_id), None)
        if not member:
            print(f"Member with ID '{member_id}' not found.")
            return
        book = next((b for b in member['Borrowed Books'] if b['ISBN'] == isbn), None)
        if not book:
            print(f"Book with ISBN '{isbn}' not found in borrowed books.")
            return
        member['Borrowed Books'].remove(book)
        book['Status'] = 'Available'
        print(f"Book '{book['Title']}' successfully returned by member '{member['Member Name']}'.")


class Employee(Member):
    """
    Handles operations specific to library employees, extending the functionality of the Member class.
    """
    def __init__(self, books=None):
        super().__init__(books)
        self.employees = []

    def add_employee(self, employee_id, member_id, position, salary):
        """
        Add an employee to the library system.

        Args:
            employee_id (str): The unique ID of the employee.
            member_id (str): The member ID associated with the employee.
            position (str): The position of the employee in the library.
            salary (float): The salary of the employee.
        """
        print("\n========== Add Employee ==========")
        member = next((m for m in self.members if m['Member ID'] == member_id), None)
        if not member:
            print(f"Member with ID '{member_id}' not found.")
            return
        employee = {
            "Employee ID": employee_id,
            "Member ID": member_id,
            "Position": position,
            "Salary": salary
        }
        self.employees.append(employee)
        print(f"Employee '{employee_id}' added successfully.")

    def update_member_status(self, member_id, new_membership_status):
        """
        Update the membership status of a member.

        Args:
            member_id (str): The ID of the member whose status is to be updated.
            new_membership_status (str): The new membership status.
        """
        print("\n========== Update Membership Status ==========")
        member = next((m for m in self.members if m['Member ID'] == member_id), None)
        if not member:
            print(f"Member with ID '{member_id}' not found.")
            return
        member['Membership Status'] = new_membership_status
        print(f"Membership status for Member ID '{member_id}' updated to '{new_membership_status}'.")
