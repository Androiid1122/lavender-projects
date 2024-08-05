contact = {}

while True:
    
    option = int(input('1. Add new contact \n 2. Search contact \n 3. Display contact \n 4. Edit contact\n 5. Delete contact \n  6. Exit \n'))
    if option == 1:
        name = input('Enter the contact name')
        number = input('Enter the phonenumber')
        contact[name] = number
    elif option == 2:
        search_name = input('Enter the contact name')
        if search_name in contact:
            print(f'{search_name}')
        else:
            print(' contact not found')
    elif option == 3:
        if not contact:
            print('empty contact book')
        else:
            display_contact()
            
