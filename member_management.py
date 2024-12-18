"""
Module: MemberManagement

This module handles operations related to library members, such as adding members
and managing their details.
"""
class Member:
    """
    Handles member-related operations like adding and updating member records.
    """
    def __init__(self, member_id=None, member_name=None, contact_no=None, age=0, membership_type=None, membership_status=None):
        self.member_id = member_id
        self.member_name = member_name
        self.contact_no = contact_no
        self.age = age
        self.membership_type = membership_type
        self.membership_status = membership_status
        self.borrowed_books = []
        self.members = []
        self.books = []

    def register_member(self, member_id, member_name, contact_no, age, membership_type, membership_status):
        print("\n========== Add Member ==========")
        if member_id in self.members:
            print(f"Member is Existed!")
        else:
            member = {
                "Member ID": member_id,
                "Member Name": member_name,
                "Contact No": contact_no,
                "Age": age,
                "Member Type": membership_type,
                "Membership Status": membership_status
            }
            self.members.append(member)
            print(f"Member '{member_id}' Added Successfully!")            
            return

    def update_member(self, member_id, new_member_name, new_contact_no, new_age, new_member_type, new_membership_status):
        print("\n========== Update Member ==========")
        for member in self.members:
            if member['Member ID'] == member_id:
                if new_member_name:
                    member['Member Name'] = new_member_name
                if new_contact_no:
                    member['Contact No'] = new_contact_no
                if new_age:
                    member['Age'] = new_age
                if new_member_type:
                    member['Member Type'] = new_member_type
                if new_membership_status:
                    member['Membership Status'] = new_membership_status
                print(f"Member ID: {member['Member ID']}\nMember Name: {member['Member Name']}\nContact No: {member['Contact No']}\nAge: {member['Age']}\nMember Type: {member['Member Type']}\nMembership Status: {member['Membership Status']}\n>>>>> Update Successfully")
                return
            else:
                return f"Member Not Found"
    
    def delete_member(self, member_id):
        print("\n========== Delete Member ==========")
        for member in self.members:
            if member['Member ID'] == member_id:
                self.members.remove(member)
                print(f"Member ID: {member['Member ID']}\nMember Name: {member['Member Name']}\n>>>>> Successfully Deleted")
                return
        print(f"Member Not Found!")

    def get_member_details(self):
        print("\n========== All Member Details ==========")
        if not self.members:
            print("Member List is Empty.")
        else:
            for member in self.members:
                print(f"Member ID: {member['Member ID']}\nMember Name: {member['Member Name']}\nContact No: {member['Contact No']}\nAge: {member['Age']}\nMember Type: {member['Member Type']}\nMembership Status: {member['Membership Status']}\n")

    def upgrade_membership(self):
        if self.membership_type == "Standard":
            self.membership_type = "Premium"
            print(f"{self.member_name}'s membership upgraded to Premium.")
        else:
            print(f"{self.member_name}'s membership is already Premium.")
    
    def downgrade_membership(self):
        if self.membership_type == "Premium":
            self.membership_type = "Standard"
            print(f"{self.member_name}'s membership downgraded to Standard.")
        else:
            print(f"{self.member_name}'s membership is already Standard.")

    def borrow_book(self, isbn):
        print("========== Book Barrow Details ==========")
        for book in self.books:
            if book['ISBN'] == isbn:
                print(f"ISBN: {book['ISBN']}\nTitle: {book['Title']}\nBook is Barrowed")
                return
            else:
                return f"Please Enter the Valid ISBN"
        
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.member_name} returned the book: {book.title}")
        else:
            print(f"{self.member_name} has not borrowed the book: {book.title}.")

class Employee(Member):
    def __init__(self, member_id=None, member_name=None, contact_no=None, age=0, membership_type=None, membership_status=None, employee_id=None, position=None, salary=None):
        super().__init__(member_id, member_name, contact_no, age, membership_type, membership_status)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary

    def update_member_status(self, member_id, new_membership_status):
        # for member in self.members:
            if member_id == member_id:
                membership_status = new_membership_status
                print(f"member with ID {member_id} membership status set to {new_membership_status}")
                return
            print(f"member with ID {member_id} is doesn't exist.")

    # def manage_inventory(self,library, book, action):        
    #     if action == "add":
    #         library.add_book(book)
    #         print(f"Book '{book.title}' has been added to the inventory.")
    #     elif action == "remove":
    #         if library.remove_book(book.book_id):
    #             print(f"Book '{book.title}' has been removed from the inventory.")
    #         else:
    #             print(f"Book with ID {book.book_id} could not be found in the inventory.")
    #     else:
    #         print("Invalid action. Use 'add' or 'remove'.")

    # def issue_fines(self, member, amount):
    #     if member.membership_status == "Active":
    #         member.fine_amount = amount
    #         print(f"Fine of Rs. {amount} issued to {member.member_name}. Total fine is now Rs.{member.fine_amount}.")
    #     else:
    #         print(f"Cannot issue a fine to {member.member_name}. Membership status is '{member.membership_status}'.")

