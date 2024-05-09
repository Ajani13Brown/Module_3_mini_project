import re
import os

def read_contacts():
    contact_list= {}
    try:
        with open('contact_list.txt','r') as file:
            for line in file:
                data = re.search(r'([\w\s]+)-:-([a-zA-Z\.0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+)-:-(\d{3}-\d{3}-\d{4})', line)
                contact_list[data.group(1)]= {'Email': data.group(2).strip(), 'Phone Number': data.group(3).strip()}
    except: 
        print("file not found or unable to be read")
    else:
        print('Importing Local Data...')
        return(contact_list)

def write_contacts(contact_list):
    with open('contact_list.txt', 'w') as file:
        for name, details in contact_list.items():
            print(name,details)
            file.write(f"{name}-:-{details['Email']}-:-{details['Phone Number']}\n")


def add_contact(contact_list):
    os.system('cls')
    name = input('Name: ')
    email = input('what is your email? ')
    number = input('what is your number? (xxx-xxx-xxxx) ')
    contact_list[name] = {'Email': email, 'Phone Number': number}
    write_contacts(contact_list)
    print(f'Added {name} to your contacts')

def view(contact_list):
    os.system('cls')
    print('Contacts')
    print('------------')
    display_contacts = read_contacts()
    print(display_contacts)
    if display_contacts is None:
        raise TypeError('No contacts in list or contacts failed to load')
    for name, details in display_contacts.items():
        print(f"Name:{name}, Email:{details['Email']}, Phone #:{details['Phone Number']}")
    print('All contacts in list displayed')

def remove_contact(contact_list):
    os.system('cls')
    contact_list = read_contacts()
    if contact_list is None:
        raise TypeError ('Contact list is empty there are no contact to search')
    for index, name in enumerate(contact_list.keys(), start=1):
        print(f"{index}.) {name}")
    remove = input('which contact would you like to remove: ')
    if remove in contact_list:
        contact_list = contact_list.pop(remove)
        print(f"Removed {remove} from contacts.")
    write_contacts(contact_list)

def search_contact(contact_list):
    os.system('cls')
    read_contacts()
    #contact_list = read_contacts()
    if contact_list is None:
        raise TypeError ('Contact list is empty there are no contact to search')
    search_name = input("Enter the name you wish to search: ")
    for name in contact_list.keys():
        if search_name == name:
            print('Reteiving contact details')
            print(f'Name: {search_name}')
            print(f"Email: {contact_list['Email']}")
            print(f"Phone Nmber: {contact_list['Phone Number']}")
    else:
        print(f'Sorry {search_name} is not in your contacts list')

def edit_contact(contact_list):
    os.system('cls')
    read_contacts()
    print(contact_list)
    if contact_list is None:
        raise TypeError ('Contact list is empty there are no contact to search')
    for name in contact_list.keys():
        print(name)
        edit_choice = input('Enter the name of the contact that you would like to edit: ')
        if edit_choice in contact_list:
            print('Editing this contact will overwrite the old contact information')
            print('Would you like to continue or do you wish to stop')
            continue_edit = int(input('1 = continue, 2 = stop: '))
            if continue_edit == 1:
                print('Ok this contact will be ovefrwritten')
                contact_list = contact_list.pop(edit_choice)
                name = input('Name: ')
                email = input('what is your email? ')
                number = input('what is your number? ')
                contact_list[name] = {'Email': email, 'Number': number}
                write_contacts(contact_list)
                print(f'{name}  has been edited your contacts')
            elif continue_edit == 2:
                print('Ok this contact will not be edited and info will not be overwritten')
                break


def contact_managment_sys():
    
    contact_list = {}

    while True:
        option = input('''
        Welcome to the Contact Management System! 
        What feature would you like to use?
        
            Options:
        ---------------------
        1: Add a new contact
        2: Edit an existing contact
        3: Delete a contact
        4: Search for a contact
        5: Display all contacts
        6: Quit 
        >  ''') 
        if option == "1":
            add_contact(contact_list)
        elif option == "2":
            edit_contact(contact_list)
        elif option == "3":
            remove_contact(contact_list)
        elif option == "4":
            search_contact(contact_list)
        elif option == "5":
            view(contact_list)
        elif option == "6":
            print('Thank you for using the Contact Management System have a nice day.')
            break
    


contact_managment_sys()

# Project incomplete my read_contact function have an error went i attemp to run it it comes up as file not found
# i spent a significant amout of time try to correct the error but was unable to.
#I continued to work on the code so you could at least see what i was able to come up with but the appication unfortunatly 
# has a lot of error.