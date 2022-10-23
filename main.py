from searchContact import *
def contactBookApp():
    while True:
        start_proj = input("Do you want to enter the app? write <y> for yes or <n> for no:")
        if start_proj.lower == "y":
            new_contact = input("Do you want to add new contact? write <y> for yes or <n> for no:")
            if new_contact.lower == "y":
                adding_contact()
            elif new_contact.lower == "n":
                printing_the_lists = input("Do you want to print the contact book? write <y> for yes or <n> for no:")
                if printing_the_lists.lower == "y":
                    printingContactBook()
                elif printing_the_lists.lower == "n":
                    exit_app = input("Do you want to close the app? write <y> for yes or <n> for no:")
                    if exit_app.lower == "y":
                        break
                    elif exit_app.lower == "n": 
                        continue
                    else: 
                        print("Sorry you have enterd invaild value! please try again")
                        continue
                else: 
                    print("Sorry you have enterd invaild value! please try again")
                    continue
            else: 
                    print("Sorry you have enterd invaild value! please try again")
                    continue
        elif start_proj.lower == "n":
            break
        else:
            print("Sorry you have enterd invaild value! please try again")
            continue

            


