    
# this function will print the invoice  
def print_invoice(x :list ,y:str):
    menu_1 = {"Black_Coffee_M" : 10 , "Black_Coffee_S": 7, "Flat white_M" :15 , "Flat white_S" :12, "Espresso_M" :10 , "Espresso_S" :8 , "Macchiato_M" :18 , "Macchiato_S":15, "coppuccino_M":18 , "coppuccino_S":15, "Hot_Chocolate_M":18 , "Hot_Chocolate_S" :16, "Latte_M":16 ,"Latte_S" :14, "Chicken Sandwich":12 , "Nutella Sandwich" : 11,"Egg Sandwich" : 12, "cheesecake" : 25 , "Cookie" : 6, "brownies" :8 } 
    print(" Your invoice")
    print("  Item :                Price :")
    order = {}
    print(f"- {(i)} ***** : {(menu_1[i])} RS")
    for i in x:
      if (i in menu_1 and i not in order):
        item= {i : menu_1[i] }
        order.update(item)
      elif (i in menu_1 and i in order):
        item = { "~~" : menu_1[i] }
        order.update(item)
            #print(f"- {(i)} ***** : {(menu_1[i])} RS")
            #print (order)
    file = open(f'{y}.txt', "a+", encoding="utf-8")
    file.write(f"This is the cart of {y} order \n {x}\n ")
    file.close()
    total = sum(order.values())  
    print(f"The total amount is : {total} RS")  
    answer = input("Please press C to checkout or E for edit your order  :")
            # we need to add quantity?
    if answer == "c" or answer == "C" :
        checkout(order)
        #open file to save the order      
    elif answer == "e" or answer == "E":
        answer = input("Do want add or remove items ? : please type A to change the order , R for remove some items or D to complete your order  : ")
        done = False
        while not done:
          if answer == "a" or answer == "A":
            return
            #project_main.menu()
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