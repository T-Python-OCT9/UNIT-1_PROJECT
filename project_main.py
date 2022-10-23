import coffee_funcs 

#Greeting

Customer = str(input("Hi , Please type your name : "))
print(f" Welcome {Customer} Can I take your order?")

# main_ menu
def menu() -> list :
  print("please check the menu and let us know your orders")
  menu = {"Black_Coffee_M" : 10 , "Black_Coffee_S": 7, "Flat white_M" :15 , "Flat white_S" :12, "Espresso_M" :10 , "Espresso_S" :8 , "Macchiato_M" :18 , "Macchiato_S":15, "coppuccino_M":18 , "coppuccino_S":15, "Hot_Chocolate_M":18 , "Hot_Chocolate_S" :16, "Latte_M":16 ,"Latte_S" :14, "Chicken Sandwich":12 , "Nutella Sandwich" : 11,"Egg Sandwich" : 12, "cheesecake" : 25 , "Cookie" : 6, "brownies" :8 } 
  items = []
  q=[]
  z=[]
  cost = [0]
  done = False
  while not done:
    print("C - Coffee")
    print("S - Sandwich")
    print("K - Cake")
    print("Q - Checkout")
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
        item = input("choose your order: ")
              
        if item == "B" or item == "b":
            Z= input ("please choose the size : M for medium and S for small ")
            if Z == "M" or Z == "m" :      
              items.append("Black_Coffee_M")
            elif Z== "S" or Z == "s":
              items.append("Black_Coffee_S")
            Q=int(input("How many items you want ? : "))
            q.append(Q)
            print("the black coffee has been added to your cart, Do you need anythings else ? :")
        elif item == "F" or item == "f":
            Z= input ("please choose the size : M for medium and S for small ")
            if Z == "M" or Z == "m" :      
              items.append("Flat white_M")
            elif Z== "S" or Z == "s":
              items.append("Flat white_S")
            Q=int(input("How many items you want ? : "))
            q.append(Q)
            print("the flat white has been added to your cart Do you need anythings else ? :")
        elif item == "E" or item == "e":
            Z= input ("please choose the size : M for medium and S for small ")
            if Z == "M" or Z == "m" :      
              items.append("Espresso_M")
            elif Z== "S" or Z == "s":
              items.append("Espresso_S")
            Q=int(input("How many items you want ? : "))
            q.append(Q)
            print("the Espresso has been added to your cart Do you need anythings else ? :")
        elif item == "M" or item == "m":
            Z= input ("please choose the size : M for medium and S for small ")
            if Z == "M" or Z == "m" :      
              items.append("Macchiato_M")
            elif Z== "S" or Z == "s":
              items.append("Macchiato_S")
            Q=int(input("How many items you want ? : "))
            q.append(Q)
            print("the Macchiato has been added to your cart Do you need anythings else ? :")
        elif item == "C" or item == "c":
            Z= input ("please choose the size : M for medium and S for small ")
            if Z == "M" or Z == "m" :      
              items.append("coppuccino_M")
            elif Z== "S" or Z == "s":
              items.append("coppuccino_S")
            Q=int(input("How many items you want ? : "))
            q.append(Q)
            print("the cappuccino has been added to your cart Do you need anythings else ? :")
        elif item == "H" or item == "h":
            Z= input ("please choose the size : M for medium and S for small ")
            if Z == "M" or Z == "m" :      
              items.append("Hot_Chocolate_M")
            elif Z== "S" or Z == "s":
              items.append("Hot_Chocolate_S")
            Q=int(input("How many items you want ? : "))
            q.append(Q)
            print("the Hot Chocolate has been added to your cart Do you need anythings else ? :")
        elif item == "L" or item == "l":
            Z= input ("please choose the size : M for medium and S for small ")
            if Z == "M" or Z == "m" :      
              items.append("Latte_M")
            elif Z == "S" or Z == "s":
              items.append("Latte_S")
            Q=int(input("How many items you want ? : "))
            q.append(Q) 
            print("the Hot latte has been added to your cart, Do you need anythings else ? :")
       
        
    elif choice == "S" or choice == "s":
        print("Sandwich Menu")
        print("C - Chicken Sandwich")
        print("N - Nutella Sandwich")
        print("E - Egg Sandwich")
        print("Q - Quit")
        item = input("choose your order: ")
        if item == "C" or item == "c":
            Q=int(input("How many items you want ? : "))
            items.append("Chicken Sandwich") 
            q.append(Q)
            print("the Chicken Sandwich has been added to your cart , Do you need anythings else ? :")
        elif item == "N" or item == "n":
            Q=int(input("How many items you want ? : "))
            items.append("Nutella Sandwich") 
            q.append(Q)
            print("the Nutella Sandwich has been added to your cart , Do you need anythings else ? :")
        elif item == "E" or item == "e":
            Q=int(input("How many items you want ? : "))
            items.append("Egg Sandwich") 
            q.append(Q)
            print("the Egg Sandwich has been added to your cart , Do you need anythings else ? :")
       
        
    elif choice == "K" or choice == "k":
        print("cake Menu")
        print("C - cheesecake")
        print("O - Cookie")
        print("B - brownies")
        print("Q - Quit")
        item = input("choose your order: ")

        if item == "C" or item == "c":
            Q=int(input("How many items you want ? : "))
            items.append("cheesecake") 
            q.append(Q)
            print("the cheesecake has been added to your cart , Do you need anythings else ? :")
        elif item == "O" or item == "o":
            Q=int(input("How many items you want ? : "))
            items.append("Cookie") 
            q.append(Q)
            print("the Cookie has been added to your cart , Do you need anythings else ? :")
        elif item == "B" or item == "b":
            Q=int(input("How many items you want ? : "))
            items.append("brownies") 
            q.append(Q)
            print("the brownies has been added to your cart , Do you need anythings else ? :")
        #checkOut
    elif choice == "Q" or choice == "q" :
        
        print("Let us proceed to checkout!")
        coffee_funcs.invoice(items, q) 
        done = True    
    else:
        print("Invalid Choice")




cart = menu()


#elif ask_for_order == "n":
 #   need_help = input("Do you want any help for choose your coffee ? write y for yes and n for no")
  #  if need_help == "y":
   #     pass
    #elif need_help == "n":
     #   pass




