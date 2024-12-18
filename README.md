# Library Management System

## Overview

The Library Management System is a Python-based application designed to manage books and members in a library. It provides functionalities for adding, updating, and deleting books, managing member records, and tracking borrowed books.

## Features

### Book Management

- Add Books: Add new books with details like title, ISBN, author, category, and status.
- Update Book Details: Modify book information such as title, author, category, and status.
- Delete Books: Remove books from the library.
- Find Books: Search for books by ISBN.
- View All Books: List all books in the library.

### Member Management

- Add Members: Add new members with details like name, contact number, age, and membership type.
- Borrow Books: Track books borrowed by members.
- Return Books: Update the status of books returned by members.
- Display Member Details: View member details including borrowed books.

### Additional Features

- Comprehensive error handling for invalid inputs.
- Modular design for scalability and maintainability.

## Installation

1. Clone the repository:

    `git clone https://github.com/your-username/library-management-system.git`

2. Navigate to the project directory:

    `cd library-management-system`

3. Ensure you have Python 3.6 or higher installed.

## Usage

1. Run the application:

    `python App.py`

2. Follow the on-screen instructions to interact with the system.

## Project Structure

```
        library-management-system/
        ├── Diagrams/                        # Project Diagram
        │   ├── 22UG2-0004_ClassDiagram.png  # Book management module
        |
        ├── BookManagement.py                # Book management module
        ├── MemberManagement.py              # Member management module
        ├── PublisherManagement.py           # Publisher management module
        ├── AuthorManagement.py              # Author management module
        ├── App.py                           # Main application file
        └── .gitignore                       # Git ignore file
```

## Example Usage
```
        ========== Add Book ==========
        Enter Title: The Great Gatsby
        Enter ISBN: 123456
        Enter Author: F. Scott Fitzgerald
        Enter Category: Fiction
        Enter Status: Available
        Book 'The Great Gatsby' Added Successfully!
```
```
        ========== Borrow a Book ==========
        Member: Alice
        Book: The Great Gatsby
        Book 'The Great Gatsby' borrowed by Alice.
```
## Future Enhancements

- Add a GUI using a library like Tkinter or PyQt.
- Integrate with a database for persistent storage.
- Implement authentication for staff and members.

## Contributing

1. Fork the repository.

2. Create a new branch for your feature/bug fix:

    `git checkout -b feature-name`

3. Commit your changes:

    `git commit -m "Description of changes"`

4. Push to your branch:

    `git push origin feature-name`

5. Create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Python documentation: <https://docs.python.org/3/>
- Community contributions and suggestions.
