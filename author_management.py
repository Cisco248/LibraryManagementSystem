"""
Module: AuthorManagement

This module handles the management of authors and licenses, including adding,
editing, listing, and deleting author and license details.
"""

class HandleAuthor:
    """
    Handles author-related operations such as adding, listing, updating, and deleting authors.
    """

    def __init__(self):
        """
        Initializes an instance of the HandleAuthor class.
        """
        self.authors = []

    def add_author(self, author_data):
        """
        Adds a new author to the system.

        Args:
            author_data (dict): A dictionary containing author details with keys:
                - 'author_id' (str): Unique identifier for the author.
                - 'author_name' (str): Name of the author.
                - 'address' (str): Address of the author.
                - 'gov_reg_no' (str): Government registration number of the author.
                - 'agreement_time' (str): Agreement time period with the author.

        Returns:
            str: Success message or error message if the author already exists.
        """
        print("\n========== Add Author ==========")
        if any(author['author_id'] == author_data['author_id'] for author in self.authors):
            print(f"Error: Author with ID '{author_data['author_id']}' already exists.")
            return
        self.authors.append(author_data)
        print(f"Author '{author_data['author_name']}' added successfully!")
        return

    def edit_author(self, author_id, updated_data):
        """
        Updates an existing author's details.

        Args:
            author_id (str): The ID of the author to update.
            updated_data (dict): A dictionary containing updated author details.

        Returns:
            str: Success message or error message if the author is not found.
        """
        print("\n========== Update Author ==========")
        for author in self.authors:
            if author['author_id'] == author_id:
                author.update({key: value for key, value in updated_data.items() if value})
                print(f"Author '{author_id}' updated successfully!")
                return
        print(f"Error: Author with ID '{author_id}' not found.")
        return

    def list_authors(self):
        """
        Lists all authors in the system.

        Returns:
            list: A list of author details or an empty list if no authors are found.
        """
        print("\n========== Author Details ==========")
        if not self.authors:
            print("No authors found.")
            return []
        for author in self.authors:
            print(f"\nAuthor ID: {author['author_id']}\nAuthor Name: {author['author_name']}\n"
                  f"Address: {author['address']}\nGov Reg No: {author['gov_reg_no']}\n"
                  f"Agreement Period: {author['agreement_time']}")
        return self.authors

    def delete_author(self, author_id):
        """
        Deletes an author from the system.

        Args:
            author_id (str): The ID of the author to delete.

        Returns:
            str: Success message or error message if the author is not found.
        """
        print("\n========== Delete Author ==========")
        for author in self.authors:
            if author['author_id'] == author_id:
                self.authors.remove(author)
                print(f"Author with ID '{author_id}' deleted successfully.")
                return
        print(f"Error: Author with ID '{author_id}' not found.")
        return

class HandleLicense:
    """
    Handles license-related operations such as adding, updating, and listing licenses.
    """

    def __init__(self):
        """
        Initializes an instance of the HandleLicense class.
        """
        self.licenses = []

    def add_license(self, license_data):
        """
        Adds a new license to the system.

        Args:
            license_data (dict): A dictionary containing license details with keys:
                - 'license_no' (str): The license number.
                - 'license_period' (str): The validity period of the license.

        Returns:
            str: Success message or error message if the license already exists.
        """
        print("\n========== Add License ==========")
        if any(license_['license_no'] == license_data['license_no'] for license_ in self.licenses):
            return f"Error: License with number '{license_data['license_no']}' already exists."
        self.licenses.append(license_data)
        print(f"License '{license_data['license_no']}' added successfully!")

    def update_license(self, license_no, updated_data):
        """
        Updates an existing license's details.

        Args:
            license_no (str): The license number to update.
            updated_data (dict): A dictionary containing updated license details.

        Returns:
            str: Success message or error message if the license is not found.
        """
        print("\n========== Update License ==========")
        for license_ in self.licenses:
            if license_['license_no'] == license_no:
                license_.update({key: value for key, value in updated_data.items() if value})
                print(f"License '{license_no}' updated successfully!")
                return
        print(f"Error: License with number '{license_no}' not found.")
        return

    def list_licenses(self):
        """
        Lists all licenses in the system.

        Returns:
            list: A list of license details or an empty list if no licenses are found.
        """
        print("\n========== License Details ==========")
        if not self.licenses:
            print("No licenses found.")
            return []
        for license_ in self.licenses:
            print(f"\nLicense No: {license_['license_no']}\nLicense Period: {license_['license_period']}")
        return self.licenses
