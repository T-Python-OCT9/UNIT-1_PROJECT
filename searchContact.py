from addingContact import *

def printingContactBook():
    for i in range():
        print("{}\t\t\t{}".format(contact_name[i], contact_num[i]))

search_contact = input("\nEnter the contact name: ")

print("Search result:")

if search_contact in contact_name:
    index = contact_name.index(search_contact)
    print(index)
    phone_number = contact_num[index]
    print("Name: {}, Phone Number: {}".format(search_contact, phone_number))

else:
    print("Name Not Found!")