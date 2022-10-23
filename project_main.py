from coffee_funcs import *
from Items import * 
#Greeting

Customer = str(input("Hi , Please type your name : "))


# main_ menu
def menu(x:str) -> list :
  input("press anything to start")
  print(f" Welcome {x} Can I take your order?")
  print("please check the menu and let us know your orders")
  menu1 = {"Black_Coffee_M" : 10 , "Black_Coffee_S": 7, "Flat white_M" :15 , "Flat white_S" :12, "Espresso_M" :10 , "Espresso_S" :8 , "Macchiato_M" :18 , "Macchiato_S":15, "coppuccino_M":18 , "coppuccino_S":15, "Hot_Chocolate_M":18 , "Hot_Chocolate_S" :16, "Latte_M":16 ,"Latte_S" :14, "Chicken Sandwich":12 , "Nutella Sandwich" : 11,"Egg Sandwich" : 12, "cheesecake" : 25 , "Cookie" : 6, "brownies" :8 } 
  items = []
  q=[]
  done = False
  while not done:
    print("C - Coffee")
    print("S - Sandwich")
    print("K - Cake")
    print("Q - Checkout")
    print("D - Coffee type")
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
            print("the black coffee has been added to your cart, Do you need anythings else ? :")
        elif item == "F" or item == "f":
            Z= input ("please choose the size : M for medium and S for small ")
            if Z == "M" or Z == "m" :      
              items.append("Flat white_M")
            elif Z== "S" or Z == "s":
              items.append("Flat white_S")
            print("the flat white has been added to your cart Do you need anythings else ? :")
        elif item == "E" or item == "e":
            Z= input ("please choose the size : M for medium and S for small ")
            if Z == "M" or Z == "m" :      
              items.append("Espresso_M")
            elif Z== "S" or Z == "s":
              items.append("Espresso_S")
            print("the Espresso has been added to your cart Do you need anythings else ? :")
        elif item == "M" or item == "m":
            Z= input ("please choose the size : M for medium and S for small ")
            if Z == "M" or Z == "m" :      
              items.append("Macchiato_M")
            elif Z== "S" or Z == "s":
              items.append("Macchiato_S")
            print("the Macchiato has been added to your cart Do you need anythings else ? :")
        elif item == "C" or item == "c":
            Z= input ("please choose the size : M for medium and S for small ")
            if Z == "M" or Z == "m" :      
              items.append("coppuccino_M")
            elif Z== "S" or Z == "s":
              items.append("coppuccino_S")
            print("the cappuccino has been added to your cart Do you need anythings else ? :")
        elif item == "H" or item == "h":
            Z= input ("please choose the size : M for medium and S for small ")
            if Z == "M" or Z == "m" :      
              items.append("Hot_Chocolate_M")
            elif Z== "S" or Z == "s":
              items.append("Hot_Chocolate_S")
            print("the Hot Chocolate has been added to your cart Do you need anythings else ? :")
        elif item == "L" or item == "l":
            Z= input ("please choose the size : M for medium and S for small ")
            if Z == "M" or Z == "m" :      
              items.append("Latte_M")
            elif Z == "S" or Z == "s":
              items.append("Latte_S")
            print("the Hot latte has been added to your cart, Do you need anythings else ? :")
       
        
    elif choice == "S" or choice == "s":
        print("Sandwich Menu")
        print("C - Chicken Sandwich")
        print("N - Nutella Sandwich")
        print("E - Egg Sandwich")
        print("Q - Quit")
        item = input("choose your order: ")
        if item == "C" or item == "c":
            Q =int(input("How many items you want ? : "))
            i=0 
            for i in range(i , Q) :
                items.append("Chicken Sandwich") 
            print("the Chicken Sandwich has been added to your cart , Do you need anythings else ? :")
        elif item == "N" or item == "n":
            Q=int(input("How many items you want ? : "))
            i=0 
            for i in range(i , Q) :
                items.append("Nutella Sandwich")
            print("the Nutella Sandwich has been added to your cart , Do you need anythings else ? :")
        elif item == "E" or item == "e":
            Q=int(input("How many items you want ? : "))
            i=0 
            for i in range(i , Q) :
                items.append("Egg Sandwich")
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
            i=0 
            for i in range(i , Q) :
                items.append("cheesecake")
            print("the cheesecake has been added to your cart , Do you need anythings else ? :")
        elif item == "O" or item == "o":
            Q=int(input("How many items you want ? : "))
            i=0 
            for i in range(i , Q) :
                items.append("Cookie")
            print("the Cookie has been added to your cart , Do you need anythings else ? :")
        elif item == "B" or item == "b":
            Q=int(input("How many items you want ? : "))
            i=0 
            for i in range(i , Q) :
                items.append("brownies")
            print("the brownies has been added to your cart , Do you need anythings else ? :")
        #checkOut
    elif choice == "Q" or choice == "q" :
        
        print("Let us proceed to checkout!")
       
        #invoice(items)
        print_invoice(items ,Customer)
        menu(Customer)
        done = True  
    elif choice == "D" or choice == "d" :
        print(" Menu")
        print("D - Description")
        print("C - calories")
        print("P - Price")
        item = input(":: ")
        if item == "D" or item == "d":
          print(f"The Description of Black Coffee is : {Black_Coffee.description}")
          print(f"The Description of Mocha is :{Mocha.description}")
          print(f"The Description of Cappuccino is :{cappuccino.description}")
          print(f"The Description of Esparesso is :{espresso.description}")
          print(f"The Description of Macchiato is {macchiato.description}")
          print(f"The Description of Hot Chocolate is {Hot_Chocolate.description}")
          print(f"The Description of Latte is {latte.description}")
          print(f"The Description of Flat White is {flat_white.description}")
        elif item == "C" or item == "c":
          print(f"The Calories of Black Coffee is : {Black_Coffee.calories}")
          print(f"The Calories of Mocha is :{Mocha.calories}")
          print(f"The Calories of Cappuccino is :{cappuccino.calories}")
          print(f"The Calories of Esparesso is :{espresso.calories}")
          print(f"The Calories of Macchiato is {macchiato.calories}")
          print(f"The Calories of Hot Chocolate is {Hot_Chocolate.calories}")
          print(f"The Calories of Latte is {latte.calories}")
          print(f"The Calories of Flat White is {flat_white.calories}")
        elif item == "P" or item == "p":
          print(f"The price of Black Coffee is : {Black_Coffee.price}")
          print(f"The price of Mocha is : {Mocha.price}")
          print(f"The price of Cappuccino is : {cappuccino.price}")
          print(f"The price of Espresso is : {espresso.price}")
          print(f"The price of Macchiato is : {macchiato.price}")
          print(f"The price of Hot Chocolate is : {Hot_Chocolate.price}")
          print(f"The price of Latte is : {latte.price}")
          print(f"The price of Flat White is : {flat_white.price}")
        input("press any thin for Back t menu")  
    else:
        print("Invalid Choice")


cart= menu(Customer)

#elif ask_for_order == "n":
 #   need_help = input("Do you want any help for choose your coffee ? write y for yes and n for no")
  #  if need_help == "y":
   #     pass
    #elif need_help == "n":
     #   pass




