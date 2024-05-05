import re
import os


def read_contacts():
    contacts = {}
    try:
        with open('contacts_list.txt', 'r') as file:
            for line in file:
                data = re.search(r'([\w\s]+)-:-([\d-]+)-:-([\w\s@.]+)', line)
    except FileNotFoundError:
        print('No Local files')
        return {}
    else:
        print('Importing Local Data...')
        return contacts


def write_contacts(contacts):
    with open('contacts_list.txt', 'w') as file:
        for name, info in contacts.items():
            file.write(f"{info['Name']}-:-{info['Phone Number']}-:-{info['Email']}\n")


def add_contact(contacts):
    os.system('cls' if os.name == 'nt' else 'clear')
    name = input('Name of Contact: ')
    number = input('Number of Contact: ')
    email = input('Contact Email: ')
    contacts[name] = {'Name': name, 'Phone Number': number, 'Email': email}
    write_contacts(contacts)
    print(f'Added {name} to your contact list')


def display(contacts):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Contact List')
    print('------------')
    for idx, (name, info) in enumerate(contacts.items()):
        print(f"{idx+1}.) {info['Name']} Phone number is {info['Phone Number']} and their email is {info['Email']}")

def edit_contact(contacts):
    display(contacts)
    option = int(input("Select which contact you want to edit: "))
    contact = list(contacts.keys())[option-1]
    print(f"Editing {contact}:")
    new_name = input('New Name: ')
    new_number = input('New Number: ')
    new_email = input('New Email: ')
    contacts[contact] = {'Name': new_name, 'Phone Number': new_number, 'Email': new_email}
    write_contacts(contacts)
    print(f"{contact} edited successfully!")

def search_contact(contacts):
    search_query = input("Enter the name of the contact: ").lower()
    search_results = [info for name, info in contacts.items() if search_query in name.lower()]
    if search_results:
        print("Search Results:")
        for idx, result in enumerate(search_results):
            print(f"{idx+1}.) {result['Name']} Phone number is {result['Phone Number']} and their email is {result['Email']}")
    else:
        print("No contacts were found with that name.")


def remove_contact(contacts):
    display(contacts)
    option = int(input("Select which contact you want to remove: "))
    contact = list(contacts.keys())[option-1]
    del contacts[contact]
    print(f"Removed {contact}!")
    write_contacts(contacts)


def management():
    contacts = read_contacts()

    while True:
        print('''
    Welcome to the Contact Management System! 
    *****************************************
        Menu:
        1. Add a new contact
        2. Edit an existing contact
        3. Delete a contact
        4. Search for a contact
        5. Display all contacts
        6. Export contacts to a text file
        7. Import contacts from a text file
        8. Quit 
        ''')
        action = input("Enter your action: ")
        try:
            action = int(action)
            if action == 1:
                add_contact(contacts)
            elif action == 2:
                edit_contact(contacts)
            elif action == 3:
                remove_contact(contacts)
            elif action == 4:
                search_contact(contacts)
            elif action == 5:
                display(contacts)
            elif action == 6:
                write_contacts(contacts)
                print("Contacts exported successfully!")
            elif action == 7:
                contacts = read_contacts()
                print("Contacts imported successfully!")
            elif action == 8:
                print("Quitting Contact Application.")
                break
            else:
                print("Invalid Selection. Choose one of the given options.")
        except ValueError:
            print("Numbers only BoZo.")


management()
