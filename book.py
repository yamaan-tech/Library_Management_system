from database import load_books, save_books
from validation import book_id_exists


def add_book():

    print("\n--- Add Book ---")

    books = load_books()

    book_id = input("Enter Book ID: ")

    if book_id_exists(books, book_id):
        print("Book ID already exists")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    category = input("Enter Category: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "status": "Available"
    }

    books.append(book)
    save_books(books)

    print("Book added successfully")


def view_books():

    print("\n--- All Books ---")

    books = load_books()

    if len(books) == 0:
        print("No books available.")
        return

    for book in books:

        print("----------------------------")
        print("Book ID  :", book["id"])
        print("Title    :", book["title"])
        print("Author   :", book["author"])
        print("Category :", book["category"])
        print("Status   :", book["status"])


def update_book():

    print("\n--- Update Book ---")

    books = load_books()

    book_id = input("Enter Book ID: ")

    for book in books:

        if book["id"] == book_id:

            book["title"] = input("Enter new title: ")
            book["author"] = input("Enter new author: ")
            book["category"] = input("Enter new category: ")

            save_books(books)

            print("Book updated successfully")
            return

    print("Book not found.")


def delete_book():

    print("\n--- Delete Book ---")

    books = load_books()

    book_id = input("Enter Book ID: ")

    for book in books:

        if book["id"] == book_id:

            books.remove(book)
            save_books(books)

            print("Book deleted successfully")
            return

    print("Book not found.")
