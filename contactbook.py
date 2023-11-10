# First Let's create a blank list contacts. We will add/append new contacts to this list.
contacts = []

def display_menu():  # This is the menu for our contact book app.Here user will select the acton he wants to perform.
    print("Contact Book Menu")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Display all contacts")
    print("6. Exit")

def add_contact():
    """
    This function will be used to add new contact to our contacts list.
    We are asking the user to input contact details.
    """
    name = input("Enter the contact's name: ")
    email = input("Enter the contact's email: ")
    phone = input("Enter the contact's phone number: ")
    contact = {"Name": name, "Email": email, "Phone": phone}  # We are creating a dictionary using above informations
    contacts.append(contact)  # Then we are adding the individuall contact information in a dictionary format to our contacts list
    print("Contact added successfully!")


def search_contact():
    """
    This function will be used to search the existing contact from our contact book list.
    The user can enter either name or email address to search the contact.
    """
    search_term = input("Enter the name or email of the contact to search: ") # Asking user to input the search term.
    found_contacts = []  # We are taking a blank list.Here we will store all the contacts that are matching with our search term.
    for contact in contacts: # Loop through each contact stored in the contacts list and match with name or email with our search term
        if search_term.lower() in contact["Name"].lower() or search_term.lower() in contact["Email"].lower():
            found_contacts.append(contact)  # Append the matching search result to the found_contacts declared above at line no 7

    if found_contacts:  # Checking if any contact is the in the found_contacts list.
        print("Matching contacts found:")
        for contact in found_contacts:  # Looping through the found_contacts list to print each contact details that is matchoing our search term.
            print("Name:", contact["Name"])
            print("Email:", contact["Email"])
            print("Phone:", contact["Phone"])
            print("-------------------")
    else:
        print("No matching contacts found.")


def update_contact():
    """
    This function will be used to edit/update the existing contact in our contacts list.
    First we will search the contact if exists, if found we will update the new details.
    """
    name = input("Enter the name of the contact to update: ") # Prompting the user to enter the name to update
    found_contact = None # Initiating a new variable with intial value None
    for contact in contacts: # Looping through the contacts list to find out if the searched contact exist.
        if contact["Name"].lower() == name.lower():
            found_contact = contact  # Assigning the found contact from the contacts list to new variable found_contact
            break

    if found_contact:  # Checking if the found_contact variable has a value other than none, Then asking user to input new contact details
        print("Contact found. Enter new details:")
        found_contact["Name"] = input("Enter the new name: ")
        found_contact["Email"] = input("Enter the new email: ")
        found_contact["Phone"] = input("Enter the new phone number: ")
        print("Contact updated successfully!")
    else:
        print("Contact not found.")


def delete_contact():
    """
    We will use this function to delete a contact from our contacts list.
    We will search the contact by name, then if found then delete it.
    """
    name = input("Enter the name of the contact to delete: ")  # Prompt the user to enter the contact name which he want to delete
    for contact in contacts:  # Loop thorough the contacts list to find out the serached contact
        if contact["Name"].lower() == name.lower():  # Contact found then remove from the list in next line
            contacts.remove(contact)   # Remove the found contact from contacts list
            print("Contact deleted successfully!")
            break
    else:
        print("Contact not found.") 


def display_all_contacts():
    """
    This function will display all the contacts stored in our contacts list.
    Simply select the choice to display all contacts
    """
    if contacts:
        print("All Contacts:")
        for contact in contacts:  # Loop through the contacts list and fetch all the contacts ,then display them one by one
            print("Name:", contact["Name"])
            print("Email:", contact["Email"])
            print("Phone:", contact["Phone"])
            print("-------------------")  # Separator between each contact
    else:
        print("No contacts found.")


# Main program loop
while True:
    """
    This is the main part or entry point to our application. When we will run this file it will from this point.
    This is an infinite loop,it will continue untill we give the choice "6". Based on user choice respective function will get called.
    """
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_all_contacts()
    elif choice == "6":
        print("Exiting the program...")
        break  # Exits the program when choice given "6"
    else:
        print("Invalid choice. Please enter a valid option (1-6).")                                      