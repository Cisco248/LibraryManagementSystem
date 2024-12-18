"""
Module: PublisherManagement

This module handles operations related to publishers, such as adding new publishers
and managing publisher information.
"""
class HandlePublisher:
    """
    Handles publisher-related operations like adding and updating publisher records.
    """
    def __init__(self, publisher_id=None, publisher_name=None, address=None, gov_reg_no=None, agreement_time=None):
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name
        self.address = address
        self.gov_reg = gov_reg_no
        self.agreement_time = agreement_time
        self.publishers = []
    """
    Handles publisher-related operation adding publisher.
    """
    def add_publisher(self, publisher_id, publisher_name, address, gov_reg_no, agreement_time):
        print("\n========== Add Publisher ==========")
        if publisher_id in self.publishers:
            print(f"Publisher Not Found!")
        else:
            publisher = {
                "Publisher ID": publisher_id,
                "Publisher Name": publisher_name,
                "Address": address,
                "Gov Reg No": gov_reg_no,
                "Agreement Time": agreement_time
            }
            self.publishers.append(publisher)
            print(f"Publisher '{publisher_id}' Added Successfully!")
            return
    """
    Handles publisher-related operation editing publisher.
    """
    def edit_publisher(self, publisher_id, new_publisher_name, new_address, new_gov_reg_no, new_agreement_time):
        print("\n========== Update Publisher ==========")
        for publisher in self.publishers:
            if publisher['Publisher ID'].lower() == publisher_id.lower():
                if new_publisher_name:
                    publisher["Author Name"] = new_publisher_name
                if new_address:
                    publisher["Address"] = new_address
                if new_gov_reg_no:
                    publisher["Gov Reg No"] = new_gov_reg_no
                if new_agreement_time:
                    publisher["Agreement Time"] = new_agreement_time
                print(f"Publisher ID: {publisher_id}\nPublisher Name: {new_publisher_name}\nAddress: {new_address}\nGov Reg No: {new_gov_reg_no}\nAgreement Period: {new_agreement_time}\n>>>>> Updated Successfully!")
        return f"Publisher is Not Found"
    """
    Handles publisher-related operation get all publisher.
    """
    def get_publisher(self):
        if not self.publishers:
            print("List is Empty.")
        else:
            print("\n========== Publisher Details ==========")
            for publisher in self.publishers:
                print(f"\nPublisher ID: {publisher['Publisher ID']}\nPublisher Name: {publisher['Publisher Name']}\nAddress: {publisher['Address']}\nGov Reg No: {publisher['Gov Reg No']}\nAgreement Period: {publisher['Agreement Time']}")
    """
    Handles publisher-related operation delete publisher.
    """
    def delete_publisher(self, publisher_id):
        print("\n========== Delete Publisher ==========")
        for publisher in self.publishers:
            if publisher_id == publisher['Author ID']:
                print(f"Publisher ID: {publisher_id}\nSuccessfully Deleted")
                self.publishers.remove(publisher)
            return f"Publisher is Not Found!"
"""
Handles publisher license-related operation to manage publisher license.
"""
class HandlePublisherLicense(HandlePublisher):
    def __init__(self, license_no=None, license_period=None):
        self.license_no = license_no
        self.license_period = license_period
        self.publishers = []
    """
    Handles publisher license-related operation add publisher license.
    """
    def add_publisher_license(self, license_no, license_period):
        print("\n========== Add Publisher License ==========")
        if license_no in self.publishers:
            print(f"Author Not Found!")
        else:
            publisher = {
                "License No": license_no,
                "License Period": license_period,
            }
            self.publishers.append(publisher)
            print(f"License '{license_no}' Added Successfully!")
            return
    """
    Handles publisher license-related operation update publisher license.
    """
    def update_publisher_license(self, license_no, license_period):
        print("\n========== Edit Publisher License ==========")
        for publisher in self.publishers:
            if publisher['License No'] == license_no:
                if license_no:
                    publisher["License No"] = license_no
                if license_period:
                    publisher["License Period"] = license_period
                print(f"License No: {license_no}\nLicense Period: {license_period}\n>>>>> Updated Successfully!")
        return f"Publisher Not Found"
    """
    Handles publisher license-related operation get all publisher license.
    """
    def get_publisher_license(self):
        if not self.publishers:
            print("List is Empty.")
        else:
            print("\n========== License Details ==========")
            for publisher in self.publishers:
                print(f"\nLicense No: {publisher['License No']}\nLicense Period: {publisher['License Period']}")