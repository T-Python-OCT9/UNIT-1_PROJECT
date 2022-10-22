

from calendar import c


x={"Black_Coffee_M" : 7 , "Black_Coffee_S" : 15}
z=["Black_Coffee_M" , "Black_Coffee_S"]
y =[7,15]


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
    
        
    
    def confirm (x:dict):
      answer = input("Please press C to confirm or A / R to add or remove item  :  ")
            # we need to add quantity?
      if answer.lower == "c":
        print(answer)        
      elif answer.lower == "a":
        pass
      elif answer.lower == "r":
        delete_item = input("please type the item")
        del order[delete_item]
        print("item has been deleted")
    
    checkout(order) 
            # we need to give chance for customer to delete or add new items 

def checkout(x:dict):
    file = open('orders.txt', "a+", encoding="utf-8")
    file.write(f"This is your orders {x}\n ")
    file.close()
    print("the order has been completed")
    return

print_invoice(z,y)
confirm(order)
