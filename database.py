import json
import os

BOOK_FILE = "data/books.json"
MEMBER_FILE = "data/members.json"

def load_data(file_name):

    # Create file if it does not exist
    if not os.path.exists(file_name):

        os.makedirs("data", exist_ok=True)

        with open(file_name, "w") as file:
            json.dump([], file, indent=4)

        return []

    # Check if file is empty
    if os.path.getsize(file_name) == 0:
        return []

    try:

        with open(file_name, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:

        print("Warning: Data file contains invalid JSON.")
        print("Starting with empty data.")

        return []


def save_data(file_name, data):

    os.makedirs("data", exist_ok=True)

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def load_books():
    return load_data(BOOK_FILE)


def save_books(books):
    save_data(BOOK_FILE, books)


def load_members():
    return load_data(MEMBER_FILE)


def save_members(members):
    save_data(MEMBER_FILE, members)