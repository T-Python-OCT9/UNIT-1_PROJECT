from operator import index
from unicodedata import name


class Contact:
    def __init__(self, name : str, phone_num : int) -> None:
        self.phone_num = phone_num
        self.name = name

    def setName(self, Name):
        if not (isinstance(Name, str)):
            raise ValueError("Name is must be a string!")
        else:
            self.name = Name
    
    def setNum(self, Phone_number):
        
        if not (isinstance(Phone_number, int) and len(str(Phone_number))) == 12:
            raise ValueError("Number is must be intger and 12 digits!")
        else:
            self.Phone_num = Phone_number
    
    def getNum(self):
        return self.phone_num

    def getName(self):
        return self.name

    def newContact(self):
        num = int(input("Enter how many contact do you want to add:"))
        for i in range(1, num + 1):
            name = input("\nEnter the contact name:")
            self.name = name
            if isinstance(self.name, str):
                contact_name.append(self.name)
            else:
                raise ValueError("The contact name must be a String!!")
            phone_number = int(input("Enter the contact phone number starts with 966:"))
            self.phone_num = phone_number
            if isinstance(self.phone_num, int) and len(str(self.phone_num)) == 12:
                contact_num.append(self.phone_num)
            else:
                raise ValueError("The contact phone number must be a intger and 12 digits")
            print("The Contact has been added successufully!")
            print(f"The contact name is: {contact_name[i - 1]}")
            print(f"The contact number is: {contact_num[i - 1]}")
        
        

    def printingContactBook(self):
        print(f"Name \t\t\t Number")
        for i in contact_name:
            x = contact_name.index(i)
            print("{}\t\t\t{}".format(i,contact_num[x]))

    def searchingContact(self):
        search_contact = input("\nEnter the contact name: ")
        print("Search result:")
        if search_contact in contact_name:
            index = contact_name.index(search_contact)
            print(index)
            phone_number = contact_num[index]
            print("Name: {}\t\t\tPhone Number: {}".format(search_contact, phone_number))
        else:
            print("Name Not Found!")
    

contact_name = []
contact_num = []
welcome_phrase = lambda object : print(f"Welcome {object.name} to my app")