"""
Module: MemberManagement

This module handles operations related to library members, such as adding members
and managing their details.
"""
class Member:
    """
    Handles member-related operations like adding, updating, and managing member records.
    """
    def __init__(self):
        self.members = []
        self.books = []

    def register_member(self, member_id, member_name, contact_no, age, membership_type, membership_status):
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
        print("\n========== Delete Member ==========")
        member = next((m for m in self.members if m['Member ID'] == member_id), None)
        if not member:
            print(f"Member with ID '{member_id}' not found.")
            return
        self.members.remove(member)
        print(f"Member with ID '{member_id}' successfully deleted.")

    def get_member_details(self):
        print("\n========== All Member Details ==========")
        if not self.members:
            print("No members found.")
        else:
            for member in self.members:
                print(f"Member ID: {member['Member ID']}\nMember Name: {member['Member Name']}\nContact No: {member['Contact No']}\n"
                      f"Age: {member['Age']}\nMembership Type: {member['Membership Type']}\nMembership Status: {member['Membership Status']}\n"
                      f"Borrowed Books: {', '.join([book['Title'] for book in member['Borrowed Books']]) or 'None'}\n")

    def borrow_book(self, member_id, isbn):
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
    def __init__(self):
        super().__init__()
        self.employees = []

    def add_employee(self, employee_id, member_id, position, salary):
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
        print("\n========== Update Membership Status ==========")
        member = next((m for m in self.members if m['Member ID'] == member_id), None)
        if not member:
            print(f"Member with ID '{member_id}' not found.")
            return
        member['Membership Status'] = new_membership_status
        print(f"Membership status for Member ID '{member_id}' updated to '{new_membership_status}'.")
