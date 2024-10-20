class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact}")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            deleted_contact = self.contacts.pop(index)
            print(f"Contact {deleted_contact.name} deleted successfully!")
        else:
            print("Invalid index. Please try again.")

def main():
    manager = ContactManager()
    while True:
        print("\nContact Manage:r")
        print("1. Add Contact:")
        print("2. View Contacts:")
        print("3. Delete Contact:")
        print("4. --Exit--")
        choice = input("Choose an option (1 to 4): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            index = int(input("Enter contact index to delete: ")) - 1
            manager.delete_contact(index)
        elif choice == '4':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
