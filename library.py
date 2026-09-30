from database import load_books, load_members


def find_book(book_id):
    """
    Find a book using Book ID.
    Returns the book if found, otherwise returns None.
    """

    books = load_books()

    for book in books:

        if book["id"] == book_id:
            return book

    return None


def find_member(member_id):
    """
    Find a member using Member ID.
    Returns the member if found, otherwise returns None.
    """

    members = load_members()

    for member in members:

        if member["id"] == member_id:
            return member

    return None


def check_book_available(book_id):
    """
    Check whether a book is available for issue.
    """

    book = find_book(book_id)

    if book is None:
        return False

    if book["status"] == "Available":
        return True

    return False


def get_library_summary():
    """
    Return basic library statistics.
    """

    books = load_books()
    members = load_members()

    total_books = len(books)
    available_books = 0
    issued_books = 0
    total_members = len(members)

    for book in books:

        if book["status"] == "Available":
            available_books += 1

        elif book["status"] == "Issued":
            issued_books += 1

    summary = {
        "total_books": total_books,
        "available_books": available_books,
        "issued_books": issued_books,
        "total_members": total_members
    }

    return summary