from contact import *

contact1 = Contact("Admin", 966123456789)

Name = input("Please Enter your name:")
Phone_number = int(input("Please Enter your num starts with 966:"))

print(contact1.getName())
print(contact1.getNum())



contact1.setName(Name)
contact1.setNum(Phone_number)

print(f"Your name is: {contact1.getName()}")
print(f"Your number is: {contact1.getNum()}")


def contactBookApp():
    while True:
        start_proj = input("Do you want to enter the app? write <y> for yes or <n> for no:")
        if start_proj == "y":
            new_contact = input("Do you want to add new contact? write <y> for yes or <n> for no:")
            if new_contact == "y":
                contact1.newContact()
            elif new_contact == "n":
                printing_the_lists = input("Do you want to print the contact book? write <y> for yes or <n> for no:")
                if printing_the_lists == "y":
                    contact1.printingContactBook()
                elif printing_the_lists == "n":
                    search_name = input("Do you want to search about contact name? write <y> for yes or <n> for no:")
                    if search_name == "y":
                        contact1.searchingContact()
                    elif search_name == "n":
                        continue
                    else:
                        print("Sorry you have enterd invaild value! please try again")
                        continue
                else: 
                    exit_app = input("Do you want to close the app? write <y> for yes or <n> for no:")
                    if exit_app == "y":
                        break
                    elif exit_app == "n": 
                        continue
                    else: 
                        print("Sorry you have enterd invaild value! please try again")
                        continue
            else: 
                print("Sorry you have enterd invaild value! please try again")
                continue
        elif start_proj == "n":
            break
        else:
            print("Sorry you have enterd invaild value! please try again")
            continue

contactBookApp()


''''''