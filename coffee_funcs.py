import project_main 

# this function take the order and ask customr to confirm order to proceed the next step
def invoice (x:list,y:list)  -> list:
    answer = input ("Do you want to add anything else? : please press y for yes and n for no ")
    if answer == "y" or answer == "Y":
      print("Back to menu")
      project_main.menu()
    elif answer == "n" or answer == "N":
      print("We will proceed to checkout .... ")
      print_invoice(x)
    else : 
        print("there is somthing wrong please let us start again ")
        project_main.menu()
    
    
# this function will print the invoice  
def print_invoice(x :list):
    menu_1 = {"Black_Coffee_M" : 10 , "Black_Coffee_S": 7, "Flat white_M" :15 , "Flat white_S" :12, "Espresso_M" :10 , "Espresso_S" :8 , "Macchiato_M" :18 , "Macchiato_S":15, "coppuccino_M":18 , "coppuccino_S":15, "Hot_Chocolate_M":18 , "Hot_Chocolate_S" :16, "Latte_M":16 ,"Latte_S" :14, "Chicken Sandwich":12 , "Nutella Sandwich" : 11,"Egg Sandwich" : 12, "cheesecake" : 25 , "Cookie" : 6, "brownies" :8 } 
    print(" Your invoice")
    print("  Item :                Price :")
    order = {}
    for i in x : 
        if i in menu_1:
            print(f"- {(i)} ***** : {(menu_1[i])} RS")
            item = {i : menu_1[i] }
            order.update(item)
        else: 
            print("Your cart is empty")
    
    total = sum(order.values())  
    print(f"The total amount is : {total} RS")  
             
    answer = input("Please press C to checkout or E for edit your order  :")
            # we need to add quantity?
    if answer == "c" or answer == "C" :
        checkout(order)
        #open file to save the order      
    elif answer == "e" or answer == "E":
        answer = input("Do want add or remove items ? : please type A for add , R for remove or D if Done  : ")
        done = False
        while not done:
          if answer == "a" or answer == "A":
            project_main.menu()
          elif answer == "r" or answer == "B":
            delete_item = input("please type the item  : ")
            del order[delete_item]
            print(f"this item : {delete_item} has been deleted")
            print("Please check your order after changes ")
            print_invoice(order)
          elif answer == "d" or answer == "D":
            checkout(order)
            done = True  

# This fun to complete the order and log it in customer file 
def checkout(x:dict):
    file = open('orders.txt', "a+", encoding="utf-8")
    file.write(f"This is your orders {x}\n ")
    file.close()
    print("the order has been completed")
    return
    #project_main.menu()