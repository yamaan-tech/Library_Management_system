from book import add_book, view_books, update_book, delete_book
from member import add_member, view_members
from issue_return import issue_book, return_book
from search import search_book


def main():

    while True:

        print("\n======================================")
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("======================================")

        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("6. Add Member")
        print("7. View Members")
        print("8. Issue Book")
        print("9. Return Book")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            update_book()

        elif choice == "4":
            delete_book()

        elif choice == "5":
            search_book()

        elif choice == "6":
            add_member()

        elif choice == "7":
            view_members()

        elif choice == "8":
            issue_book()

        elif choice == "9":
            return_book()

        elif choice == "10":
            print("Thank you for using Library Management System")
            break

        else:
            print("Wrong choice. Please try again.")


# if __name__ == "__main__":
main()
