from database import load_members, save_members

def add_member():

    print("\n--- Add Member ---")
    members = load_members()

    member_id = input("Enter Member ID: ")

    for member in members:

        if member["id"] == member_id:
            print("Member ID already exists")
            return

    name = input("Enter Member Name: ")
    phone = input("Enter Phone Number: ")

    member = {
        "id": member_id,
        "name": name,
        "phone": phone
    }

    members.append(member)
    save_members(members)

    print("Member added successfully")


def view_members():

    print("\n--- All Members ---")
    members = load_members()

    if len(members) == 0:
        print("No members available.")
        return

    for member in members:

        print("----------------------------")
        print("Member ID :", member["id"])
        print("Name      :", member["name"])
        print("Phone     :", member["phone"])
