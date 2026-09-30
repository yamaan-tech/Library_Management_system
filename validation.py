def book_id_exists(books, book_id):

    for book in books:

        if book["id"] == book_id:
            return True

    return False


def member_id_exists(members, member_id):

    for member in members:

        if member["id"] == member_id:
            return True

    return False


def check_empty(value):

    if value.strip() == "":
        return True

    return False
