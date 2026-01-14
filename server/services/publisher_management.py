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

    def add_publisher(self, publisher_id, publisher_name, address, gov_reg_no, agreement_time):
        """
        Adds a new publisher to the list.

        Args:
            publisher_id (str): Unique identifier for the publisher.
            publisher_name (str): Name of the publisher.
            address (str): Address of the publisher.
            gov_reg_no (str): Government registration number.
            agreement_time (str): Agreement period with the publisher.
        """
        print("\n========== Add Publisher ==========")
        if any(publisher['Publisher ID'] == publisher_id for publisher in self.publishers):
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

    def edit_publisher(self, publisher_id, new_publisher_name=None, new_address=None, new_gov_reg_no=None, new_agreement_time=None):
        """
        Edits the details of an existing publisher.

        Args:
            publisher_id (str): The ID of the publisher to be updated.
            new_publisher_name (str, optional): New name of the publisher.
            new_address (str, optional): New address of the publisher.
            new_gov_reg_no (str, optional): New government registration number.
            new_agreement_time (str, optional): New agreement period.
        """
        print("\n========== Update Publisher ==========")
        for publisher in self.publishers:
            if publisher['Publisher ID'].lower() == publisher_id.lower():
                if new_publisher_name:
                    publisher["Publisher Name"] = new_publisher_name
                if new_address:
                    publisher["Address"] = new_address
                if new_gov_reg_no:
                    publisher["Gov Reg No"] = new_gov_reg_no
                if new_agreement_time:
                    publisher["Agreement Time"] = new_agreement_time
                print(f"Publisher ID: {publisher_id}\nPublisher Name: {new_publisher_name}\nAddress: {new_address}\nGov Reg No: {new_gov_reg_no}\nAgreement Period: {new_agreement_time}\n>>>>> Updated Successfully!")
                return
        print("Publisher Not Found")

    def get_publisher(self):
        """
        Retrieves all publisher details.

        Returns:
            None: Prints publisher details.
        """
        if not self.publishers:
            print("List is Empty.")
        else:
            print("\n========== Publisher Details ==========")
            for publisher in self.publishers:
                print(f"\nPublisher ID: {publisher['Publisher ID']}\nPublisher Name: {publisher['Publisher Name']}\nAddress: {publisher['Address']}\nGov Reg No: {publisher['Gov Reg No']}\nAgreement Period: {publisher['Agreement Time']}")

    def delete_publisher(self, publisher_id):
        """
        Deletes a publisher from the list.

        Args:
            publisher_id (str): The ID of the publisher to delete.
        """
        print("\n========== Delete Publisher ==========")
        for publisher in self.publishers:
            if publisher['Publisher ID'] == publisher_id:
                print(f"Publisher ID: {publisher_id}\nSuccessfully Deleted")
                self.publishers.remove(publisher)
                return
        print(f"Publisher ID '{publisher_id}' Not Found!")


class HandlePublisherLicense(HandlePublisher):
    """
    Manages publisher license-related operations.
    """
    def __init__(self, license_no=None, license_period=None, publisher_id=None):
        """
        Initializes a publisher license handler.

        Args:
            license_no (str): License number.
            license_period (str): License duration.
            publisher_id (str): ID of the publisher.
        """
        super().__init__(publisher_id=publisher_id)  # Call the parent class constructor
        self.license_no = license_no
        self.license_period = license_period

    def add_publisher_license(self, license_no, license_period):
        """
        Adds a license to a publisher.

        Args:
            license_no (str): License number.
            license_period (str): License period.
        """
        print("\n========== Add Publisher License ==========")
        if any(publisher['License No'] == license_no for publisher in self.publishers):
            print(f"License Already Exists!")
        else:
            publisher = {
                "License No": license_no,
                "License Period": license_period,
            }
            self.publishers.append(publisher)
            print(f"License '{license_no}' Added Successfully!")

    def update_publisher_license(self, license_no, license_period):
        """
        Updates the publisher license details.

        Args:
            license_no (str): License number.
            license_period (str): License period.
        """
        print("\n========== Edit Publisher License ==========")
        for publisher in self.publishers:
            if publisher['License No'] == license_no:
                publisher["License Period"] = license_period
                print(f"License No: {license_no}\nLicense Period: {license_period}\n>>>>> Updated Successfully!")
                return
        print("License Not Found")

    def get_publisher_license(self):
        """
        Retrieves all publisher licenses.

        Returns:
            None: Prints publisher license details.
        """
        if not self.publishers:
            print("List is Empty.")
        else:
            print("\n========== License Details ==========")
            for publisher in self.publishers:
                print(f"\nLicense No: {publisher['License No']}\nLicense Period: {publisher['License Period']}")
