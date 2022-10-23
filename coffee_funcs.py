    
# this function will print the invoice  
from turtle import done


def print_invoice(x :list ,y:str):
    menu_1 = {"Black_Coffee_M" : 10 , "Black_Coffee_S": 7, "Flat white_M" :15 , "Flat white_S" :12, "Espresso_M" :10 , "Espresso_S" :8 , "Macchiato_M" :18 , "Macchiato_S":15, "coppuccino_M":18 , "coppuccino_S":15, "Hot_Chocolate_M":18 , "Hot_Chocolate_S" :16, "Latte_M":16 ,"Latte_S" :14, "Chicken Sandwich":12 , "Nutella Sandwich" : 11,"Egg Sandwich" : 12, "cheesecake" : 25 , "Cookie" : 6, "brownies" :8 } 
    print(" Your invoice")
    print("  Item :                Price :")
    order = {}
    count1=0
    count2=0
    for i in x:
      print(f"- {(i)} ***** : {(menu_1[i])} RS")
      if (i in menu_1 and i not in order):
        item= {i : menu_1[i] }
        order.update(item)
        count1=count1 +menu_1[i]
      elif (i in menu_1 and i in order):
        item= {i : menu_1[i] }
        order.update(item)
        count2=count2 +menu_1[i]

    total = sum(order.values()) 
    total2= count1 + count2
     
            #print(f"- {(i)} ***** : {(menu_1[i])} RS")
            #print (order)
    file = open(f'{y}.txt', "a+", encoding="utf-8")
    file.write(f"{y} You have these  Items in your cart  \n ")
    file.write(f" {x}\n ")
    file.close()
    
    print(f"The total amount is : {total2} RS")  
    answer = input("Please press C to checkout or E for edit your order  :")
            # we need to add quantity?
    if answer == "c" or answer == "C" :
        checkout(order,y)
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
            print_invoice(order,y)
          elif answer == "d" or answer == "D":
            checkout(order, y)
            done = True  

# This fun to complete the order and log it in customer file 
def checkout(x:dict ,y :str) -> str :
    print("the order has been completed")
    file = open('orders.csv', "a+", encoding="utf-8")
    file.write(f"the customer {y} has ordered these items  {x}\n ")
    file.close()
    Done :str = "The order has been completed"
    return Done
    
    
    #project_main.menu()