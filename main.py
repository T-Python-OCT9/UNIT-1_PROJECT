from User import *

print("\n( Coffee Up )")
print("A perfect day ends with a Coffee Up ...")
print("_" * 40 +"\n")

while True:

    UserName = input("Please enter your name: ")
    print(f"Welcom {UserName.upper()} to our coffee up shop ...\n")
    User1 = User()
    
    while True:
        print("Coffee Up List:")
        file = open("list.txt", "r", encoding="utf-8")
        list = file.read()
        print(list)
        file.close()
        print()
        try:
            Selection = int(input("Make your selection: "))
        except ValueError :
            print("You did not make a valid selection.")

        
        if Selection == 1:
            print()
            print("-------View Coffee List-------")
            User1.View_Coffee_list()
            print("-------------------------------\n")
            #User1.View_Cart_Item()
        elif Selection == 2:
            print()
            print("-----------Add Item-----------")
            User1.View_Coffee_list()
            print()
            User1.Add_Item()
        elif Selection == 3:
            print()
            print("----------Remove Item----------")
            User1.Remove_Item()
        elif Selection == 4:
            print()
            print("--------View Cart Item--------")
            User1.View_Cart_Item()
        elif Selection == 5:
            print()
            print("------------Receipt------------")
            User1.Receipt()
        elif Selection == 6:
            User1.Clear_List()
        elif Selection == 7:
            print("\nHope to see you back soon!\n")
            break
        else:
            print("Enter the valid number.")
    User1.Clear_List()    
    More_User = input("Do you have anther user yes or no? ")
    if More_User.lower() == "yes":
        pass
    else:
        break


