

store = [{"id": 1001, "Name": "HP", "Available": 100, "Price": 2500},
            {"id": 1002, "Name": "DELL", "Available": 100, "Price": 3500},
            {"id": 1003, "Name": "ASUS", "Available": 100, "Price": 2800},
            {"id": 1004, "Name": "APPLE", "Available": 100, "Price": 6000},
            {"id": 1005, "Name": "ACER", "Available": 100, "Price": 2400},
            {"id": 1006, "Name": "SAMSUNG", "Available": 100, "Price": 3500}]


def DisplayMenuAdmin():
    print("Id\tName\tAvailable\tPrice")
    print("-----------------")
    for d in store:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
    
    adminWindow()
    adminOptions()

def DisplayMenu():
    print("Id\tName\tAvailable\tPrice")
    print("-----------------")
    for d in store:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
    
    userLoginWindow()
    userChoiceOptions()


def addproducts():
    n = int(input("Enter the items need to be added : "))
    for i in range(n):
        new_id = int(input("Enter id : "))
        new_Name = input("Enter Name : ")
        new_Available = int(input("Enter Available : "))
        new_Price = int(input("Enter Price : "))
        d = [{"id": new_id, "Name": new_Name, "Available": new_Available, "Price": new_Price}]
        store.extend(d)
        DisplayMenuAdmin()

temp=[]

def removeproducts():
    i = int(input("Enter the id need to be deleted : "))
    for d in store:
        found = d["id"] == i
        if found == False:
            temp.append(d)
            continue
        if found == True:
            d["Available"] -= 1
    print("Deleting item....")
    if len(temp) == d:
        print(f"{i} not found")
    else:
        print(f"{i}'s one available is removed from the list")
    DisplayMenuAdmin()


def adminWindow():
    print("-------------------")
    print("1.Display Menu")
    print("2.Add Product")
    print("3.Remove Product")
    print("4.Logout")
    print("-------------------")



def adminOptions():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        DisplayMenuAdmin()
    elif choice == 2:
        addproducts()
    elif choice == 3:
        removeproducts()
    elif choice == 4:
        login()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n--------------\n")
        adminWindow()
        print("\n---------------\n")
        adminOptions()

def userChoiceOptions():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        DisplayMenu()
    if choice == 2:
        buyOrder()   
    elif choice == 3:
        login()
    else:
        print("Invalid Choice. Please enter valid choice")

def buyOrder():
    
    buy_id = int(input("\nTo buy enter id : "))
    
    for d in store:
        
        if d["id"] == buy_id:
            print("\nId\tName\tPrice")
            print("----------------------")
            print(f'{d["id"]}\t{d["Name"]}\t{d["Price"]}')
            print()
            print("Purchased successfully")
            print("-----------------------")
        

def userLoginWindow():
    print("----------------\n")
    print("1.Display Menu")
    print("2.Buy order")
    print("3.Logout")
    print("\n------------------")

def login():
    log_in = input("login admin / login user [a/u] :")
    if log_in == "a":
        pwd = input("Enter password : ")
        if pwd == "admin":
            adminWindow()
            adminOptions()
        else:
            print("Invalid password. Please enter valid password")
    elif log_in == "u":
       userLoginWindow()
       userChoiceOptions()
            
    else:
        print("Invalid password. Please enter valid password")


login()


