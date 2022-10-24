#import classes
import CoffeeMethod as coffee
import Buy


#main class
#explain programming for user
print("_"*50)
print("\nHi, this is a coffee machine\nWe have some coffee here\n")

#Dictionary for coffee menue
print("\t\tMenu")
coffeeDictionary={"Cappuccino":16,
    "Latte\t":16,
    "Espresso":10,
    "Americano":11,
    "Coffee Mocha":16,
    "Hotchocolate":15}
#list coffee menue
item_coffee=coffeeDictionary.items()
coffee.coffee_menu(item_coffee)


#lambda 
tax_calculation=lambda price_lambda:price_lambda+(price_lambda*0.15)

#To start program
start=input("\nPress \"*\" to start order your coffee:\n")

#start loop
while(start=="*"):
    print("-"*50)
    #to choice from menu
    print("\nFor Cappuccino press \'1\'\nFor Latte press \'2\'\nFor Espresso Press \'3\'\nFor Americano press \'4\'\nFor Coffee Mocha press \'5\'\nFor Hotchocolate press \'6\'")
    choice=input("\nChoose coffee you want please:\n")
    #Take value from user and test if have error of not
    try:
        price=coffee.coffeePrice(choice)
        coffee_name=coffee.coffeeName(choice)
        print(f"The price is : {price} SR")
    except ValueError as error:
        print(error)
        break
    print("-"*50)
    #Ask user to complete buy or cancel or change 
    complete_order=input("\nDo you want to complete your order ?\n\nPress \"Y\" to continue \nPress \"N\" to cancel\nPress \"H\" to change:\n")
    #To complete order
    if complete_order=="y"or complete_order=="Y":
        print("-"*50)
        #Ask user to choice to buy
        print("\nChoose how to pay: \n** If you pay from card you will have '20%' discount ")
        buy=input("Press \'1\' for card or \'2\' for cash: \n")
        #If user choice buy from card
        if buy=="1":
            #to calculator price
            card_buy=Buy.Card(price)
            discount_price=card_buy.printInfo()
            print("-"*50)
            #print order and calculator price after discount and calculator tax
            print(f"\nYour order is {coffee_name}\nThe price after discount : {discount_price}SR\nThe price after add the tax : {tax_calculation(discount_price)}SR\n")
            #Ask to enter card and buy
            complete_with_card= input("Choose \"C\" to pass your credit card on the screan \nChoose \"N\" to cancel")
            #to enter card and buy
            if complete_with_card=="c" or complete_with_card=="C":
                print("-"*50)
                #end do coffee
                print(f"\nYour coffee {coffee_name} is ready, take it please ")
                print(f"\nEnjoy with your coffee\n") 
                #Ask user if want another order
                start=input("\nDo you want order another coffee ? \n\nTo order another coffee press \"*\" \nTo exit press N \n")
            #To cancel order
            elif complete_with_card=="n" or complete_with_card=="N":
                print("-"*50)   
                print(f"\nThank you for use coffee machine\n\n")   
                break
            #If user put incorrect value
            else:
                print("-"*50)
                print("\nYou enter incorrect value, make a new order\n")
        #If user choice buy cash      
        elif buy=="2":
            print("-"*50)
            #Print information of order
            print(f"\nYour order is {coffee_name}\nThe price: {price} SR\nAfter add the tax {tax_calculation(price)} SR")
            #Ask user to enter his mony
            user_m=input("Enter your money: \n")
            #Take value from user and test if have error of not
            try:
                cash_buy=Buy.Cash(price,float(user_m))
                money_p:float=cash_buy.printInfo()
            except TypeError as error:
                print(error)
                break
            #Information discount price 
            ronund_price=round(money_p,2)
            print(f"\nTotal amount {tax_calculation(price)} SR\nRemmaining: {ronund_price} SR\nTake the change please")
            ##end do coffee
            print(f"\nYour coffee {coffee_name} is ready, take it please ")  
            print(f"\nEnjoy with your coffee\n")   
            #Ask user if want another order
            start=input("Do you want order another coffee ? \n\nTo order press \"*\" \nTo exit press N \n")
        #if user enter another choice or incorrect value
        else:
            print("-"*50)
            print("\nYou enter incorrect value, make a new order\n")
    #To change order      
    elif complete_order=="h" or complete_order=="H" :
        pass
    #To cancel order
    elif complete_order=="n" or complete_order=="N":
        print("-"*50)   
        print(f"\nThank you for use coffee machine\n\n")   
        break
    #If user enter incorrect choice 
    else:
        print("-"*50)
        print("\nYou enter incorrect value, make a new order\n")
#end loop 
print("-"*50) 
print(f"\nEnd Programming\n")









