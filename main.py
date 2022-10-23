#import classes
import CoffeeType as coffee
import Classes


#main class
#explain programming for user
print("_"*50)
print("\nHi, this is coffee machine, we have past coffee her\nTo order you must chose to start\"*\"\nTo chose your coffee enter number of coffee\nTo complete your order enter \"y \"\nTo chang your order enter \"h\"\nTo cansel your order enter \"n\"\nNow we will list the menue:\n")

#Dictionary for coffee menue
coffeeDictionary={"coffee1":15,
    "coffee2":13 ,
    "coffee3":12,
    "coffee4":14,
    "coffee5":16,
    "coffee6":15}
#list coffee menue
item_coffee=coffeeDictionary.items()
coffee.coffee_menu(item_coffee)


#lambda 
tax_calculation=lambda price_lambda:price_lambda+(price_lambda*0.15)

#To start program
start=input("\nIf you want drink coffee enter \"*\"\n")

#start loop
while(start=="*"):
    print("-"*50)
    #to choice from menu
    print("\nTo choice coffee1 enter \"1\"\nTo choice coffee2 enter \"2\"\nTo choice coffee3 enter \"3\"\nTo choice coffee4 enter \"4\"\nTo choice coffee5 enter \"5\"\nTo choice coffee6 enter \"6\"")
    choice=input("Choice coffee you want plese:")
    #Take value from user and test if have error of not
    try:
        price=coffee.coffeePrice(choice)
        coffee_name=coffee.coffeeName(choice)
        print(f"price is : {price}")
    except ValueError as error:
        print(error)
        break
    print("-"*50)
    #Ask user to complete buy or cancel or change 
    complete_order=input("if you want to complete your order enter \"y\",if you want to cancel your order enter\"n\", if you want to change your order enter \"h\":\n")
    #To complete order
    if complete_order=="y"or complete_order=="Y":
        print("-"*50)
        #Ask user to choice to buy
        print("How do you want to \'?\'\n*Note, If you buy from card you will have discount 20%")
        buy=input("enter \"1\" to chose card or \"2\" to cash: \n")
        #If user choice buy from card
        if buy=="1":
            #to calculator price
            card_buy=Classes.Card(price)
            discount_price=card_buy.printInfo()
            print("-"*50)
            #print order and calculator price after discount and calculator tax
            print(f"Your order is {coffee_name} and the price after discount is {discount_price}, The price after calculator tax is {tax_calculation(discount_price)}")
            #Ask to enter card and buy
            complete_with_card= input("Choose c to , if you want to cancel enter n, if you want to change enter h:\n")
            #to enter card and buy
            if complete_with_card=="c" or complete_with_card=="C":
                #end do coffee
                print(f"your coffee {coffee_name} is ready, take it pleas ")
                #Ask user if want another order
                start=input("do you want order another coffee ? if you want enter \"*\" if you do not enter no")
                print("-"*50)
            #To cancel order
            elif complete_with_card=="n" or complete_with_card=="N":
                break
            #To change order
            elif complete_with_card=="*" :
                pass
            #If user put incorrect value
            else:
                print("-"*50)
                print("you enter incorrect value, sory you will go back to star")
        #If user choice buy cash      
        elif buy=="2":
            print("-"*50)
            #Print information of order
            print(f"Your order is {coffee_name}, the price after calculator tax is {tax_calculation(price)}")
            #Ask user to enter his mony
            user_m=input("enter your mony plese: \n")
            #Take value from user and test if have error of not
            try:
                cash_buy=Classes.Cash(price,float(user_m))
                mouny_p:float=cash_buy.printInfo()
            except TypeError as error:
                print(error)
                break
            #Information discount price 
            print(f"The mony after discount price is {mouny_p}\nTake \'?\'")
            ##end do coffee
            print(f"your coffee {coffee_name} is ready, take it pleas ")
            #Ask user if want another order
            start=input("do you want order another coffee ? if you want enter \"*\" if you do not enter no")
            print("-"*50)
        #if user enter another choice or incorrect value
        else:
            print("-"*50)
            print("you enter incorrect value, sory you will go back to star")
    #To change order      
    elif complete_order=="h" or complete_order=="H" :
        pass
    #To cancel order
    elif complete_order=="n" or complete_order=="N":
        break
    #If user enter incorrect choice 
    else:
        print("-"*50)
        print("you enter incorrect value, sory you will go back to star")
        

print("Thank you for use coffee machine")








