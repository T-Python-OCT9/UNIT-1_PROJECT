
def invoice (x:list,y:list)  -> list:
    answer = input ("Do you want to add anything else? : please press y for yes and n for no ")
    if answer.lower == "y":
        menu()
    elif answer.lower == "n":
        print("We will proceed to checkout  : ")
        print_invoice(x,y)

def print_invoice(x :list, y:list):
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
            
    answer = input("Please press C to confirm or E for edit your order  :")
            # we need to add quantity?
    if answer.lower == "c":
        checkout(order)
        #open file to save the order      
        
    elif answer.lower == "e":
        answer = input("Do want add or remove items ? : please type A for add , R for remove or D if Done  : ")
        done = False
        while not done:
          if answer.lower == "a":
            menu()
          elif answer.lower == "r":
            delete_item = input("please type the item")
            del order[delete_item]
            checkout(order)
          elif answer.lower == "d":
            checkout(order)
            done = True  
            # we need to give chance for customer to delete or add new items 
        answer_2 = print("This is your invoice after changes .. let us to complete your order ? : type y if yes and n for no")
        if answer_2.lower ==  "y":
            checkout(order)

            #checkout
        elif answer_2.lower == "n":
            menu()

def checkout(x:dict):
    file = open('orders.txt', "a+", encoding="utf-8")
    file.write(f"This is your orders {x}\n ")
    file.close()
    print("the order has been completed")
    menu()