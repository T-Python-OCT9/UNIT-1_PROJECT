num = int(input("Enter how many contact do you want to add:"))
contact_name = []
contact_num = []

def adding_contact():
    for i in range(1, num + 1):
        name = input("\nEnter the contact name:")
        check_name_staut(name)
        phone_number = int(input("Enter the contact phone number starts with 966:"))
        check_phone_num_status(phone_number)
        print("The Contact has been added successufully!")
    print(f"The contact name is: {contact_name}")
    print(f"The contact number is: {contact_num}")


def check_name_staut(user_name):
    if isinstance(user_name, str):
        contact_name.append(user_name)
    else:
        raise ValueError("The contact name must be a String!!")

def check_phone_num_status(user_number : int):
    if isinstance(user_number, int) and len(str(user_number)) == 12:
        contact_num.append(user_number)
    else:
        raise ValueError("The contact phone number must be a intger and 12")
    
adding_contact()