from database import load_books


def search_book():

    print("\n--- Search Book ---")

    books = load_books()

    keyword = input("Enter title, author or category: ").lower()

    found = False

    for book in books:

        if (keyword in book["title"].lower()
                or keyword in book["author"].lower()
                or keyword in book["category"].lower()):

            print("\nBook Found")
            print("Book ID  :", book["id"])
            print("Title    :", book["title"])
            print("Author   :", book["author"])
            print("Category :", book["category"])
            print("Status   :", book["status"])

            found = True

    if not found:
        print("No matching book found.")
