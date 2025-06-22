phonebook = {}

def add_contact(name, number):
    """Adds a new contact to the phonebook."""
    phonebook[name] = number
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    """Displays all contacts in the phonebook."""
    if not phonebook:
        print("Phonebook is empty.")
        return
    print("\n--- Your Contacts ---")
    for name, number in phonebook.items():
        print(f"Name: {name}, Phone: {number}")
    print("---------------------\n")

def search_contact(name):
    """Searches for a contact by name and displays their number."""
    if name in phonebook:
        print(f"Phone number for '{name}': {phonebook[name]}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    """Deletes a contact from the phonebook."""
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter phone number: ")
            add_contact(name, number)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '5':
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()