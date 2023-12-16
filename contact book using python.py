contacts = {}

def display_contacts():
    print("Name\n\nContact number")
    for key in contacts:
        print(f"{key}\n\n{contacts[key]}")

while True:
    choice = int(input("1. Add new Contact\n2. Search Contact\n3. Display Contact\n4. Edit Contact\n5. Delete Contact\n6. Exit\nEnter your choice: "))

    if choice == 1:
        name = input("Enter the contact name: ")
        phone = input("Enter the Mobile Number: ")
        contacts[name] = phone
    elif choice == 2:
        search_name = input('Enter the contact name: ')
        if search_name in contacts:
            print(f"{search_name}'s contact number is {contacts[search_name]}")
        else:
            print("The name is not found in the contact book")
    elif choice == 3:
        if not contacts:
            print("Empty contact book")
        else:
            display_contacts()
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited: ")
        if edit_contact in contacts:
            new_phone = input('Enter the new mobile number: ')
            contacts[edit_contact] = new_phone
            print('Contact updated')
            display_contacts()
        else:
            print("The name is not found in the contact book")
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted: ")
        if del_contact in contacts:
            confirm = input("Do you want to delete this contact? (y/n): ")
            if confirm.lower() == 'y':
                contacts.pop(del_contact)
                display_contacts()
        else:
            print("Name is not found in the contact book")
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please enter a valid option.")

