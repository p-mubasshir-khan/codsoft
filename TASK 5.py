class ContactBook:
    def __init__(phone):
        phone.contacts = {}

    def add_contact(phone):
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        phone.contacts[name] = {"phone": phone}
        print("Contact added successfully!")

    def view_contacts(phone):
        if not phone.contacts:
            print("No contacts in the contact book.")
        else:
            print("Contact List:")
            for name, details in phone.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(phone):
        search_term = input("Enter name or phone number to search: ")
        found = False
        for name, details in phone.contacts.items():
            if search_term in name or search_term in details["phone"]:
                print(f"Name: {name}, Phone: {details['phone']}")
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(phone):
        name = input("Enter contact name to update: ")
        if name in phone.contacts:
            phone = input("Enter new phone number: ")
            phone.contacts[name] = {"phone": phone}
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(phone):
        name = input("Enter contact name to delete: ")
        if name in phone.contacts:
            del phone.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.search_contact()
        elif choice == '4':
            contact_book.update_contact()
        elif choice == '5':
            contact_book.delete_contact()
        elif choice == '6':
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()