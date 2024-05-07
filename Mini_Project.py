import re
import os


def read_contacts():
    contacts = {}
    try:
        with open('contacts_list.txt', 'r') as file:
            for line in file:
                data = re.search(r'([\w\s]+)-:-([\d-]+)-:-([\w\s@.]+)', line)

def write_contacts(contacts):
    with open('contacts_list.txt', 'w') as file:
        for name, info in contacts.items():
            file.write(f"{info['Name']}-:-{info['Phone Number']}-:-{info['Email']}\n")


def add_contact(contacts): 
    name = input('Name of Contact: ') # asking the user to enter the contacts info.
    number = input('Number of Contact: ')
    email = input('Contact Email: ')
    contacts[name] = {'Name': name, 'Phone Number': number, 'Email': email}
    write_contacts(contacts)
    print(f'Added {name} to your contact list')


def display(contacts):
    print('Contact List')
    print('------------')
    for idx, (name, info) in enumerate(contacts.items()):
        print(f"{idx+1}.) {info['Name']} Phone number is {info['Phone Number']} and their email is {info['Email']}")

def edit_contact(contacts):
    display(contacts)
    option = int(input("Select which contact you want to edit: ")) # asking the user to pick a contact that they would like to edit.
    contact = list(contacts.keys())[option-1]
    print(f"Editing {contact}:")
    new_name = input('New Name: ')
    new_number = input('New Number: ')
    new_email = input('New Email: ')
    contacts[contact] = {'Name': new_name, 'Phone Number': new_number, 'Email': new_email}
    write_contacts(contacts)
    print(f"{contact} edited successfully!")

def search_contact(contacts):
    search_query = input("Enter the name of the contact: ").lower()# able to search for a contact in the contacts lists and used .lower() so incase they used caps, there wouldn't be any errors
    search_results = [info for name, info in contacts.items() if search_query in name.lower()] 
    if search_results:
        print("Search Results:")
        for idx, result in enumerate(search_results):
            print(f"{idx+1}.) {result['Name']} Phone number is {result['Phone Number']} and their email is {result['Email']}")
    else:
        print("No contacts were found with that name.")


def remove_contact(contacts):
    display(contacts) #letting the user be able to delete a contact they no longer want in their contacts
    option = int(input("Select which contact you want to remove: "))
    contact = list(contacts.keys())[option-1]
    del contacts[contact] # using the del function to delete a certain contact. I tried using the pop() but wasn't working for me
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
        6. Quit 
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
                print("Quitting Contact Application.")
                break
            else:
                print("Invalid Selection. Choose one of the given options.")
        except ValueError:
            print("Numbers only BoZo.")


management()
