# Library Management System

## Project Overview

Library Management System is a Python-based console application developed to manage books and library members.

The system provides features for adding, updating, deleting, searching, issuing, and returning books. It also provides basic reports and stores data using JSON files.

## Features

* Add Book
* View Books
* Update Book
* Delete Book
* Search Book
* Add Member
* View Members
* Issue Book
* Return Book
* Library Reports
* JSON Data Storage
* Input Validation
* Basic Testing

## Technologies Used

* Python
* JSON
* File Handling
* Git
* GitHub

## Project Structure

```text
Library-Management-System/
│
├── main.py
├── book.py
├── member.py
├── library.py
├── issue_return.py
├── search.py
├── validation.py
├── report.py
├── database.py
│
├── data/
│   ├── books.json
│   └── members.json
│
├── tests/
│   └── test_library.py
│
├── README.md
└── statement.md
```

## How to Run

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

### Step 2: Open the Project

```bash
cd Library-Management-System
```

### Step 3: Run the Application

```bash
python main.py
```

## Main Menu

The application provides the following options:

```text
1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Search Book
6. Add Member
7. View Members
8. Issue Book
9. Return Book
10. Reports
11. Exit
```

## Testing

Basic tests are available inside the `tests` folder.

The tests verify:

* Book status
* Book issue operation
* Book return operation

## Data Storage

The project uses JSON files for storing:

* Book information
* Member information

Example:

```text
data/books.json
data/members.json
```

## Future Enhancements

The project can be extended with:

* Login system
* Admin and member roles
* Database integration using MySQL
* Due-date management
* Fine calculation
* Email notifications
* Graphical user interface
* Web-based version

## Author

Student Name: Yamaan Shaikh

Course: cse core

College: Vellore Institute of Technology Bhopal

Year: 26-27
