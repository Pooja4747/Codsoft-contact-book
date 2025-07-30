import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def show_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

def search_contacts(contacts):
    query = input("Enter name to search: ").lower()
    results = [c for c in contacts if query in c["name"].lower()]
    if results:
        print("Search results:")
        show_contacts(results)
    else:
        print("No contacts found with that name.")

def delete_contact(contacts):
    show_contacts(contacts)
    index = int(input("Enter contact number to delete: ")) - 1
    if 0 <= index < len(contacts):
        removed = contacts.pop(index)
        save_contacts(contacts)
        print(f"Deleted contact: {removed['name']}")
    else:
        print("Invalid contact number.")

def main():
    contacts = load_contacts()

    while True:
        print("\n📒 Contact Book")
        print("1. Show All Contacts")
        print("2. Add New Contact")
        print("3. Search Contact by Name")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
