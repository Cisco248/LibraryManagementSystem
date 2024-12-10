class HandleAuthor:
    def __init__(self, author_id=None, author_name=None, address=None, gov_reg_no=None, agreement_time=None):
        self.author_id = author_id
        self.author_name = author_name
        self.address = address
        self.gov_reg = gov_reg_no
        self.agreement_time = agreement_time
        self.authors = {}

    def add_author(self, author_id, author_name, address, gov_reg_no, agreement_time):
        print("\n========== Add Author ==========")
        if author_id in self.authors:
            print(f"Author Not Found!")
        else:
            self.authors[author_id] = {
                "Author ID": author_id,
                "Author Name": author_name,
                "Address": address,
                "Gov Reg No": gov_reg_no,
                "Agreement Time": agreement_time
            }
            print(f"Author '{author_id}' Added Successfully!")            
            return

    def edit_author(self, author_id, author_name, address, gov_reg_no, agreement_time):
        print("\n========== Update Author ==========")
        if author_id not in self.authors:
            print(f"Author is Not Found")
            return
        author = self.authors[author_id]
        if author_name:
            author["Name"] = author_name
        if address:
            author["Address"] = address
        if gov_reg_no:
            author["Gov Reg No"] = gov_reg_no
        if agreement_time:
            author["Agreement Time"] = agreement_time
        print(f"Author ID: {author_id}\nAuthor Name: {author_name}\nAddress: {address}\nGov Reg No: {gov_reg_no}\nAgreement Period: {agreement_time}\nUpdated Successfully!")

    def get_authors(self):
        if not self.authors:
            print("List is Empty.")
        else:
            print("\n========== Author Details ==========")
            for index, (author_id, details) in enumerate(self.authors.items(), start=1):
                id = details.get('Author ID', 'N/A')
                name = details.get('Author Name', 'N/A')
                address = details.get('Address', 'N/A')
                gov_no = details.get('Gov Reg No', 'Unknown')
                agreement_time = details.get('Agreement Time', "N/A")
                print(f"\nAuthor ID: {id}\nAuthor Name: {name}\nAddress: {address}\nGov Reg No: {gov_no}\nAgreement Period: {agreement_time}")
    
    def delete_author(self, author_id):
        print("\n========== Delete Author ==========")
        if author_id in self.authors:
            print(f"Author ID: {author_id}\nSuccessfully Deleted")
            del self.authors[author_id]
        else:
            print(f"Book is Not Found!")

class HandleLicense(HandleAuthor):
    def __init__(self, license_no=None, license_period=None):
        self.license_no = license_no
        self.license_period = license_period
        self.authors = {}

    def add_license(self, license_no, license_period):
        print("\n========== Add License ==========")
        if license_no in self.authors:
            print(f"Author Not Found!")
        else:
            self.authors[license_no] = {
                "License No": license_no,
                "License Period": license_period,
            }
            print(f"License '{license_no}' Added Successfully!")            
            return

    def update_license(self, license_no, license_period):
        print("\n========== Edit License ==========")
        if license_no not in self.authors:
            print(f"Author is Not Found")
            return
        author = self.authors[license_no]
        if license_no:
            author["License No"] = license_no
        if license_period:
            author["License Period"] = license_period
        print(f"License No: {license_no}\License Period: {license_period}\nUpdated Successfully!")
    
    def get_license(self):
        if not self.authors:
            print("List is Empty.")
        else:
            print("\n========== License Details ==========")
            for x, (y, details) in enumerate(self.authors.items(), start=1):
                no = details.get('License No', 'N/A')
                time = details.get('License Period', 'N/A')
                print(f"\nLicense No: {no}\nLicense Period: {time}")