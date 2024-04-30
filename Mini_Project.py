import re
import os


def read_contacts():
    contacts = {}
    try:
        with open('contacts_list.txt', 'r') as file:
            for line in file:
                data = re.search(r'([\w\s]+)-:-([\d-]+)-:-([\w\s@.]+)', line)
                contacts[name] = {'Name': data.group(1), 'Phone Number': data.group(2), 'Email': data.group(3)}
    except FileNotFoundError:
        print('No Local files')
        return {}
    else:
        print('Importing Local Data...')
        return contacts

def write_contacts(contacts):
    with open('contacts_list.txt', 'w') as file:
        for name, info in contacts.items():
            file.write(f"{name}-:-{info['Phone Number']}-:-{info['Email']}\n")

def add_contact(contacts):
    os.system('cls')
    name = input('Name of Contact: ')
    number = input('number of contact: ')
    email = input('Contacts Email: ')
    contacts[name] = {'Phone Number': number, 'Email': email}
    write_contacts(contacts)
    print(f'Added {name} to your contact list')

def display(contacts):
    os.system('cls')
    print('Contact List')
    print('------------')
    for idx, info in enumerate(contacts.items()):
        print(f"{idx+1}.) {info['Name']} Phone number is {info['Phone Number']} and their email is {info['Email']}")

def remove_contact(contacts):
    display(contacts)
    option = input("Select which contact you want to remove: ")
    contact = contacts.pop(option-1)
    print(f"Removed {contact['Name']}!")
    write_contacts(contacts)






def management():
    
    contacts = {}
    
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
                pass
            elif action == 3:
                remove_contact(contacts)
            elif action == 4:
                pass
            elif action == 5:
                display(contacts)
                pass
            elif action == 8:
                print("Quitting Contact Application.")
                break
            else:
                print("Invalid Selection. Choose one of the given options.")
        except ValueError:
            print("Numbers only BoZo")








management()
