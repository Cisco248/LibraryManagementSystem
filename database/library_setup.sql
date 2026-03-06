CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

DROP TABLE IF EXISTS books;

-- table formed as per the csv
CREATE TABLE books (
    isbn VARCHAR(20) NOT NULL,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    publisher VARCHAR(100),
    publication_year INT, 
    -- BookType is converted to lower enum 
    book_type ENUM('ebook', 'hardcover', 'paperback') NOT NULL,
    -- Status is converted to lower enum 
    status ENUM('available', 'borrowed', 'reserved') NOT NULL DEFAULT 'available',
    format VARCHAR(20),
    size VARCHAR(20),
    PRIMARY KEY (isbn)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Inserting data manually
INSERT INTO books (isbn, title, author, publisher, publication_year, book_type, status, format, size) 
VALUES 
('978-0-123456-78-9', 'Python Programming', 'John Doe', 'Tech Books', 2023, 'ebook', 'available', 'PDF', '5.2 MB'),
('978-0-987654-32-1', 'Data Science Basics', 'Jane Smith', 'Data Press', 2022, 'hardcover', 'borrowed', NULL, NULL),
('978-1-111111-11-1', 'Web Development', 'Bob Johnson', 'Web Publishers', 2024, 'ebook', 'available', 'EPUB', '3.8 MB'),
('978-2-222222-22-2', 'Machine Learning', 'Alice Brown', 'AI Books', 2023, 'paperback', 'available', NULL, NULL),
('978-3-333333-33-3', 'Database Design', 'Charlie Wilson', 'Tech Press', 2021, 'ebook', 'reserved', 'PDF', '7.1 MB');

SELECT * FROM books;