"""
Module: AuthorManagement

This module handles the management of authors, including adding, listing,
and retrieving author details.
"""
class HandleAuthor:
    """
    Handles author-related operations such as adding, listing, and updating authors.
    """
    def __init__(self, author_id=None, author_name=None, address=None, gov_reg_no=None, agreement_time=None):
        self.author_id = author_id
        self.author_name = author_name
        self.address = address
        self.gov_reg = gov_reg_no
        self.agreement_time = agreement_time
        self.authors = []

    def add_author(self, author_id, author_name, address, gov_reg_no, agreement_time):
        print("\n========== Add Author ==========")
        if author_id in self.authors:
            print(f"Author Not Found!")
        else:
            author = {
                "Author ID": author_id,
                "Author Name": author_name,
                "Address": address,
                "Gov Reg No": gov_reg_no,
                "Agreement Time": agreement_time
            }
            self.authors.append(author)
            print(f"Author '{author_id}' Added Successfully!")
            return

    def edit_author(self, author_id, new_author_name, new_address, new_gov_reg_no, new_agreement_time):
        print("\n========== Update Author ==========")
        for author in self.authors:
            if author['Author ID'].lower() == author_id.lower():
                if new_author_name:
                    author["Author Name"] = new_author_name
                if new_address:
                    author["Address"] = new_address
                if new_gov_reg_no:
                    author["Gov Reg No"] = new_gov_reg_no
                if new_agreement_time:
                    author["Agreement Time"] = new_agreement_time
                print(f"Author ID: {author_id}\nAuthor Name: {new_author_name}\nAddress: {new_address}\nGov Reg No: {new_gov_reg_no}\nAgreement Period: {new_agreement_time}\n>>>>> Updated Successfully!")
        return f"Author is Not Found"

    def get_authors(self):
        if not self.authors:
            print("List is Empty.")
        else:
            print("\n========== Author Details ==========")
            for author in self.authors:
                print(f"\nAuthor ID: {author['Author ID']}\nAuthor Name: {author['Author Name']}\nAddress: {author['Address']}\nGov Reg No: {author['Gov Reg No']}\nAgreement Period: {author['Agreement Time']}")

    def delete_author(self, author_id):
        print("\n========== Delete Author ==========")
        for author in self.authors:
            if author_id == author['Author ID']:
                print(f"Author ID: {author_id}\nSuccessfully Deleted")
                self.authors.remove(author)
            return f"Author is Not Found!"

class HandleLicense(HandleAuthor):
    def __init__(self, license_no=None, license_period=None):
        self.license_no = license_no
        self.license_period = license_period
        self.authors = []

    def add_license(self, license_no, license_period):
        print("\n========== Add License ==========")
        if license_no in self.authors:
            print(f"Author Not Found!")
        else:
            author = {
                "License No": license_no,
                "License Period": license_period,
            }
            self.authors.append(author)
            print(f"License '{license_no}' Added Successfully!")
            return

    def update_license(self, license_no, license_period):
        print("\n========== Edit License ==========")
        for author in self.authors:
            if author['License No'] == license_no:
                if license_no:
                    author["License No"] = license_no
                if license_period:
                    author["License Period"] = license_period
                print(f"License No: {license_no}\nLicense Period: {license_period}\n>>>>> Updated Successfully!")
        return f"Author Not Found"

    def get_license(self):
        if not self.authors:
            print("List is Empty.")
        else:
            print("\n========== License Details ==========")
            for author in self.authors:
                print(f"\nLicense No: {author['License No']}\nLicense Period: {author['License Period']}")