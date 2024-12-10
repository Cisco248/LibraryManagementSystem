class Member:
    def __init__(self, member_id=None, member_name=None, contact_info=None, age=0, membership_type=None, membership_status=None):
        self.member_id = member_id
        self.member_name = member_name
        self.contact_info = contact_info
        self.age = age
        self.membership_type = membership_type
        self.membership_status = membership_status
        self.borrowed_books = []
        self.members = []

    def register_member(self, member):
        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                print(f"Member with ID {member.member_id} already exists")
                return
        self.members.append(member)

    def update_contact_info(self, new_contact_info):
        if self.contact_info != new_contact_info:
            prev_contact_info = self.contact_info
            self.contact_info = new_contact_info
            print(f"{self.member_name}'s previous contact info: {prev_contact_info} updated to {self.contact_info}")
        else:
            print(f"{self.member_name}'s contact info is the same as the new one, no update needed.")   

    def borrow_book(self, book):
        if self.membership_status == "Active":
            self.borrowed_books.append(book)
            print(f"{self.member_name} borrowed the book: {book.title}")
        else:
            print(f"{self.member_name}'s membership is not active, cannot borrow books.")
        
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.member_name} returned the book: {book.title}")
        else:
            print(f"{self.member_name} has not borrowed the book: {book.title}.")
        
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

class Employee(Member):
    def __init__(self, member_id, member_name, contact_info, age, membership_type, membership_status, employee_id, position, salary):
        super().__init__(member_id, member_name, contact_info, age, membership_type, membership_status)
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

