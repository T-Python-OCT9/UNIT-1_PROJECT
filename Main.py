
#Greeting
from Items import coffee_Drinks

Customer = str(input("Hi , Please type your name : "))
print(f" Welcome {Customer} Can I take your order?")

ask_for_order = input("Please type Y if you ready or N if not yet  :") 
if ask_for_order == "y":
  print("please check the menu and let us know your orders")
  items = []
  q=[]
  cost = [0]

  def invoice (x:list,y:list) : 
    print (f" Your items are : \n {x} the qauantity {y} \n")
    '''Total = 0 
    for i in y:
        Total += y 
    print(f"the total a mount is {y} RS" )'''
 
 
  done = False


  while not done:
    print("C - Coffee")
    print("S - Sandwich")
    print("K - Cake")
    print("O - Checkout")
    print("Q - Quit")
    choice = input(":: ")
    if choice == "c" or choice == "C":
        print("Coffee Menu")
        print("B - Black Coffee")
        print("F - Flat white")
        print("E - espresso")
        print("M - macchiato")
        print("C - cappuccino")
        print("H - Hot_Chocolate")
        print("L - latte")
        print("Q - Quit")
        item = input("type your choise : ")
              
        if item == "B" or item == "b":
            Q=int(input("How many items you want ? : "))
            items.append("Black_Coffee") 
            q.append(Q)
            print("the black coffee has been added to your cart")
        elif item == "F" or item == "f":
            Q=int(input("How many items you want ? : "))
            items.append("Flat white") 
            q.append(Q)
            print("the flat white has been added to your cart")
        elif item == "E" or item == "e":
            Q=int(input("How many items you want ? : "))
            items.append("Espresso") 
            q.append(Q)
            print("the Espresso has been added to your cart")
        elif item == "M" or item == "m":
            Q=int(input("How many items you want ? : "))
            items.append("Macchiato") 
            q.append(Q)
            print("the Macchiato has been added to your cart")
        elif item == "C" or item == "c":
            Q=int(input("How many items you want ? : "))
            items.append("coppuccino") 
            q.append(Q)
            print("the cappuccino has been added to your cart")
        elif item == "H" or item == "h":
            Q=int(input("How many items you want ? : "))
            items.append("Chocolate") 
            q.append(Q)
            print("the Hot Chocolate has been added to your cart")
        elif item == "L" or item == "l":
            Q=int(input("How many items you want ? : "))
            items.append("Latte")
            q.append(Q) 
            print("the Hot latte has been added to your cart")
        else:
            continue 
        
    elif choice == "S" or choice == "s":
        print("Sandwich Menu")
        print("C - Chicken Sandwich")
        print("N - Nutella Sandwich")
        print("E - Egg Sandwich")
        print("Q - Quit")
        item = input("type your choise")
        if item == "C" or item == "c":
            Q=int(input("How many items you want ? : "))
            items.append("Chicken Sandwich") 
            q.append(Q)
            print("the Chicken Sandwich has been added to your cart")
        elif item == "N" or item == "n":
            Q=int(input("How many items you want ? : "))
            items.append("Nutella Sandwich") 
            q.append(Q)
            print("the Nutella Sandwich has been added to your cart")
        elif item == "E" or item == "e":
            Q=int(input("How many items you want ? : "))
            items.append("Egg Sandwich") 
            q.append(Q)
            print("the Egg Sandwich has been added to your cart")
        else:
            continue
        
    elif choice == "K" or choice == "k":
        print("cake Menu")
        print("C - cheesecake")
        print("O - Cookie")
        print("B - brownies")
        print("Q - Quit")
        item = input("type your choise")

        if item == "C" or item == "c":
            Q=int(input("How many items you want ? : "))
            items.append("cheesecake") 
            q.append(Q)
            print("the cheesecake has been added to your cart")
        elif item == "O" or item == "o":
            Q=int(input("How many items you want ? : "))
            items.append("Cookie") 
            q.append(Q)
            print("the Cookie has been added to your cart")
        elif item == "B" or item == "b":
            Q=int(input("How many items you want ? : "))
            items.append("brownies") 
            q.append(Q)
            print("the brownies has been added to your cart")
        else:
            continue

    #checkOut
    elif choice == "O" or choice == "o" :
        invoice(items,q)
    
    #For Quit
    elif choice == "Q" or choice == "q" :
        print("Quit!")
        done = True
    else:
        print("Invalid Choice")
        
elif ask_for_order == "n":
    need_help = input("Do you want any help for choose your coffee ? write y for yes and n for no")
    if need_help == "y":
        pass
    elif need_help == "n":
        pass




