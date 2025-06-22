slam_book = {}

def add_entry():
    name = input("Enter your name: ")
    answer = input("Enter your answer to the question: ")
    slam_book[name] = answer
    print("Entry added.")

def display_entries():
    if not slam_book:
        print("No entries yet.")
        return
    for name, answer in slam_book.items():
        print(f"Name: {name}, Answer: {answer}")

def search_entry():
    name = input("Enter the name to search for: ")
    if name in slam_book:
        print(f"Name: {name}, Answer: {slam_book[name]}")
    else:
        print("Name not found.")

def main():
    while True:
        print("\nSlam Book Menu:")
        print("1. Add Entry")
        print("2. Display Entries")
        print("3. Search Entry")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            display_entries()
        elif choice == '3':
            search_entry()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    