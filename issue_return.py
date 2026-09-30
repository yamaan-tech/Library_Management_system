from database import load_books, save_books


def issue_book():

    print("\n--- Issue Book ---")

    books = load_books()

    book_id = input("Enter Book ID: ")

    for book in books:

        if book["id"] == book_id:

            if book["status"] == "Available":

                book["status"] = "Issued"
                save_books(books)

                print("Book issued successfully.")

            else:
                print("Book is already issued.")

            return

    print("Book not found.")


def return_book():

    print("\n--- Return Book ---")

    books = load_books()

    book_id = input("Enter Book ID: ")

    for book in books:

        if book["id"] == book_id:

            if book["status"] == "Issued":

                book["status"] = "Available"
                save_books(books)

                print("Book returned successfully.")

            else:
                print("Book is already available.")

            return

    print("Book not found.")
