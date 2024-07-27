class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")
    
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("----- Contact List -----")
            for contact in self.contacts:
                print(contact)
                print("------------------------")
    
    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                print(contact)
                found = True
        if not found:
            print(f"No contacts found with '{search_term}'.")
    
    def update_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                new_name = input(f"Enter new name for '{contact.name}' (press enter to keep '{contact.name}'): ").strip()
                new_phone_number = input(f"Enter new phone number for '{contact.name}' (press enter to keep '{contact.phone_number}'): ").strip()
                new_email = input(f"Enter new email for '{contact.name}' (press enter to keep '{contact.email}'): ").strip()
                new_address = input(f"Enter new address for '{contact.name}' (press enter to keep '{contact.address}'): ").strip()
                
                if new_name:
                    contact.name = new_name
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                
                print(f"Contact '{contact.name}' updated successfully.")
                found = True
                break
        
        if not found:
            print(f"No contacts found with '{search_term}'.")
    
    def delete_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                self.contacts.remove(contact)
                print(f"Contact '{contact.name}' deleted successfully.")
                found = True
                break
        
        if not found:
            print("No contacts found with '{search_term}'.")
    
    def menu(self):
        while True:
            print("\n----- Contact Book Menu -----")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                name = input("Enter name: ").strip()
                phone_number = input("Enter phone number: ").strip()
                email = input("Enter email: ").strip()
                address = input("Enter address: ").strip()
                new_contact = Contact(name, phone_number, email, address)
                self.add_contact(new_contact)
            
            elif choice == '2':
                self.view_contacts()
            
            elif choice == '3':
                search_term = input("Enter name or phone number to search: ").strip()
                self.search_contact(search_term)
            
            elif choice == '4':
                search_term = input("Enter name or phone number to update: ").strip()
                self.update_contact(search_term)
            
            elif choice == '5':
                search_term = input("Enter name or phone number to delete: ").strip()
                self.delete_contact(search_term)
            
            elif choice == '6':
                print("Exiting Contact Book. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

# Running the Contact Book application
if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu()